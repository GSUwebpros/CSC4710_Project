
# SOME THINGS TO BE AWARE OF
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

** Make sure you have downloaded MySQL Workbench or XAMMP on your system and make sure you have downloaded Python as well. 
** Preferably, MySQL workbench because I'm not too familiar with XAMPP but it is fine if you know how to use it.

** Type these commands in the cmd in the directory with all the project files:

    pip install flask
    pip install flask_mysqldb
    pip install mysql-connector-python

** In the db_connector.py file, change the value of the password parameter of the "conn" object to whatever password you gave whilst downloading MySQL on your pc.
** if you did not give a password just leave it as an empty string

** The HTML files are templates that we can use to design the website. I just used some Bootstrap classes to have an interface to work with whilst doing the backend but we can delete and add our own CSS but the overall structure in terms of the number of HTML files should be similar to this.


