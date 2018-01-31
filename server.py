from flask import Flask, request, Response, jsonify
from opportunity import OpportunityManager
from pymongo import MongoClient
from verify import ActionVerifier
from seed import seed
from bson import json_util
from collections import defaultdict
import time
import json
#import pprint

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
locations = db["locations"] # Streamer for locations
motionActivityUpdates = db["motionActivityUpdates"]
sensorMoments = db["sensorMoments"]
worldObjects = db["worldObjects"] # Objects with locations

# Fill server database with hardcoded moments/objects

@app.route('/')
def index():
    return 'hs4x homepage'

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
		timeStr = str(time.time())
		# Write to db
		locations.insert(data)
		save_string = latStr+','+lngStr+','+timeStr+'\n'
		# Return result of opportunity manager!
		best_moment = opportunityManager.get_moment(float(latStr),float(lngStr))
		json_moment = json.dumps(best_moment[0])
		return json_moment
	return "{}"

# Send best moment to ExperienceKit for insertion
@app.route('/moments')
def all_moments():
	moments = db.moments.find()
	# return jsonify({"result":"ok"})
	# print json_util.dumps(moments)

	return Response(
		# RETURN BEST MOMENT
		json_util.dumps(moments[0]), 
		mimetype='application/json'
	)

# Dump world objects
@app.route('/objects')
def all_object():
	objects = db.worldObjects.find()
	return Response(
		json_util.dumps(objects[0]), 
		mimetype='application/json'
	)

# Add new moment to DB
@app.route('/moment', methods = ['POST'])
def add_moment():
	try:
		data = request.get_json(silent=True)
		# Write to moments collection
		print data
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

#verifier not used, so it's commented out
# @app.route('/verify', methods = ['POST'])
# def verify_action():
# 	if request.method == 'POST':
# 		data = request.get_json()
# 		to_verify = data['to_verify']
# 		from_timestamp = data['from_timestamp']
# 		return str(actionVerifier.verify(to_verify, from_timestamp))
# 	return str(False)

# FROM YK, makes running app refresh
if __name__ == "__main__":
   #app.run(debug=True)
	app.run(host='0.0.0.0')
