this is the code for the hs4x backend using flask (python).

files:
	all_moments.json - all the moments we've brainstormed, for pasting into moments.json

	moments.json - moments to be available for the current run

	data.txt - the "database" for lat,lng,timestamp (and eventually accel)

	demoserver.py - entry point with code for all endpoints

	objects.json - each moment corresponds to an object, which are defined in this file

	opportunity.py - opportunity manager code for returning the best moments

	Procfile - necessary to build on heroku, tells it to use gunicorn to run the server with one worker (more than one worker can service multiple requests at once, but then multiple versions of state as well)

	requirements.txt - also for heroku, tells it which python packages are needed

	runtime.txt - specifies python version to use

	verify.py - action verifier code, unused for now

	venv/ - virtualenv for downloading python packages to the project and not to local dev machine


build instructions:
	- can ignore all other branches, master is the most up to date. code is on master bc it needs to be to push to heroku (git push heroku master)
	- to run locally, can type "heroku local"
	- to download pip packages from requirements.txt, type "pip install -r requirements.txt"
