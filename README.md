# WorkingTime
Webapplication project for counting working time and more.

###### Application is using mostly Python with Django framework, and a bit of Vuejs.

Application was written as a main purpose for counting working time in my hotel. 
Since there is not any system for it, just 'a pen and paper' system, i decided to make one.

Everyone who is working can sign up and start using it.

### How does 'working time' work?

Very simple. Everytime when you start working you just press the button **'Work'**. In that moment new data is created in DB with start_working time as now() and is
atached to your user_profile through ForeignKey. When you finish you work, you press the button again and end_working time data is getting now().
Then end_working time is beeing subtracted from start_working and delta_seconds converted to minutes. To DB is saved a string of how long you have been working.

- You can't start your work on the same day more than once.
- You can't skip to start_working/end_working template, you will get a **"Nope"** message.


### FrontPage
On the **frontpage** is printed a list of all working dates with a working time. 


### Tips
I made also a Tips application, which is made for a management team to calculate and split tips between all employees.

First to every employee are assign points. Then you type total of tips to share. 
All points from every employee are getting added together and tips are divided by that number.
Then a quotient is multiplied by points of every single employee.

### Coming Soon:
- List of departments in the hotel 
- UI for userprofile to change/add options like:
  - Gender
  - Age
  - Department
  - Email
