class ActionVerifier():

	def __init__(self):
		pass
	
	#implement these for each action
	def verify_sprint(self, data):
		return True

	def verify(self, to_verify, from_timestamp):
		with open('data.txt') as file:
			#get all data for certain period
			data_lines = file.readlines()
			data = [ line.split(',') for line in data_lines ]
			print data
			data_from_timestamp = [ d for d in data if float(d[2].strip()) >= from_timestamp ]

			#take relevant data and call corresponding action,
			#	specified by the moment
			if to_verify == "SPRINT":
				return self.verify_sprint(data_from_timestamp)
