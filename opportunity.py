import json

class OpportunityManager():

	def __init__(self):
		self.times_pinged = 0

		with open('moments.json') as file:
		    self.moments = json.load(file)

	def get_moment(self):
		self.times_pinged += 1
		if self.times_pinged > 5:
			context_scores = self.get_context_scores()
			return json.dumps(self.moments[context_scores.index(max(context_scores))])
		else:
			return "{}"

	def get_context_scores(self):
		context_scores = []
		for moment in self.moments:
			context_scores.append(1)
		return context_scores