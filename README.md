# WorkingTime
Webapplication project for counting working time and more.

Website is deployed on heroku: 
[workingsite-app](https://workingsite-app.herokuapp.com)

###### Application is using mostly Python with Django framework, Vuejs for frontend which is connecting with Django Rest Framework.

Application was written as a main purpose for counting working time in my hotel. 
Since there is not any system for it, just 'a pen and paper' system, i decided to make one.

Everyone who is working can sign up and start using it, as soon as supervisor confirm it as a employee of hotel.


### How does 'working time' work?

Very simple. Everytime when you start working you just press the button **'START'**. In that moment new data is created in DB with start_working time as now() and is atached to your user_profile through ForeignKey. When you finish you work, you press the **'STOP'** button and end_working time data is getting now(), except if working time is over 10h, then it's added 
```
workingtime.start_working + timedelta(hours=10)
```
to end_working and employee is getting information that he worked more than 10h which is not allowed(supervisors can change time to how long they want, just not into the past).
Only time when employee can save over 10h working time, is when he worked for example 9h 59min and checked **BREAK** box(if person didn't have a break) which is adding 30min to your end time.
Then end_working time is beeing subtracted from start_working and delta_seconds converted to minutes. To DB is saved a string of how long you have been working and integer of minutes which are later used to show total time of work.

- You can't start your work on the same day more than once, except if you delete time from that same day.
- Any new time has to be confirmed or corrected by any supervisor

### FrontPage

On the **frontpage** is printed a list of all working dates with a working time. 
Employee can see if time was confirmed or corrected by supervisor. Employee can see logs of changes to the time:
- Who made the changes
- When
- What kind of change
- Note from person who corrected time
Can also delete time.
### Tips

Tips application, which is made for a management team to calculate and split tips between all employees in the same department as supervisor who is using app.

First to every employee are assign points. Then you type total of tips to share. 
All points from every employee are getting added together and tips are divided by that number.
Then a quotient is multiplied by points of every single employee.

### UserProfile

Created user profile, where you can assign your name, last_name, age and email address(unique) to your profile.
In the moment of creating new account you are redirected to profile page to assign required fields(name, last_name). Same when you delete your name or last_name.
Without it you can't go anywhere, you will be always redirected here. It's needed for a Tips app which is using names and last_names of the users.
- User can now change a password in Userprofile.
- Supervisor/Manager can see all working times on any userprofile page and change them with small note.

### Search bar

Everyone can look for employees but just supervisor or higher rank can go to the profile. Employees will be redirected to frontpage

### Logs

Every change of time is saved in logs. 
- By Who
- When
- Changed time
- Note

Supervisor or higher, can download logs of time of any employee. Its a txt file.

(Only supervisor or higher)
### Daily and Weekly(KW)
- Daily list of working employees with their times
- Weekly list of employees with their times, need to choose a week of the year(number).
