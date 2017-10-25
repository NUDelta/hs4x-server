class ActionVerifier():

	def __init__(self):
		pass
	
	def verify_sprint(self, data):
		return True

	def verify(self, to_verify, from_timestamp):
		with open('data.txt') as file:
			data_lines = file.readlines()
			data = [ line.split(',') for line in data_lines ]
			print data
			data_from_timestamp = [ d for d in data if float(d[2].strip()) >= from_timestamp ]

			if to_verify == "SPRINT":
				return self.verify_sprint(data_from_timestamp)
