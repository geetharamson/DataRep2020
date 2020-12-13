##Author : GEETHA KARTHIKESAN
##G00376320@gmit.ie
##DATA REPRESENTATION PROJECT

from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='', static_folder='staticpages')

job=[
    {"JobId": 1, "JobTitle": "API manufacturer ", "Company": "UCB", "County": "Clare", "NoOfVacancy":100},
    {"JobId": 2, "JobTitle": "Animal Health ", "Company": " Bimeda Ireland", "County":"Dublin", "NoOfVacancy": 150},
    {"JobId": 3, "JobTitle": "Pharma manufacturer", "Company": "Temmler", "County": "Kerry", "NoOfVacancy": 60},
	{"JobId": 4, "JobTitle": "Infants Products", "Company": "Wyeth", "County": "Limerick", "NoOfVacancy": 600},
	{"JobId": 5, "JobTitle": "Food Supplements", "Company": "Bioshell", "County": "Mayo", "NoOfVacancy": 40},
]
jobId=6

@app.route('/')
def index():
    return "hello"
	
#get all
@app.route('/job')
def getAll():
    return jsonify(job)
	

# find By id
@app.route('/job/<int:JobId>')
def findById(JobId):
    foundJob = list(filter (lambda t : t["JobId"]== JobId, job))
    if len(foundJob) == 0:
        return jsonify({}) , 204
    return jsonify(foundJob[0])	
	

# create
#  curl -X POST -d "{\"JobTitle\":\"test\", \"Company\":\"some company\",\"County\":\"Meath\",\"NoOfVacancy\":123}" http://127.0.0.1:5000/job
@app.route('/job', methods=['POST'])
def create():
    global nextId
    if not request.json:
        abort(400)
    
    job = {
        "JobId": nextId,
        "JobTitle": request.json["JobTitle"],
        "Company": request.json["Company"],
        "County": request.json["County"],
		"NoOfVacancy": request.json["NoOfVacancy"]
    }
    job.append(job)
    nextId += 1
    return jsonify(job)
    return "served by Create "	
	
	
#update
# curl -X PUT -d "{\"JobTitle\":\"new Title\", \"Company\":\"something\",\"County\":\"unknown\",\"NoOfVacancy\":130}" -H "content-type:application/json" http://127.0.0.1:5000/job/8
@app.route('/job/<int:JobId>', methods=['PUT'])

def update(JobId):
    foundJob = list(filter(lambda t: t["JobId"] == JobId, job))
    if len(foundJob) == 0:
        return jsonify({}), 404
    currentJob = foundJob[0]
    if 'JobTitle' in request.json:
        currentJob['JobTitle'] = request.json['JobTitle']
    if 'Company' in request.json:
        currentJob['Company'] = request.json['Company']
    if 'County' in request.json:
        currentJob['County'] = request.json['County']
    if 'NoOfVacancy' in request.json:
        currentJob['NoOfVacancy'] = request.json['NoOfVacancy']

    return jsonify(currentJob)

#delete
# curl -X DELETE http://127.0.0.1:5000/job/1
@app.route('/job/<int:JobId>', methods=['DELETE'])
def delete(JobId):
    foundJob = list(filter(lambda t: t["JobId"] == JobId, job))
    if len(foundJob) == 0:
        return jsonify({}), 404
    job.remove(foundJob[0])

    return jsonify({"done":True})

if __name__ == "__main__":
    app.run(debug=True)
	
