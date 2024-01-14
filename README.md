# Workout-Log
Workout Log Django Application (Python, HTML, CSS, PostgreSQL, Plotly)
Django application that allows users to perfrom CRUD operations to input, view, update, and delete their workouts. 
  - Used HTML and CSS for structuring and style of the web page.
  - Used Python for backend logic and functionality making use of the Django Framework.
  - Used PostgreSQL hosted by AWS as the database management system.
  - Used Plotly library to create graph to track user progress

Features include:
  - Shows users all workouts by date
  - Shows users maximum weight lifted per rep (1-10) in neatly organized and dynamically updating table
  - Shows users graph of Estimated One rep max vs Date to show progress of the user

I personally inputed all of my workouts since August 2023. I will show all the functionalities of the web application using my Bench Press workouts


![image](https://github.com/IvanTejeda/Workout-Log/assets/29577371/33c408c0-5db8-4b0b-930a-e436bc385ee3)



CREATE:





![image](https://github.com/IvanTejeda/Workout-Log/assets/29577371/84e93096-fe8a-46c2-81ed-10f84cf76da3)




Allows users to add workout weight, sets, and reps per date. Takes data in as a form and sends POST request to to the correct class in views.py which saves the data into the appropriate database.  
from views.py:





![image](https://github.com/IvanTejeda/Workout-Log/assets/29577371/b3da713d-620a-48e9-8515-fea7381354a5)




READ:
Allows users to see their previous workouts by date, with each date corresponding to a table. Also has a button for each data object to allow users to edit or delete data



![image](https://github.com/IvanTejeda/Workout-Log/assets/29577371/99cc8145-c5ab-41c9-99dd-90f1f9cf0a1f)S

Algorithm to sort bench data by date which allows HTML file to create a table for each date:



![image](https://github.com/IvanTejeda/Workout-Log/assets/29577371/ee422a02-9dba-4741-869b-cdfdea65a23d)





![image](https://github.com/IvanTejeda/Workout-Log/assets/29577371/7a70df4d-fd29-4fd2-9482-06c00de4b1c6)

Also shows user their max weight per rep. Similar algorithm to query database grouping by reps, then picking the max weight and corresponding date. 



![image](https://github.com/IvanTejeda/Workout-Log/assets/29577371/69ca1339-84e7-4030-bd6c-d9fabb57009a)

A tough problem with this feature was, for example, if the user was able to perform a weight for 6 reps, then technically they performed that weight for reps 1-5 also. If the user never submitted a workout for reps 1-5, the table still needed to show that this was their 1-5 rep max. The solution was to iterate through reps 1-10 backwards (10-1) then populate the table downwards so that if a weight was performed for 6 reps it would also know it can be performed for 1-5 reps. At each repition, it would need to check if a max weight was already there, then compare to see which was higher and then populate with the appropriate weight.  



![image](https://github.com/IvanTejeda/Workout-Log/assets/29577371/d6004fec-687c-46d6-830a-f9f4fa6d1dff)




The last feature and my personal favorite is the graph to of the users estimated one rep max vs date. This shows progress and can let the user know when they should try to perform a one rep max. The formula to estimate a user's one rep max was Matt Brzycki's: Weight/(1.0278 - (0.0278 x reps))

plotly library was used to create the graph 




![image](https://github.com/IvanTejeda/Workout-Log/assets/29577371/f8301686-8565-48b5-8c77-51d825c41807)



(as you can see, I stopped lifting intensly during November as a decline is shown. I blame finals, being sick, and SHPE convention).

Since this is a derived attribute, it was a function inside the model. Technically a property. 



![image](https://github.com/IvanTejeda/Workout-Log/assets/29577371/ddda1b31-83f0-4a5b-a92d-1e6f70ea0316




The tough part about this feature was that a user would have several estimates of a one rep max in the same day. For example, if a user inputted that they lifted 225 for 1 rep on jan 1st, and then they also lifted 235 for 1 rep on jan 1st, then for jan 1st the user has 2 estimates of 225 and 235. I had to write an algorithm that would only take the HIGHEST estimate for each date. In our example, it would only read 235 for jan 1st, not 225. 
This algorithm stores all bench objects in the variable "entry". It also creates two lists one for the x variable (dates) named "h" and one for the y variable (estimates) named "v". Then it iterates through each entry object. If the certain date was already in the date list, then it would compare estimates, and keep the highest one. 




![image](https://github.com/IvanTejeda/Workout-Log/assets/29577371/7d0534b7-4e87-4a01-b8e7-600efcabe927)





UPDATE:



![image](https://github.com/IvanTejeda/Workout-Log/assets/29577371/6d257784-af65-41f8-9141-f2f7fad0df6c)

Exact same process as creating data. Makes sure that it updates the correct object in the database by filtering by id. 
from urls.py:



![image](https://github.com/IvanTejeda/Workout-Log/assets/29577371/15655525-71e8-4251-b638-49d4fbcd76f6)



from views.py: notice it takes id as a parameter to ensure it is updating the correct object 



![image](https://github.com/IvanTejeda/Workout-Log/assets/29577371/f2efee16-d7b5-4164-a59d-d9fae6a01b50)

DELETE:
When the delete button is pressed the user is directed to this page




![image](https://github.com/IvanTejeda/Workout-Log/assets/29577371/7afcb209-7b0f-4c72-adae-a073100eb351)




Same process as creating and updating, send POST request and the views.py handles it on the correct data object. 









