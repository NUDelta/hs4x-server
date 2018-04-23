from flask import Flask, request, Response, jsonify
from opportunity import OpportunityManager
from pymongo import MongoClient
from verify import ActionVerifier
from seed import seed
from seed2 import seed2
from seed3 import seed3
from bson import ObjectId
from bson import json_util
from collections import defaultdict
import time
import json
import random

app = Flask(__name__)
opportunityManager = OpportunityManager()

uri= "mongodb://localhost:27017"
#uri= "mongodb://ob:kim@ds153577.mlab.com:53577/hs4x"
dbName = "hs4x"
client = MongoClient(uri)
db = client[dbName]

# Collections based on Experience Kit
experiences = db["experiences"] # Story of full run
moments = db["moments"] # Individual interactions
#locations = db["locations"] # Streamer for locations
motionActivityUpdates = db["motionActivityUpdates"]
sensorMoments = db["sensorMoments"]
worldObjects = db["worldObjects"] # Objects with locations
runs = db["runs"] # Run organizes the entire experience for each individual run
users = set() # Keep track of user ids. Hacky fix.

#seed(moments, worldObjects)
#seed2(moments, worldObjects)
#seed3(moments, worldObjects)

# Fill server database with hardcoded moments/objectt

@app.route('/')
def index():
	return 'hs4x'

def generate_userId():
	randId = random.randint(1,1001)
	while(randId in users):
		randId = random.randint(1,1001)
	return randId

# Initialize the run for a user
# Front end sends in a start time
# Return a run id and unique user id
@app.route('/initialize_run', methods = ['POST'])
def initialize_run():
	data = request.get_json() 
	user_id = generate_userId()
	users.add(user_id)
	start_time = str(data['start_time'])
	run_oid = runs.insert({
		"user_id": user_id,
		"start_time": start_time,
		"end_time": "",
		"locations": [],
		"speeds": [],
		"moments_played": []
	})
	returnDict = {}
	returnDict["run_id"] = str(run_oid)
	returnDict["user_id"] = str(user_id)
	return Response(
			# The id of the run created for future use on Front end
			json_util.dumps(returnDict),
			mimetype='application/json'
	)

# Recieves the posted location from the ios app, 
#	and then immediately checks whether there are 
#	any moments in range to send. 
#	If so, it returns best moment

@app.route('/location', methods = ['POST'])
def save_location():
	if request.method == 'POST':
  		data = request.get_json()
		latStr = str(data['latitude'])
		lngStr = str(data['longitude'])
		speed = str(data['speed'])
		run_id = str(data['run_id'])
		timeStr = str(time.time())

		runs.update(  
					{"_id" : ObjectId(run_id)}, 
					{"$push":{"speeds": speed}})

		runs.update(
					{"_id" : ObjectId(run_id)}, 
					{"$push":{"locations": {"latitude": latStr, "longitude": lngStr}}})
		
		save_string = latStr+','+lngStr+','+timeStr+'\n'
		# Return result of opportunity manager!
		best_moment = opportunityManager.get_moment(run_id, float(latStr),float(lngStr))
		if best_moment != None:
			return Response(
				json_util.dumps(best_moment[0]),
				mimetype='application/json'
			)
		else:
			return jsonify({})
	return jsonify({"result":0})

@app.route('/verify', methods = ['POST'])
def verify_action():
	# To verify an action, we need:
	# the run_id, the current speed, the moment it is verifying
	data = request.get_json()
	run_id = str(data['run_id'])
	speed = str(data['speed'])	
	moment = str(data['moment']) # How do I identify a moment? By prompt most likely...

	# Action verifier will check for a speed change and update the database accordingly
	respond2action = opportunityManager.action_verifier(run_id, int(speed), moment)
	verification_response = {"action_verified": respond2action}
	
	return Response(
		json_util.dumps(verification_response), 
		mimetype='application/json'
	)

# Dump world objects
@app.route('/objects')
def all_object():
	objects = db.worldObjects.find()
	return Response(
		json_util.dumps(objects), 
		mimetype='application/json'
	)

# Dump world objects
@app.route('/moments')
def all_moments():
	moments = db.moments.find()
	return Response(
		json_util.dumps(moments), 
		mimetype='application/json'
	)

# Add new moment to DB
@app.route('/moment', methods = ['POST'])
def add_moment():
	try:
		data = request.get_json(silent=True)
		# Write to moments collection
		moments.insert(data)
		return jsonify(status='OK',message='inserted successfully')
	except Exception, e:
		return str(e)

# Add new object to DB
@app.route('/object', methods = ['POST'])
def add_object():
	try:
		data = request.get_json
		# Write to moments collection
		worldObjects.insert(data)
		return jsonify(status='OK',message='inserted successfully')
	except Exception, e:
		return str(e)

# Send best moment to ExperienceKit for insertion
@app.route('/intro')
def intro():
	moments = list()
	for moment in db.moments.find({"name": "Intro"}):
		moments.append(moment)
	return Response(
		# Right now, returning the first intro moment it finds, later should be randomized or calcualted
		json_util.dumps(moments[0]), 
		mimetype='application/json'
	)

@app.route('/end')
def end():
	moments = list()
	for moment in db.moments.find({"name": "End"}):
		moments.append(moment)
	return Response(
		# Right now, returning the first intro moment it finds, later should be randomized or calcualted
		json_util.dumps(moments[0]), 
		mimetype='application/json'
	)

# FROM YK, makes running app refresh
if __name__ == "__main__":
	#app.run(debug=True)
	app.run(host='0.0.0.0')
