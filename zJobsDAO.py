#Geetha Karthikesan
# G00376320@gmit.ie

#pip install mysql-connector-python

import mysql.connector
import dbconfig as cfg
class JobsDAO:
    db = ""

    #def __init__(self):
    def connectToDB(self):
        self.db = mysql.connector.connect(
        host =       cfg.mysql["host"],
        user =       cfg.mysql["root"],
        password =   cfg.mysql["my66Query"],
        database =   cfg.mysql["database"]
        )
        return db 
    #print("Connection made")    

    def __init__(self):
        self.connectToDB()
		
	# Check for cnxn, if none make one.
    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()	

    def create(self, values):
        cursor = self.db.cursor()
        sql = "insert into pharmajobs (JobId, JobTitle, Company, County, NoOfVacancy) values (%s,%s,%s,%s,%s)"
        cursor.execute(sql, values)
        self.db.commit()
        lastRowID = cursor.lastRowID
        cursor.close()
        return lastRowID
        print("create done")


    def getAll(self):
        cursor = self.getCursor()
        sql = "select * from job"
        cursor.execute(sql)
        results = cursor.fetchall()

        # Formatting what comes back from DB
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        cursor.close()
        return returnArray
        print("get all done")

    def findByID(self, id):
        cursor = self.getCursor()
        sql = "select * from job where JobId = %s"
        values = (JobId, )

        cursor.execute(sql, values)
        result = cursor.fetchone()
        # Format what comes back from db
        job = self.convertToDictionary(result)

        cursor.close()  
        return job

    def update(self, values):
        cursor = self.getCursor()
        sql = "update job set JobTitle = %s, Company = %s, County = %s, NoOfVacancy = %s where JobId = %s"
        
        cursor.execute(sql, values)
        self.db.commit()
        print("update done")
        cursor.close()

    def delete(self, id):
        cursor = self.getCursor()
        sql = "delete from job where JobId = %s"
        values = (JobId, )

        cursor.execute(sql, values)
        self.db.commit()
        print("delete done for JobId", JobId)
        cursor.close()

    # Converting tuple returned from DB into dict
    def convertToDictionary(self, result):
        
        # List of attributes - match html with colnames
        colnames = ['JobId', 'JobTitle', 'Company', 'County', 'NoOfVacancy']
        
        # Empty list
        item = {}

        # Can't enumerate through an empty result, so check.
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value

        return item

jobsDAO = JobsDAO()