import json
import time
import sys
from math import sin, cos, sqrt, atan2, radians

class OpportunityManager():

	def __init__(self):
		with open('moments.json') as file:
		    self.moments = json.load(file)
		with open('objects.json') as file:
		    self.objects = json.load(file)
		self.sent = {}


	def get_moment(self,lat,lng):
		moments_in_range = self.get_moments_in_range(lat,lng)
		valid_moments = [ moment for moment in moments_in_range if moment["prompt"] not in self.sent.keys() ]
		best_moment = self.get_best_moment(valid_moments)
		if len(best_moment.keys()) == 0:
			print "{}"
			return "{}"
		else:
			self.sent[best_moment["prompt"]] = True
			print json.dumps(best_moment)
			return json.dumps(best_moment)

	def get_moments_in_range(self,lat,lng):
		moments_in_range = []
		for moment in self.moments:
			objectId = moment["id"]
			objectRadius = moment["radius"]
			objectLat = float(self.objects[objectId]["lat"])
			objectLng = float(self.objects[objectId]["lng"])
			if self.estimate_distance(lat,lng,objectLat,objectLng) < objectRadius:
				moments_in_range.append(moment)
		return moments_in_range

	def get_best_moment(self, moments):
		fewest_responses = sys.maxint
		best_moment = {}
		for moment in moments:
			momentId = moment["id"]
			objectResponses = self.objects[momentId]["responses"]
			if objectResponses < fewest_responses:
				fewest_responses = objectResponses
				best_moment = moment
		return best_moment

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