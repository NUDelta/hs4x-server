from pymongo import MongoClient

def seed(moments, worldObjects):
	moments.insert({ 
		"name": "Intro",
		"prompt": "Hey there, runner number 5. You can hear me alright, yeah? I'm Violet and I'm your designated guide! So don't worry. Well, worry a little bit. I'm watching you from an outlook in the base, so I can keep watch and warn you if you're in danger - but you have to do the running and be quick. We need you to get back to base safely and gather some important information for us about the Northwestern Campus so we can send out more teams to gather resources. Got it? Good. Ok. I see you're starting out now -- keep a good pace and stay alert",
		"id": "NA",
		"radius": 0
	})
	moments.insert({ 
		"name": "Expand",
		"prompt": "There are zombies on your tail, run to the stronghold at the Rock between Harris Hall and University Hall.",
		"id": "rock",
		"radius": 70
	})
	moments.insert({
		"name": "Exploit",
		"prompt": "If you see someone guarding the Rock, then our fortress in the area is still going strong and you are safe to continue on your way towards Tech. Otherwise, canvas the area by running around the Rock and then continue to your original destination.",
		"id": "rock",
		"radius": 50
	})
	moments.insert({
		"name": "Expand",
		"prompt": "There are zombies coming towards you on Sheridan, jog to Norris if you want to avoid them.",
		"id": "Norris",
		"radius": 100

	})
	moments.insert({
		"name": "Exploit",
		"prompt": "Jog into Norris and up towards the Starbucks -- if it is crowded the zombies are probably on their way -- leave quickly via the door you entered. Otherwise, leave Norris through a different entrance to throw the zombies off your tail.",
		"id": "Norris",
		"radius": 50
	})
	moments.insert({ 
		"name": "Expand",
		"prompt": "The Garrett Parking Lot is coming up on your right and zombies are close. Jog into the lot to look for cover.",
		"id": "Garrett",
		"radius": 100
	})
	moments.insert({ 
		"name": "Exploit",
		"prompt": "If you see many cars in the lot and few empty spots then there it will provide cover from the zombies, weave through the cars in the lot to throw the zombies off. Otherwise, sprint out of the lot and continue on quickly.",
		"id": "Garrett",
		"radius": 50
	})
	moments.insert({ 
		"name": "Exploit",
		"prompt":  "Run through the main courtyard. If the dining hall through the windows is packed, sprint as fast as you can out of there. Zombies will be there in no time. If not, keep your pace steady.",
		"id": "Plex",
		"radius": 100
	})
	moments.insert({ 
		"name": "Explore",
		"prompt":  "Hey there runner 5, do you see any fire hydrants nearby? If you do, mark it for us by sprinting to it and pausing. We need to know where they can be found for when we start sending teams out.",
		"id": "NA",
		"radius": 0
	})
	moments.insert({ 
		"name": "Expand",
		"prompt":  "There is a park due north of you. There is a pack of zombies on your tail and the park might provide cover -- sprint quickly!!",
		"id": "Tallmadge Park",
		"radius": 50
	})
	moments.insert({ 
		"name": "Exploit",
		"prompt":  "Great you made it. We're considering setting up a small settlement here. If there is a thick foliage for cover in the area, run a path circumventing the park. Otherwise, keep heading on.",
		"id": "Tallmadge Park",
		"radius": 20
	})
	moments.insert({ 
		"name": "Expand",
		"prompt":  "We have a settlement set up at Coffee Lab, run two blocks north and two west to check in there.",
		"id": "Coffee Lab",
		"radius": 100
	})
	moments.insert({ 
		"name": "Exploit",
		"prompt":  "This is an old settlement -- if it is overrun with people, sprint past -- Zombies will be here in no time -- otherwise pause for a moment to regain your energy.",
		"id": "Coffee Lab",
		"radius": 20
	})
	moments.insert({ 
		"name": "Explore",
		"prompt":  "You are in unexplored territory, runner 5. Keep an eye out for parking spots -- those usually mean residents fled quickly and left behind valuables. If you see some in the area, reduce your pace and try to memorize the area so we can come back later and pick resources up. Otherwise, keep continuing on to base.",
		"id": "NA",
		"radius": 0
	})
	moments.insert({ 
		"name": "Expand",
		"prompt":  "The local grocery store D&Ds might have leftover food. Peak inside. If there are lots of people, sprint past, otherwise slowly jog past.",
		"id": "D&Ds",
		"radius": 50
	})
	moments.insert({ 
		"name": "End",
		"prompt":  "Great job, runner 5. You had very few run-ins with zombies and collected incredibly important data for us. You're within our base range now and you are safe. Until our next mission together!",
		"id": "NA",
		"radius": 0
	})

	worldObjects.insert({
		"name": "rock",
		"lat": 42.051507,
		"lng": -87.675919,
		"responses": 5	
	})
	worldObjects.insert({
		"name": "Norris",
		"lat": 42.053384, 
		"lng": -87.672949,
		"responses": 5	
	})
	worldObjects.insert({
		"name": "Garrett",
		"lat": 42.055600,
		"lng": -87.676569,
		"responses": 5	
	})
	worldObjects.insert({
		"name": "Plex",
		"lat": 42.052936,
		"lng": -87.679330,
		"responses": 2	
	})
	worldObjects.insert({
		"name": "Tallmadge Park",
		"lat": 42.054570,
		"lng": -87.682204,
		"responses": 4	
	})
	worldObjects.insert({
		"name": "Coffee Lab",
		"lat": 42.0583,
		"lng": -87.6837,
		"responses": 7	
	})
	worldObjects.insert({
		"name": "D&Ds",
		"lat": 42.058701,
		"lng": -87.683191,
		"responses": 2	
	})
	worldObjects.insert({
		"name": "test-obj",
		"lat": 42.05909,
    	"lng": -87.674446,
    	"responses": 5
	})

dbName = "hs4x"
#uri= "mongodb://localhost:27017"
uri= "mongodb://ob:kim@ds153577.mlab.com:53577/hs4x"
client = MongoClient(uri)
db = client[dbName]
