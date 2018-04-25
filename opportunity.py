import json
import time
import sys
from bson import json_util
from bson import ObjectId
from pymongo import MongoClient
from math import sin, cos, sqrt, atan2, radians


class OpportunityManager():
	def __init__(self):
		#uri= "mongodb://ob:kim@ds153577.mlab.com:53577/hs4x"
		uri= "mongodb://localhost:27017"
		dbName = "hs4x"
		client = MongoClient(uri)
		self.db = client[dbName]
		self.moments = list(self.db.moments.find())
		self.objects = list(self.db.worldObjects.find())

	#	Find all moments in range
	#	Make sure it has not already been sent
	# 	Return to frontend
	def get_moment(self, run_id, lat,lng):
		moments_in_range = self.get_moments_in_range(run_id, lat,lng)
		if len(moments_in_range) > 0:
			valid_moments = [ moment[0] for moment in moments_in_range ] # if moment["prompt"] not in self.sent 
			distances = [ dist[1] for dist in moments_in_range ] # if moment["prompt"] not in self.sent 

			best_moment, dist_to = self.get_best_moment(valid_moments)				

			run = self.db.runs.find_one({"_id" : ObjectId(run_id)})
			prompt = best_moment["prompt"]
			# Best moment can return empty, don't send if so
			if len(best_moment.keys()) == 0:
				return None
			# Check that this moment has not been sent already
			elif prompt in run["moments_played"]:
				print("This moment has been sent already!")
				return None
			# Send this moment to front end. Add to runs "played moment"
			else:
				print("Send this moment to front end. Add to run's played moments, update last distance run")
				best_moment = [json.loads(json.dumps(best_moment, default=json_util.default))]
				self.db.runs.update(
					{"_id" : ObjectId(run_id)}, 
					{"$addToSet":{"moments_played": prompt}})
				# Keep track of how far we just made the runner go out of their way
				if dist_to != None:
					self.db.runs.update(
						{"_id" : ObjectId(run_id)}, 
						{"$set":{"last_distance": distances[dist_to]}})
				return best_moment
		return None

	# Returns all moments within range of lat, lng
	def get_moments_in_range(self, run_id, lat,lng):
		moments_in_range = []
		available_expands = []
		expands = self.db.moments.find({"name": "Expand"})
		# Only moments flagged as "available" in the database
		for expand in expands:
			if(expand["available"]):
				available_expands.append(expand)
		for moment in available_expands:
			objectId = moment["id"]
			objectRadius = moment["radius"]
			obj = list(self.db.worldObjects.find({"name":objectId}))
			# Toggle object radius depending on how far runner JUST ran
			last_distance = list(self.db.runs.find({"_id": ObjectId(run_id)}))[0]["last_distance"]
			if last_distance > 50:
				objectRadius = .5*objectRadius

			if len(obj) > 0:
				obj = obj[0]
				objectLat = float(obj["lat"])
				objectLng = float(obj["lng"])
				dist = self.estimate_distance(lat,lng,objectLat,objectLng)
				if dist < objectRadius:
					moments_in_range.append([moment, dist])
				else:
					pass
		return moments_in_range
			

	# Returns moment from given array of moments least % covered attributes
	def get_best_moment(self, moments):
		fewest_attr_left = sys.maxint
		best_moment = {}
		distance_index = None
		for index, moment in enumerate(moments):
			momentId = moment["id"]
			target_object = self.db.worldObjects.find({"name": momentId})
			target_object = list(target_object)[0]
			attributes = target_object["attributes"]
			countTrue = sum(1 for x in attributes.values() if x[0])

			# Make the attributes left a percentage of the attributes of a worldObject
			attributes_left = (len(attributes) - countTrue)/len(attributes)	

			if attributes_left == fewest_attr_left and momentId == best_moment["id"] and (moment["radius"] < best_moment["radius"]):
				best_moment = moment
				distance_index = index
			elif attributes_left < fewest_attr_left:
				fewest_attr_left = attributes_left
				best_moment = moment
				distance_index = index

		return best_moment, distance_index

	# Stackoverflow function to compute distance. accurate to a couple ft
	def estimate_distance(self,lat1,lng1,lat2,lng2):
		# Approximate radius of earth in km
		R = 6373.0
		lat1 = radians(lat1)
		lon1 = radians(lng1)
		lat2 = radians(lat2)
		lon2 = radians(lng2)
		dlon = lon2 - lon1
		dlat = lat2 - lat1
		a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
		c = 2 * atan2(sqrt(a), sqrt(1 - a))
		distance = R * c * 3280.84
		return distance


	# SIMPLE action verifier -- just assess change in speed
	def action_verifier(self, run_id, speed, moment):
		data_set_size = 10
		speeds = list(self.db.runs.find({"_id": ObjectId(run_id)}))[0]["speeds"]
		speeds = map(int, speeds)

		if (len(speeds) > data_set_size):
			previous = speeds[-1*data_set_size:]
			avg = sum(previous)/data_set_size
		else:			
			avg = sum(speeds)/len(speeds)
		
		# Verified = true means this person sprinted 
		verified = speed > avg

		# Front end needs to look for this string. If empty, not verified
		if verified:
			self.update_database(verified, moment)
			return "Good sprinting. Thanks runner 5."
		return ""

	# Based on action verification, update the database accordingly
	def update_database(self, verified, moment_prompt):
		moment = list(self.db.moments.find({"prompt": moment_prompt}))[0]
		momentId = moment["id"]
		worldObj = list(self.db.worldObjects.find({"name": momentId}))[0]

		specific_attribute = moment["attribute"]
		
		# Access the dictionary within the collection by "attributes.{specific_attribute}"
		attribute2update = "attributes." + specific_attribute 
		
		# Status and responses = [None, 0] or something like that
		# Gotta be a better way to do this ... but having trouble accessing the list itself
		status_and_responses = worldObj["attributes"][specific_attribute]
		status_and_responses[1] = status_and_responses[1] + 1
		
		# Increment number of responses to this attribute
		self.db.worldObjects.update_one(  
					{"name" : worldObj["name"]}, 
					{'$set':{
						attribute2update: status_and_responses
					}
		})

		# For now, dealing with "yes" verifications only...
		# Set to true if responses more than 2
		if status_and_responses[1] > 2:
			status_and_responses[0] = True
			self.db.worldObjects.update_one(  
						{"name" : worldObj["name"]}, 
						{'$set':{
							attribute2update: status_and_responses
							}
			})

			# Unlock the next moment, if there is one
			if moment["unlock"] != None:
				next_moment = list(self.db.moments.find({"attribute": moment["unlock"]}))[0]
				self.db.moments.update_one(  
						{"prompt" : next_moment["prompt"]}, 
						{'$set':{
							"available": True
							}
				})

		




















































		

