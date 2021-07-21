Objective:

Stack Overflows awards two badges- 

1. A GOLDEN 'Fanatic' badge upon Visiting the site each day for 100 consecutive days. (Days are counted in UTC.)
2. A SILVER 'Enthusiast' badge upon Visiting the site each day for 30 consecutive days. (Days are counted in UTC.)

What makes these badges hard to get is that you have to visit the site everyday without any gaps. What if you forget to check the website for a day?. The counter for the badge resets :(.

In this repo. I have created a simple 2 line python file that can open the website and also a .bat file to run the python code.
Windows Task scheduler is used to execute the .bat file daily when the user logs in.


### Setup

1. Download the repo.
2. Edit the two files as instrcted in the files.
3. Open Start.
4. Search for Task Scheduler and click the top result to open the app.
5. Right-click the "Task Scheduler Library" branch and select the New Folder option.
6. Confirm a name for the folder — for example, Yourname.
7. Click the OK button.
8. Expand the "Task Scheduler Library" branch.
9. Right-click the MyScripts folder.
10. Select the Create Basic Task option.
11. In the "Name" field, confirm a name for the task — for example, SystemInfoBatch.
12. (Optional) In the "Description" field, write a description for the task.
13. Click the Next button.
14. Select the 'Whwn I log on' option under trigger.
15. Choose Start a program under Action
16. Click browse and choose the .bat file that you have edited
17. Click Finish



A different idea with implementation can be found here- https://github.com/modocache/stackoverflow-fanatic
