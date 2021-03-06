from pymongo import MongoClient

def seedNudge(nudgeStories):
	
	nudgeStories.insert({ 
	# Story 1:
		"id": "story1",
		"sequence": ["You're doing well, runner 5. Keep this pace and, if you feel safe enough, run towards [ENTERLOCATION] to gather some intel for us.", "Our intel is telling us that [ENTERLOCATION] might be a safe place for a settlement, run that direcion to check it out if you can.", "Ok, don't freak out runner 5, but Zombies are close, run towards [ENTERLOCATION] if you can, it should be safe in that area for you."]
	})


def seedDefault(defaultStories):
	
	defaultStories.insert({ 

	# Story 1:
		"id": "story1",
		"sequence": ["intro", "warm-up", "stable", "cool-down", "end"],
		"intro": "Hey there, runner number 5. You can hear me alright, yeah? I'm Violet and I'm your designated guide! We need you to get back to base safely and gather some important information for us about the Northwestern Campus so we can send out more teams to gather resources. Got it? Good. Ok. I see you're starting out now -- keep a good pace and stay alert",
		"warm-up": "We're gonna start you off slow, runner 5. Slowly build up your pace little by little to warm up",
		"stable": "We've lost some of our agents, runner 5, you're our only hope, we're going to need you to pick up the pace and gather more intel for us",
		"cool-down": "You've gotten us great intel, runner 5, slow down a little to conserve your energy",
		"end": "Great job, runner 5. You had very few run-ins with zombies and collected incredibly important data for us. You're within our base range now and you are safe. Until our next mission together!"
	})



