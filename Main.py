# -*- coding: utf-8 -*-
from NpcClass import *
from UserClass import *
from RoomClass import *
from StorageClass import *
from ItemClass import *
from Initialize import *
import re

"""
Starts and Ends Game
"""
'''
def createObjects():
    furniture = [StorageClass.Storage("front cabinet",2, None, "cabinet in the front of the room"),
                StorageClass.Storage("back cabinet",2, None, "cabinet in the back of the room"),
                StorageClass.Storage("front desk",2, None, "desk in the front of the room"),
                StorageClass.Storage("phone charging station",1,None, "phone charging station")]
    Rm170 = RoomClass.Room("CSE Classroom", 170, furniture, True) 
    Hanas = NpcClass.boss("Mr. Hanas", "roll", 1, None)
'''
mainChar = None
endStr = "\n\t(+)  "

RoomList = {"120":Rm120, "125":Rm125, "130":Rm130, "145":ChemLab, "155":Bio, "170":CSE, "185":Rm185, 
            "tech":TechLab, "main":MainOffice, "nurse":NurseOffice}

def mainloop():
	gameStart()

	while True:
		print "You enter the hallway."
		userIn = getQuery().strip().lower() # the response of the user -> pls don't remove the mothod to get the query
		userCMD = " ".split(userIn) # for multiple word commands
		if userIn in ("help", "h"):
			#print helpStr  <-- This will be defined in another python file
			continue
		elif '?' in userIn:
			objAsked = userIn.strip("?")
			print objAsked
			"""
			Now there are a few steps to take:
				try and match the string to an object's name
				state an error and write 'continue' if there is none
			"""
		elif "view" == userIn[0]:
			if userIn[1] in ("backpack", "inventory", "items", "stuff"):
				print "These are your items:"
				for item in mainChar.getItems():
					print "\n\t" + item
				print "You have a total of %d items in your inventory and a carrying capacity of %d items."%(len(mainChar.getItems()), mainChar.space)
		# add if and elifs for every keyword in the doc

def gameStart():
	print "Welcome to Escape HTHS!" # introduction text
	name = raw_input("What is your name?" + endStr) # name of the user
	items = [] # items the user starts with, prepopulate if necessary
	keys = [] # maybe start with a key to the first room?
	health = 10 # change health if necessary
	global mainChar
	mainChar = User(name, items, keys, health)
	print "You just failed your finals! You were supposed to be able to go home at 2:20, but now you are going to be held at HTHS for the rest of the summer. The only way to get out is to escape — but you have to figure out how. You are currently stuck in the CSE room, staring at unfinished Python code that you must complete. Until you do, there will be no food or water provided. It wouldn’t be too bad, except that the Python assignment is absolutely impossible. You have no clue how to complete it."
	print "The clock on the wall reads 2:30. Mr. Hanas is sitting at his table, fiddling with a six-sided die in his hand. You notice a 20-sided die sitting on the table next to you, left there by a Dungeons and Dragons player."
	#Mr. Hanas boss fight
	return

def getQuery():
	"""
	Ask the user for what they want to do as an action

	"""
	query = raw_input("What would you like to do?\nType\n\t'help' for a help menu\n\t'<object>?' for an object's description" + endStr) # take note of this.  The help is really important
	return query




if __name__ == "__main__": # this automatically runs the program when executed (opened in a shell)
	mainloop()