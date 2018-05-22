from pymongo import MongoClient

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

