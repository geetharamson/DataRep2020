import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="my66Query",
  database="datarep"
)

cursor = db.cursor()
sql="CREATE TABLE pharmajobs (JobId INT AUTO_INCREMENT PRIMARY KEY, JobTitle VARCHAR(250), Company VARCHAR(250), County VARCHAR(250), NoOfVacancy INT)"
sql="CREATE TABLE employees (EmployeeId INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(250), Age INT,Salary INT)"

cursor.execute(sql)