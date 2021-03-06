![Gym-Booking-Discord-Bot](https://socialify.git.ci/davepetrov/Gym-Booking-Discord-Bot/image?description=1&font=Inter&language=1&owner=1&pattern=Diagonal%20Stripes&theme=Light)

A Discord bot that helps you book the gym times during COVID-19. Nowadays, gyms are completely booked, but now its time to workout after months of endless quarantine. Let the bot do the annoying part...the booking! Through discord, you can specify a time range that you want to work out, the specific gym(s) you are signed up for, and the bot will book the time slot for you before anyone else can take your spot and will remind you when your next work out will be. Now you can go to the gym without worrying about missing an available time slot that fits your schedule.

# How to use the bot 
Join https://discord.gg/zDpsGyj and use the following commands!
###### *Note*: Currently Unavailable for use, Ping me if you'd like me to reactivate :)

# Running the bot on your own
```sh 
node index.js
```
If you want the bot to stay online, keep the program running in the background.

## Commands
### !book
#### Parameters:
  - Password
  - Email address
  - Exact fit4less location
  - Minimum time range to book
  - Maximum time range to book
#### Description/example:
In short, this command does all the automated booking, reserving all the times within the specific time block you give it. Suppose the user is free and wants to book a time between 11:00 and 17:00 for the "Centerpoint-Mall" location. The user calls the command from the server and gets a private message revealing the private login information with all the booked times.
  
  <img src="/images/book-showcase.png" width="700">
  
### !reserved
#### Parameters:
- Password 
- Email
#### Description:
Lists all of the current scheudeled times

<img src="/images/reserved-showcase.png" width="700">
  
  
### !locations
The bot replies with a list of available locations, the user will copy whichever location into the [location] parameters when booking with !book
   
### !help
Lists all the commands with short descriptions

## TODO:
- Add a login command that saves the user's information
- Book with friends
