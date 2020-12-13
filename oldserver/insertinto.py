import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="datarep"
)

cursor = db.cursor()
sql="insert into pharmajobs (JobId,JobTitle,Company,County,NoOfVacancy) values (%s,%s,%s,%s,%s)"
values = (1,"APIManufacturer","UCB","Clare",120)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)