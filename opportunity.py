import json
import time

class OpportunityManager():

	def __init__(self):
		self.times_pinged = 0
		# Keep track of the last 4x stage sent to frontend
		self.last_stage = None
		self.stage1_sent = None

		with open('moments.json') as file:
		    self.moments = json.load(file)

	def get_moment(self, id):
		print self.last_stage
		if id == "1":
			self.times_pinged += 1
		if self.times_pinged > 1 and id == "1":
			# context_scores = self.get_context_scores()
			# return json.dumps(self.moments[context_scores.index(max(context_scores))])
			self.last_stage = 0
			return json.dumps(self.moments[0])
		elif self.last_stage >= 0 and self.last_stage < 2 and id == "2":
			if self.last_stage == 0:
				self.stage1_sent = time.time()
				self.last_stage += 1
				return json.dumps(self.moments[self.last_stage])
			elif time.time() - self.stage1_sent > 6:
				self.last_stage += 1
				return json.dumps(self.moments[self.last_stage])
			else:
				return "{}"
		else:
			return "{}"

	# def get_context_scores(self):
	# 	context_scores = []
	# 	for moment in self.moments:
	# 		context_scores.append(1)
	# 	return context_scores