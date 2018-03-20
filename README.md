this is the code for the hs4x backend using flask (python).

files:

	server.py - entry point with code for all endpoints. Contains connection to mlab, heroku server, and mongodb database. Sets up 		collections for database: experiences, moments, locations, motionActivityUpdates, worldObjects, and runs.

	opportunity.py - opportunity manager code for returning the best moments
	
	seed.py (and seed2.py) - brainstormed moments of type Expore, Expand, and Exploit along with corresponding worldObjects. This 		document can be used to seed the mongodb db database.

	Procfile - necessary to build on heroku, tells it to use gunicorn to run the server with one worker (more than one worker can service multiple requests at once, but then multiple versions of state as well)

	requirements.txt - also for heroku, tells it which python packages are needed

	runtime.txt - specifies python version to use

	verify.py - action verifier code, unused for now

	venv/ - virtualenv for downloading python packages to the project and not to local dev machine

build instructions:

	- can ignore all other branches, master is the most up to date. code is on master bc it needs to be to push to heroku (git push heroku master)
	- run LOCALLY: 
		- set uri = mongodb://localhost:27017 in both server.py and opportunity.py
		- run mongod in terminal window
		- (To seed if previously unseeded, add "seed(moments, worldObjects)" at beginning of server.py but only run the server 			with this line once! )
		- In another terminal window, run "python server.py"
	- run REMOTE:
		- set uri remote heroku server in server.py and opportunity.py
		- git add, git commit, push heroku master
		- (To seed if previously unseeded, add "seed(moments, worldObjects)" at beginning of server.py but only run the server 			with this line once! )
		- run "python server.py"
	- to download pip packages from requirements.txt, type "pip install -r requirements.txt"
