#Assumptions: Account used already exists

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.action_chains import ActionChains
import os
import sys
from time import sleep
import datetime


def scrollTo(drive, element):
    '''
    Prerequisite: The element MUST exist on webpage driver
    '''
    while True:
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        sleep(2)
        try:
            return element
        except:
            continue
    
class Account():
    '''
    Account associated with fit4less account
    '''
    def __init__(self, password, emailaddress, location):
        self.password=password
        self.email=emailaddress
        self.location=location #Must be exact location
        self.countbooked=0
        self.timesbooked={}

    def getPassword(self):
        return self.password

    def getEmailAddress(self):
        return self.email

    def getLocation(self):
        return self.location

    def bookTime(self, driver): 
        alltimes_elements = driver.find_elements_by_xpath("(/html/body/div[5]/div/div/div/div/form/div[@class='available-slots'])[2]/div")\
    
        if len(alltimes_elements)==0:
            print("No times available for this date")
            return 0;

        for time in alltimes_elements:
            clock = time.get_attribute("data-slottime")[3::]
            
            print(clock)
            time_id = time.get_attribute("id")
            index_of_colon=clock.find(':')
            index_of_space=clock.find(' ')
            hour, minute = 0, 0
            hour += int(clock[:index_of_colon])
            minute = int(clock[index_of_colon+1:index_of_space])
            if clock[-2:]=="PM":
                if hour == 12:
                    pass
                else:
                    hour+=12
            elif clock[-2:]=="AM" and hour == 12:
                hour= 0
            
            #print(hour, minute)
            timegym=datetime.datetime.now().replace(hour=int(hour), minute=int(minute), second=0, microsecond=0)
            #print(timegym)
            if minrangetimegym <= timegym <= maxrangetimegym:
                #book this time
                booktime=scrollTo(driver,driver.find_element_by_id(time_id))
                booktime.click() #Click on the specifc time to book, falling in the time domain we want
                driver.find_element_by_id("dialog_book_yes").click() #Accept COVID-19 terms of service 
                print("Booked time for " + clock)
                return clock
            
        print()
        return 0

    def book(self, driver, minrangetimegym, maxrangetimegym):
        # driver = webdriver.safari.webdriver.WebDriver(quiet=False)
        # driver = webdriver.Firefox()
        #driver.maximize_window()


        # 1) Enter https://www.fit4less.ca/ > 2) Bookworkout
        try:
            driver.get('https://myfit4less.gymmanager.com/portal/login.asp')


            # 3) login
            # Find username/email box, set
            email = driver.find_element_by_name('emailaddress')
            email.send_keys(self.getEmailAddress())

            # Find password box, set
            password = driver.find_element_by_name('password')
            password.send_keys(self.getPassword())

            # Find login button, click
            driver.implicitly_wait(5)
            login_button=scrollTo(driver,driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/form/div[2]/div[1]/div'))
            login_button.click()

            # 4) Select Club: Ex: North York Centerpoint Mall

            selectclub_element=scrollTo(driver, driver.find_element_by_id('btn_club_select'))
            selectclub_element.click()
            location_element = driver.find_element_by_xpath("//div[contains(text(),'{}')]".format(self.getLocation()))
            location_element.click()


            # 5) Select Day: Ex: Tomorrow. Check todays date, select tomorrows date (Maximum of 3 days in advance)
            #driver.find_element_by_id('btn_date_select').click()
            today = datetime.date.today()
            tomorrow=today + datetime.timedelta(days = 1) 
            dayaftertomorrow=today + datetime.timedelta(days = 2) 
            days=[today.strftime("%Y-%m-%d"), tomorrow.strftime("%Y-%m-%d"), dayaftertomorrow.strftime("%Y-%m-%d")] #Book 3 days in advance
            print(days)

            for i in days:
                print("-------------")
                try: 
                    countbooked=driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div/form/p[3]")
                except:
                    print("Maximum Booked. Booked {} times".format(self.countbooked))
                    return 1
                self.countbooked=countbooked.text[9]

                selectday_element=scrollTo(driver, driver.find_element_by_id('btn_date_select'))        
                selectday_element.click()
                day_element_name="date_"+i
                print("Looking at times for", i)
                sleep(2)
                driver.find_element_by_id(day_element_name).click()

            # 6) Select time: [TO-DO] No times available -> Recommend tomorrows times, else: Let me select times. Recommend times between a certain preset range, but show all times too.
                booked = self.bookTime(driver)
                if booked != 0:
                    self.timesbooked[i]=booked
                    print("Booked for ", i)

        except Exception as e:
            print(e)
            print("Something went wrong")


if __name__ == '__main__':
    password=sys.argv[1]
    email=sys.argv[2]
    location=sys.argv[3]
    person=Account(password, email, location)


    # david=Account('dp05092001', 'peamap101@gmail.com', 'North York Centerpoint Mall')
    start_time="13:00"
    end_time="16:00"
    minrangetimegym=datetime.datetime.now().replace(hour=int(start_time[:start_time.find(":")],), minute=int(start_time[start_time.find(":")+1:]))
    maxrangetimegym=datetime.datetime.now().replace(hour=int(end_time[:end_time.find(":")]), minute=int(end_time[end_time.find(":")+1:]))
    print("Starting bot...")
    driver = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver'))
    person.book(driver, minrangetimegym, maxrangetimegym)
    print("-------------")
    print("Booked this section:", person.timesbooked)
    #driver.quit()