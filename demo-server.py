from flask import Flask, request
from opportunity import OpportunityManager
from verify import ActionVerifier
import time

app = Flask(__name__)
opportunityManager = OpportunityManager()
# actionVerifier = ActionVerifier()

@app.route('/location', methods = ['POST'])
def save_location():
	if request.method == 'POST':
		data = request.get_json()
		latStr = str(data['latitude'])
		lngStr = str(data['longitude'])
		timeStr = str(time.time())
		with open('data.txt','a') as file:
			save_string = latStr+','+lngStr+','+timeStr+'\n'
			print save_string
			file.write(save_string)
	return opportunityManager.get_moment(float(latStr),float(lngStr))

# @app.route('/verify', methods = ['POST'])
# def verify_action():
# 	if request.method == 'POST':
# 		data = request.get_json()
# 		to_verify = data['to_verify']
# 		from_timestamp = data['from_timestamp']
# 		return str(actionVerifier.verify(to_verify, from_timestamp))
# 	return str(False)
		
