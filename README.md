# Update-Student-Org-Roster
Automatically bulk add members to an OSU student org.

This python program uses Selenium in python to automatically add members to an Ohio State University student organization.   

First, create a .txt file of your new members' OSU name.# with one name dot number per line and add the file to your project.
Remember to record the name of your file in the 'members_file' variable.

Manually login to Student Organization Management and go to your club's 'update roster' page.  Copy the URL and store it in 'roster_page' variable.

You will also need to download a chromedriver if you don't already have one on your computer.  
Download it here: http://chromedriver.chromium.org/downloads
Store the location of your chromedriver in the 'path' variable.

Finally, add your OSU username and password to the 'username' and 'password' variables so the program can login as you.

Even though there is an error exception in the program, sometimes the browser will stop processing and stay on a webpage that says: "Individual not found."
If that happens, just click the 'Cancel' button on the same and it should start running again, continuing where it left off.


This program was originally designed for the 'CEO @ Ohio State' to automatically add over 700 new members to the club at once. 