def seed(moments, worldObjects):
	
	moments.insert({ 

	# THE ROCK 

		"name": "Expand",
		"prompt": "There are zombies on your tail, run to the stronghold at the Rock. Sprint by the rock to mark it for our records.",
		"id": "rock",
		"attribute": "rock-exists",
		"unlock": "rock-guarded",
		"available": True,
		"radius": 200
	})

	moments.insert({ 
		"name": "Expand",
		"prompt": "If you see someone guarding the Rock, then our fortress in the area is still going strong, otherwise sprint past the Rock.",
		"id": "rock",
 		"unlock": "rock-crowded",
		"available": False,
		"radius": 200
	})
	moments.insert({
		"name": "Expand",
		"prompt": "The Rock is being guarded, which means it is safe. However, are lots of people crowding the area by it? If so, zombies will arrive soon so sprint away.",
		"id": "rock",
		"attribute": "rock-crowded",
		"unlock": None,
		"available": False,
		"radius": 200
	})


	# NORRIS

	moments.insert({
		"name": "Expand",
		"prompt": "Our sources are telling us Norris seems to be safer than where you are headed, jog to Norris and sprint into it immediately.",
		"id": "Norris",
		"attribute": "norris-exists",
		"unlock": "norris-no-line",
		"available": True,
		"radius": 200
	})

	moments.insert({
		"name": "Expand",
		"prompt": "Jog into Norris and up towards the Starbucks -- if there is no line Zombies have been here recently. Sprint out of there.",
		"id": "Norris",
		"attribute": "norris-no-line",
		"unlock": "norris-crowded",
		"available": False,
		"radius": 200
	})

	moments.insert({
		"name": "Expand",
		"prompt": "There is no line at the Starbucks, but check the surrounding area in Norris - is it crowded? If so, sprint out of there.",
		"id": "Norris",
		"attribute": "norris-crowded",
		"unlock": None,
		"available": False,
		"radius": 200
	})

	# TODO rest

	moments.insert({ 
		"name": "Expand",
		"prompt": "The Garrett Parking Lot is coming up on your right and zombies are close. Jog into the lot to look for cover.",
		"id": "Garrett",
		"attribute": "garrett-exists",
		"unlock": "garrett-full",
		"available": True,
		"radius": 200
	})
	moments.insert({ 
		"name": "Expand",
		"prompt": "If you see many cars in the lot and few empty spots then there it will provide cover from the zombies, weave through the cars in the lot to throw the zombies off. Otherwise, sprint out of the lot and continue on quickly.",
		"id": "Garrett",
		"attribute": "garrett-full",
		"unlock": None,
		"available": False,
		"radius": 200
	})

	moments.insert({ 
		"name": "Expand",
		"prompt":  "Cut through the Plex courtyard to avoid Zombies on your path. You should sprint there",
		"id": "Plex",
		"attribute": "Plex-exists",
		"unlock": "Plex-full",
		"available": True,
		"radius": 200
	})

	moments.insert({ 
		"name": "Expand",
		"prompt":  "Run through the main courtyard of Plex. If the dining hall through the windows is packed, sprint as fast as you can out of there. Zombies will be there in no time.",
		"id": "Plex",
		"attribute": "Plex-full",
		"unlock": None,
		"available": False,
		"radius": 200
	})
	
	moments.insert({ 
		"name": "Expand",
		"prompt":  "There is a park nearby. There is a pack of zombies on your tail and the park might provide cover -- sprint quickly.",
		"id": "Tallmadge Park",
		"attribute": "Tallmadge-exists",
		"unlock": "Tallmadge-foliage",
		"available": True,
		"radius": 200
	})

	moments.insert({ 
		"name": "Expand",
		"prompt":  "Great you made it. We're considering setting up a small settlement here. If there is a thick foliage for cover in the area, run a path circumventing the park. Otherwise, keep heading on.",
		"id": "Tallmadge Park",
		"attribute": "Tallmadge-foliage",
		"unlock": None,
		"available": False,
		"radius": 200
	})

	moments.insert({ 
		"name": "Expand",
		"prompt":  "We have a settlement set up at Coffee Lab, run to it to check in.",
		"id": "Coffee Lab",
		"attribute": "Coffee-lab-exists",
		"unlock": "Coffee-lab-full",
		"available": True,
		"radius": 200
	})
	moments.insert({ 
		"name": "Expand",
		"prompt":  "This is an old settlement -- if it is overrun with people, sprint past -- Zombies will be here in no time -- otherwise pause for a moment to regain your energy.",
		"id": "Coffee Lab",
		"attribute": "Coffee-lab-full",
		"unlock": None,
		"available": False,
		"radius": 200
	})

	moments.insert({ 
		"name": "Expand",
		"prompt":  "The local grocery store D&Ds might have leftover food. Peak inside. If there are lots of people, sprint past, otherwise slowly jog past.",
		"id": "D&Ds",
		"attribute": "D&Ds-exists",
		"unlock": None,
		"available": True,
		"radius": 50
	})
	
	# moments.insert({ 
	# 	"name": "Explore",
	# 	"prompt":  "You are in unexplored territory, runner 5. Keep an eye out for parking spots -- those usually mean residents fled quickly and left behind valuables. If you see some in the area, reduce your pace and try to memorize the area so we can come back later and pick resources up. Otherwise, keep continuing on to base.",
	# 	"id": "NA",
	# 	"radius": 0
	# })

	# moments.insert({ 
	# 	"name": "Explore",
	# 	"prompt":  "Hey there runner 5, do you see any fire hydrants nearby? If you do, mark it for us by sprinting to it and pausing. We need to know where they can be found for when we start sending teams out.",
	# 	"id": "NA",
	# 	"radius": 0
	# })

	# moments.insert({ 
	# 	"name": "End",
	# 	"prompt":  "Great job, runner 5. You had very few run-ins with zombies and collected incredibly important data for us. You're within our base range now and you are safe. Until our next mission together!",
	# 	"id": "NA",
	# 	"radius": 0
	# })

	worldObjects.insert({
		"name": "the rock",
		"lat": 42.051507,
		"lng": -87.675919,
		"attributes": {"rock-exists": [None, 0], "rock-guarded": [None, 0], "rock-crowded": [None, 0]}
	})
	worldObjects.insert({
		"name": "Norris",
		"lat": 42.053384, 
		"lng": -87.672949,
		"attributes": {"norris-exists": [None, 0], "norris-no-line": [None, 0], "norris-crowded": [None, 0]}
	})
	worldObjects.insert({
		"name": "Garrett",
		"lat": 42.055600,
		"lng": -87.676569,
		"attributes": {"garrett-exists": [None, 0], "garrett-full": [None, 0]}
	})
	worldObjects.insert({
		"name": "Plex",
		"lat": 42.052936,
		"lng": -87.679330,
		"attributes": {"Plex-exists": [None, 0], "Plex-full": [None, 0]}
	})
	worldObjects.insert({
		"name": "Tallmadge Park",
		"lat": 42.054570,
		"lng": -87.682204,
		"attributes": {"Tallmadge-exists": [None, 0], "Tallmadge-foliage": [None, 0]}
	})
	worldObjects.insert({
		"name": "Coffee Lab",
		"lat": 42.0583,
		"lng": -87.6837,
		"attributes": {"Coffee-lab-exists": [None, 0], "Coffee-lab-full": [None, 0]}
	})
	worldObjects.insert({
		"name": "D&Ds",
		"lat": 42.058701,
		"lng": -87.683191,
		"attributes": {"D&Ds-exists": [None, 0]}
	})
	

