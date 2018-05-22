from pymongo import MongoClient

def seed2(moments, worldObjects):
	moments.insert({ 
		"name": "Expand",
		"prompt": "From here, you can see the Basketball court -- a prime spot for zombies. If you see zombies on the court cross the street quickly.",
		"id": "Basketball",
		"radius": 50
	})
	moments.insert({ 
		"name": "Expand",
		"prompt": "Sargent hall is one of our strongholds. Peak in. Is it empty? If so, get out of there fast.",
		"id": "Sargent",
		"radius": 50
	})
	moments.insert({ 
		"name": "Expand",
		"prompt": "Mudd is up ahead. Is there construction happening nearby? Run away if so. The noise might attract zombies!",
		"id": "Mudd",
		"radius": 20
	})
	moments.insert({ 
		"name": "Expand",
		"prompt": "There is a parking lot by you. Are many cars parked in it? If so run through the lot and look for leftover resources!",
		"id": "Lot",
		"radius": 20
	})
	
	worldObjects.insert({
		"name": "Basketball",
		"lat": 42.059143,
    	"lng": -87.674594,
    	"responses": 5
	})
	worldObjects.insert({
		"name": "Sargent",
		"lat": 42.058922, 
    	"lng": -87.675175,
    	"responses": 5
	})
	worldObjects.insert({
		"name": "Mudd",
		"lat": 42.058730, 
    	"lng": -87.674684,
    	"responses": 5
	})
	worldObjects.insert({
		"name": "Lot",
		"lat": 42.059105, 
    	"lng": -87.673066,
    	"responses": 5
	})

