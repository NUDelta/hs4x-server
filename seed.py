from pymongo import MongoClient

def seed(moments, worldObjects):
	moments.insert({ 
		"name": "Expand",
		"prompt": "There are zombies on your tail, run to the stronghold at the Rock between Harris Hall and University Hall.",
		"id": "rock",
		"radius": 400
	})
	moments.insert({
		"name": "Exploit",
		"prompt": "If you see someone guarding the Rock, then our fortress in the area is still going strong and you are safe to continue on your way towards Tech. Otherwise, canvas the area by running around the Rock and then continue to your original destination.",
		"id": "rock",
		"radius": 100
	})
	moments.insert({
		"name": "Expand",
		"prompt": "There are zombies coming towards you on Sheridan, jog to Norris if you want to avoid them.",
		"id": "Norris",
		"radius": 1400
	})
	moments.insert({
		"name": "Exploit",
		"prompt": "Jog into Norris and up towards the Starbucks -- if it is crowded the zombies are probably on their way -- leave quickly via the door you entered. Otherwise, leave Norris through a different entrance to throw the zombies off your tail.",
		"id": "Norris",
		"radius": 100
	})
	moments.insert({ 
		"name": "Expand",
		"prompt": "The Garrett Parking Lot is coming up on your right and zombies are close. Jog into the lot to look for cover.",
		"id": "Garrett",
		"radius": 250
	})
	moments.insert({ 
		"name": "Exploit",
		"prompt": "If you see many cars in the lot and few empty spots then there it will provide cover from the zombies, weave through the cars in the lot to throw the zombies off. Otherwise, sprint out of the lot and continue on quickly.",
		"id": "Garrett",
		"radius": 85
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

dbName = "hs4x"
uri= "mongodb://localhost:27017"
client = MongoClient(uri)
db = client[dbName]

# Collections based on Experience Kit
moments = db["moments"] # Individual interactions
worldObjects = db["worldObjects"] # Objects with locations