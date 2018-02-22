# -*- coding: utf-8 -*-
#I'm just playing aroud with this and seeing if my idea works - Anna
from NpcClass import *
from UserClass import *
from RoomClass import *
from StorageClass import *
from ItemClass import *
from Initialize import *
import Help
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

roomList = {"120":Rm120, "125":Rm125, "130":Rm130, "145":ChemLab, "155":Bio, "170":CSE, "185":Rm185, 
			"tech":TechLab, "main":MainOffice, "nurse":NurseOffice}

def mainloop():
	gameStart()

	while True:
		print "\nYou enter the hallway." #probably take this out and add "exit to hallway" to text printed after leaving a room
		nextAction = getAction() # we shouldn't have code like this running in the main method, the getAction should take care of it
		if nextAction == "help":
			print "this is a placeholder" #print helpStr  <-- This will be defined in another python file/function
		elif nextAction == "stats":
			print "\nName: " + mainChar.name
			print "HP: " + str(mainChar.health) + "/10" #fsr this doesn't work
		elif nextAction == "items":
			print "\nThese are your items:"
			for item in mainChar.getItems():
				print "\n\t" + item
			print "You have a total of %d items in your inventory and a carrying capacity of %d items."%(len(mainChar.getItems()), mainChar.space)
		elif nextAction == "escape":
				break #check keys
		elif nextAction == "room":
				print "\nList of Rooms:"
				for room in roomList:
					print "\"" + room + "\"" + ": " + roomList[room].name
				userIn = raw_input().strip().lower()
				if userIn in roomList:
					pass #call function that tests if rooms are locked or need items
				else:
					print "Sorry, room not recognized."
		else:
			print "Sorry, action not recognized."
	print "Congrats! You escaped HTHS!"

def gameStart():
	print "Welcome to Escape HTHS!" # introduction text
	name = raw_input("What is your name?" + endStr) # name of the user
	items = [] # items the user starts with, prepopulate if necessary
	keys = [] # maybe start with a key to the first room?
	health = 10 # change health if necessary
	global mainChar
	mainChar = User(name, items, keys, health)
	print "You just failed your finals! You were supposed to be able to go home at 2:20, but now you are going to be held at HTHS for the rest of the summer. The only way to get out is to escape - but you have to figure out how. You are currently stuck in the CSE room, staring at unfinished Python code that you must complete. Until you do, there will be no food or water provided. It wouldn't be too bad, except that the Python assignment is absolutely impossible. You have no clue how to complete it."
	print "\nThe clock on the wall reads 2:30. Mr. Hanas is sitting at his table, fiddling with a six-sided die in his hand. You notice a 20-sided die sitting on the table next to you, left there by a Dungeons and Dragons player."
	#Mr. Hanas boss fight
	return

def getAction(room=None):
	actions = {}
	userIn = raw_input("\nWhat will you do?" + endStr).strip().lower()
	'''
	if room == None:
		actions["room"] = "Enter a room"
		actions["stats"] = "View your stats"
		actions["items"] = "View and use items"
		actions["escape"] = "Escape HTHS!"
	else: #rooms should probably also have a dictionary with actions, esp 120/130
		for each in room.furniture:
			actions[each.name] = each.description #should add another parameter for this text?
		actions["stats"] = "View your stats"
		actions["items"] = "View and use items"
		actions["leave"] = "Leave room"
	actions["help"] = "Get help text"
	'''
	userCMD = userIn.split(" ") # for multiple word commands
	print "UserIn:\t" + str(userIn)
	print "UserCMD:\t" + str(userCMD)
	if userIn in ("help", "h"):
		print Help.HelpMenu # print helpStr  <-- This will be defined in another python file
		return "done"
	elif '?' in userIn:
		objAsked = userIn.strip("?")
		print objAsked # take this string and get the object being asked about, then print the description
		return "done"
	elif len(userCMD) < 2:
		print "Invalid Action.  Please try again."
		getAction(room)
	elif userCMD[0] == "view":
		if userCMD[1] in ("backpack", "inventory", "items", "stuff"):
			print "These are your items:"
			for item in mainChar.getItems():
				print "\n\t" + item
			print "You have a total of %d items in your inventory and a carrying capacity of %d items."%(len(mainChar.getItems()), mainChar.space)
			return "done"
		elif userCMD[1] == "stats":
			print "\nName: " + mainChar.name
			print "HP: " + str(mainChar.health) + "/10" #fsr this doesn't work <-- cast into a string first
			return "done"
	elif userCMD[0] == "rename":
		oldName = mainChar.getName()
		mainChar.changeName(userCMD[1])
		print "You used to be %s but now you've covertly changed your name to %s"%(oldName, userCMD[1])
		return "done"
	elif userCMD[0] == "escape":
		return "escape" #check keys
	elif userCMD[0] == "quit":
		print "never quit\nnever never ever ever quit"
		return "done"
	elif userCMD[0] in ("leave", "exit"):
		if room != None:
			return "leave"
	##
	# add more code for other actions here, where userCMD[0] is the command name or first term and userCMD[1] is the object, action, or name
	# see the Help.HelpMenu for a working list of commands
	##

	'''
	elif nextAction == "room":
			print "\nList of Rooms:"
			for room in roomList:
				print "\"" + room + "\"" + ": " + roomList[room].name
			userIn = raw_input().strip().lower()
			if userIn in roomList:
				pass #call function that tests if rooms are locked or need items
			else:
				print "Sorry, room not recognized."
	else:
		print "Sorry, action not recognized."
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

	for each in actions:
		print "\"" + each + "\"" + ": " + actions[each]
	userIn = raw_input(endStr).strip().lower()
	
	if userIn in actions:
		return userIn
	else:
		return "nope"
	'''


if __name__ == "__main__": # this automatically runs the program when executed (opened in a shell)
	mainloop()