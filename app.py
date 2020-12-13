##Author: GEETHA KARTHIKESAN
## DATA REPRESENTATION PROJECT 2020



# flask related
from flask import Flask, jsonify, request, abort


# For interaction with MySQL Table = job in Database = datarep
from zJobsDAO import jobsDAO

app = Flask(__name__, static_url_path='', static_folder='.')

job=[
    {"JobId": 1, "JobTitle": "API manufacturer ", "Company": "UCB", "County": "Clare", "NoOfVacancy":100},
    {"JobId": 2, "JobTitle": "Animal Health ", "Company": " Bimeda Ireland", "County":"Dublin", "NoOfVacancy": 150},
    {"JobId": 3, "JobTitle": "Pharma manufacturer", "Company": "Temmler", "County": "Kerry", "NoOfVacancy": 60},
	{"JobId": 4, "JobTitle": "Infants Products", "Company": "Wyeth", "County": "Limerick", "NoOfVacancy": 600},
	{"JobId": 5, "JobTitle": "Food Supplements", "Company": "Bioshell", "County": "Mayo", "NoOfVacancy": 40},
]
jobId=6

# Action = Get all job from DB
# curl "http://127.0.0.1:5000/job"

@app.route('/job')
def getAll():
    #return "in getAll"

    # Connect to job table in datarep DB!
    results = jobsDAO.getAll()
    return jsonify(results)
    #return results


# Action = Find job in DB by ID
# curl "http://127.0.0.1:5000/job/1"

@app.route('/job/<int:JobId>')
def findByID(JobId):
    #return "in find by ID for id "+ str(id)

    # Return job from DB by requested id
    foundJob = jobsDAO.findByID(id)

    # Check if id exists
    if not foundJob:
        return "That id does not exist in the database table"
        abort(404)
    
    return jsonify(foundJob)
	
	
# create()
# Action = Create a new job in the DB
# curl -i -H "Content-Type:application/json" -X POST -d "{\"JobTitle\": \"Newjob\", \"Company\":\"Poker\", \"County": \"Kildare\",\"NoOfVacancy\": 50 }" "http://127.0.0.1:5000/job"

@app.route('/job', methods=['POST'])
def create():
    #return "in create"

    if not request.json:
        abort(400)
   
    job = {
        "JobTitle": request.json['JobTitle'],
        "Company": request.json['Company'],
        "County": request.json['County'],
        "NoOfVacancy": request.json['NoOfVacancy']
    }

    # Make the tuple for DB
    values = (job['JobTitle'], job['Company'], job['County'], job['NoOfVacancy'])
    newJobId = jobsDAO.create(values)
    job['JobId'] = newJobId

    return jsonify(job)
	
	
    # update(JobId)
#
# Action = Update job in DB by ID
# curl -i -H "Content-Type:application/json" -X PUT -d "{\"NoOfVacancy\":44}" "http://127.0.0.1:5000/job/3"

@app.route('/job/<int:JobId>', methods=['PUT'])
def update(JobId):
    #return "in update by ID for JobId "+ str(JobId)

    # Find the job in DB table
    foundJob = jobsDAO.findByJobId(JobId)

    if not foundJob:
        return "That JobId does not exist in the database table"
        abort(404)

    if not request.json:
        abort(400)

    # Get what was passed up
    reqJson = request.json

    # Info to update    
    if 'JobTitle' in reqJson:
        foundJob['JobTitle'] = reqJson['JobTitle']
    if 'Company' in reqJson: 
        foundJob['Company'] = reqJson['Company']
    if 'County' in reqJson:
        foundJob['County'] = reqJson['County']

    # Make the tuple for DB
    values = (foundJob['JobTitle'], foundJob['Company'], foundJob['County'], foundJobId['JobId'],foundJob['NoOfVacancy'])
    # Do the update on DB
    jobDAO.update(values)
    return jsonify(foundJob)

##################################################################

# Action = Delete job in DB by ID
# curl -X DELETE "http://127.0.0.1:5000/job/3"

@app.route('/job/<int:JobId>', methods=['DELETE'])
def delete(id):
    #return "in delete by ID for id "+ str(id)

    # Check if id exists in job table in DB
    foundJob = jobDAO.findByJobId(JobId)
    if not foundJob:
        return "That id does not exist in the database table"
        abort(404)

    # Remove job from DB by id
    jobsDAO.delete(id)
    return jsonify({"done":True})

	
	
if __name__ == '__main__' :
    app.run(debug= True)	