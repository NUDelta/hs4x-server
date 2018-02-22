import json
import time
import sys
from bson import json_util
from pymongo import MongoClient
from math import sin, cos, sqrt, atan2, radians


class OpportunityManager():
	def __init__(self):
		uri= "mongodb://ob:kim@ds153577.mlab.com:53577/hs4x"
		#uri= "mongodb://localhost:27017"

		dbName = "hs4x"
		client = MongoClient(uri)
		self.db = client[dbName]

		#load moments and objects from DB
		self.moments = list(self.db.moments.find())
		self.objects = list(self.db.worldObjects.find())
		#self.sent = set()

	#	called by endpoint, finds all moments in range,
	#	filters out any it's already sent, and
	#	returns the one with the fewest responses
	def get_moment(self,lat,lng):
		moments_in_range = self.get_moments_in_range(lat,lng)
		if len(moments_in_range) > 0:
			valid_moments = [ moment for moment in moments_in_range ] # if moment["prompt"] not in self.sent 
			best_moment = self.get_best_moment(valid_moments)
			#best_moment can return {}, so check if empty
			if len(best_moment.keys()) == 0:
				return {}
			else:
				best_moment = [json.loads(json.dumps(best_moment, default=json_util.default))]
				#self.sent.add(best_moment[0]["prompt"])
				return best_moment
		return {}


	#returns all moments within range of lat, lng
	def get_moments_in_range(self,lat,lng):
		moments_in_range = []
		expands = self.db.moments.find({"name": "Expand"})
		for moment in expands:
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
			

	#returns moment from given array of moments with fewest responses
	def get_best_moment(self, moments):
		fewest_responses = sys.maxint
		best_moment = {}
		for moment in moments:
			momentId = moment["id"]
			reponses = self.db.worldObjects.find({"name": momentId})
			response = list(reponses)[0]["responses"]
			if response < fewest_responses:
				fewest_responses = response
				best_moment = moment
		return best_moment

	#stackoverflow function to compute distance. accurate to a couple ft
	def estimate_distance(self,lat1,lng1,lat2,lng2):
		# approximate radius of earth in km
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
