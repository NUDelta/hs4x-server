from flask import Flask, request
from opportunity import OpportunityManager
from verify import ActionVerifier
import time

app = Flask(__name__)
opportunityManager = OpportunityManager()
actionVerifier = ActionVerifier()

@app.route('/')
def hello_world():
	print 'hello world'
	return 'Hello, Worlds!'

@app.route('/location', methods = ['POST'])
def save_location():
	if request.method == 'POST':
		data = request.get_json()
		print 'lat:', data['latitude'], '-', 'long:', data['longitude']
		with open('data.txt','a') as file:
			save_string = str(data['latitude'])+','+str(data['longitude'])+','+str(time.time())+'\n'
			file.write(save_string)
	return 'saved!'

@app.route('/moments', methods = ['GET'])
def get_moments():
	return opportunityManager.get_moment()

@app.route('/verify', methods = ['POST'])
def verify_action():
	if request.method == 'POST':
		data = request.get_json()
		to_verify = data['to_verify']
		from_timestamp = data['from_timestamp']
		return str(actionVerifier.verify(to_verify, from_timestamp))
	return str(False)
		
