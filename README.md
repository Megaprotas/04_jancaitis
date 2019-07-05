[![Build Status](https://travis-ci.org/Megaprotas/04_jancaitis.svg?branch=master)](https://travis-ci.org/Megaprotas/04_jancaitis)

BugHunters
Project is dedicated to form a community of programmers or hobbyists who could paste the bug they stuggle and 
I could solve the case (statistics of posted/in process/fixed will be provided). Also, more complex features would be
for sale. To attract more traffic simple blog is created, where differet issues could be discussed.


UX
Website is split into three different parts. Free part of bug posting and stats, secons is e-commerce bit, third is a
blog, so each user can find exactly what they are looking for. Each bug or a feature has its basic and detailed view, 
to prevent taking most of a screen, especially on smaller devices.
Also users are allowed to comment or vote (once), add features to cart and pay.
To help user to get confirmation about each action (registration, purchase, login) the messages at top of the screen
shows up.
Bugs can have three statuses: posted, in pending, fixed. Each of them is resembled by different colors as well as sorted
based on their status. Also, only user who posted the bug is allowed to edit/delete it.
Newest bug shows up on a front page.

Features - only superuser can post/edit/delete them. To prevent fraud.

Blog - simple function, also - only superuser is allowed to post, and other users got option to comment it. Also
calculation of views is presented.

Forms - all forms share same design features, regardless if its registration or purchase. So the user can follow same 
design pattern.

Graphs (done using Charts.JS) are under bug, it updates according to number of bugs posted. Uses pie charts to show the 
ration of bug statuses and bar charts showing total number of bugs, as well as ones posted per day/week/month.

Also, website is fully responsive, so could be viewed on different devices.


TECHNOLOGIES USED
Django
JavaScript: Stripe, Charts.JS
Bootstrap
Postgres
CSS
HTML5


DEPLOYEMENT
Code was written using PyCharm, local GIT was used for a version control before uploading it to GitHub and Heroku. All
static files are on AWS.


TESTING
Registration - form being rendered correctly, and user can be created successfully.
Login - username and password of registered user has been entered and login was successful. Message flashed. 
Same  results with email and password.
After creation another new user I tried to edit/delete bugs/comments of other user, but buttons allowing to do so
wasn't showing.
Only superuser could create the blog post/feature.
Items after purchase are shown in a cart successfully.
Charts are showing correctly, tried to upload different posts with different statuses and it gives right information.

CREDITS
Thank You to my mentor for explaining how to do charts properly and for all of his help throughout this project.
Thanks to code institute for showing e-commerce and registration parts.

MEDIA
All pics are royalty free and been taken from pexels.com

FEATURES COULD BE IMPLEMENTED
- showing each item total price = item unit price * quantity
- Ajax the page for quicker load
- join features and bugs under one app
- footer :)