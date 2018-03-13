import json
import time
import sys
from bson import json_util
from bson import ObjectId
from pymongo import MongoClient
from math import sin, cos, sqrt, atan2, radians


class OpportunityManager():
	def __init__(self):
		uri= "mongodb://ob:kim@ds153577.mlab.com:53577/hs4x"
		#uri= "mongodb://localhost:27017"
		dbName = "hs4x"
		client = MongoClient(uri)
		self.db = client[dbName]
		self.moments = list(self.db.moments.find())
		self.objects = list(self.db.worldObjects.find())

	#	Find all moments in range
	#	Find the one with the least number of responses
	#	Make sure it has not already been sent
	# 	Return to frontend
	def get_moment(self, run_id, lat,lng):
		moments_in_range = self.get_moments_in_range(lat,lng)
		if len(moments_in_range) > 0:
			valid_moments = [ moment for moment in moments_in_range ] # if moment["prompt"] not in self.sent 
			best_moment = self.get_best_moment(valid_moments)
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
				print("Send this moment to front end. Add to run's played moments")
				best_moment = [json.loads(json.dumps(best_moment, default=json_util.default))]
				self.db.runs.update(
					{"_id" : ObjectId(run_id)}, 
					{"$addToSet":{"moments_played": prompt}})
				return best_moment
		return None

	# Returns all moments within range of lat, lng
	def get_moments_in_range(self,lat,lng):
		moments_in_range = []
		list_expand_exploits = []
		expands = self.db.moments.find({"name": "Expand"})
		exploits = self.db.moments.find({"name": "Exploit"})
		for expand in expands:
			list_expand_exploits.append(expand)
		for exploit in exploits:
			list_expand_exploits.append(exploit)
		for moment in list_expand_exploits:
			objectId = moment["id"]
			objectRadius = moment["radius"]
			obj = self.db.worldObjects.find({"name":objectId})
			obj = list(obj)
			if len(obj) > 0:
				obj = obj[0]
				objectLat = float(obj["lat"])
				objectLng = float(obj["lng"])
				if self.estimate_distance(lat,lng,objectLat,objectLng) < objectRadius:
					moments_in_range.append(moment)
				else:
					pass
		return moments_in_range
			

	# Returns moment from given array of moments with fewest responses
	def get_best_moment(self, moments):
		fewest_responses = sys.maxint
		best_moment = {}
		for moment in moments:
			momentId = moment["id"]
			reponses = self.db.worldObjects.find({"name": momentId})
			response = list(reponses)[0]["responses"]
			# Exploits and expands on the same object have the same number of responses, but we always want to smaller range one
			if response == fewest_responses and momentId == best_moment["id"] and (moment["radius"] < best_moment["radius"]):
				best_moment = moment
			elif response < fewest_responses:
				fewest_responses = response
				best_moment = moment
		return best_moment

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
