## Data Representation Project GMIT 2020

#### Author : Geetha Karthikesan
#### Email: G00376320@gmit.ie

This repository contains the project for Data Representation 

### Building the project:
+ Thought to some about the Pharmaceutical jobs in Ireland, hence made use of https://www.getreskilled.com/pharmaceutical-jobs/ireland-factory-table/ to collect details 
 for my database and hence step by step process to do my project.
+ The first step was to develop the environment with Flask.
+ Then server.
+ Then build the CRUD.
+ Launch to a web page.

## Contents of this repository
This repository contains:
    
    server: app.py

    web page: pharmajobs.html

    DAO: zjobsDAO.py  [zjobsDAO.py contains jobsDAO class]

    DB config to edit on PA: dbconfigtemplate.py

    Virtual environment requirements: requirements.txt

    index: jobs2.html

    All old files in \oldservers
    
    Images : have snip shots of my work with snipping tool

    Link to app on pythonanywhere :http://geethakathikesan.eu.pythonanywhere.com/
    
    
### How to clone this repository

A repository on GitHub exists as a remote repository. You can clone this repository to create a local copy on your computer by following these instructions:

   1. On GitHub, navigate to the main page of the repository https://github.com/geetharamson/DataRep2020.git   
   2. Under the repository name, click Clone or download.
   3. Choose "Clone with HTTPS".
   4. Open a terminal on your machine. Change the current working directory to the location where you want the cloned directory to be made.
   5. Type git clone, and then paste the URL you copied in 2 above.
   
            > https://github.com/geetharamson/DataRep2020.git
   6.Press enter to clone the repository to your machine.

### Virtual Environment Requirements:
    
 In the cmder create virtual environment: ((WINDOWS machine))
      
    >install python -m venv venv

To run the virtual environment
           
    > venv\Scripts\activate.bat

To see the packages needed to run this project

    > pip freeze

To load the file of packages

    > pip freeze -r requirements.txt

 To install the requires packages:

    >pip install flask
    >pip install mysql-connector-python
    
 To exit
      
     > deactivate

### Testing the connection
You can test the connection by checking the http responses with the Curl, for example:

      > curl -i http://localhost:5000/

##### Add-ins:
 The Following was outputted: C:\Users\Owner\Desktop\project (venv) λ flask run

Serving Flask app "server1"
Environment: production WARNING: This is a development server.
Do not use it in a production deployment. Use a production WSGI server instead.
Debug mode: off
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


### MySQL database & table
     Database = datarep
     Table = pharmajobs

MySQL command to create is 

      create table pharmajobs(
    -> JobId int PRIMARY KEY,
    -> JobTitle varchar(250),
    -> Company varchar(250),
    -> County varchar(250),
    -> NoOfVacancy int(11)
    -> );

|  Field        |  Type        | Null    |  Key   | Default | Extra  |
| ------------- | ----------   | ------  | ------ |-------- | -------|
| JobId         |   int        |   NO    |   PRI  |  NULL   |        |
| JobTitle      | varchar(250) |   YES   |        |  NULL   |        |
| Company       | varchar(250) |   YES   |        |  NULL   |        |
| County        | varchar(250) |   YES   |        |  NULL   |        |
| NoOfVacancy   | int          |   YES   |        |  NULL   |        |



## REFERENCES

Python Virtual Environment - [https://docs.python-guide.org/dev/virtualenvs/]
Flask User Guide - [https://flask.palletsprojects.com/en/1.1.x/#user-s-guide]
PythonAnywhere -[https://blog.pythonanywhere.com/121/]













