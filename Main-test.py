# -*- coding: utf-8 -*-
#I'm just playing aroud with this and seeing if my idea works - Anna
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

roomList = {"120":Rm120, "125":Rm125, "130":Rm130, "145":ChemLab, "155":Bio, "170":CSE, "185":Rm185, 
            "tech":TechLab, "main":MainOffice, "nurse":NurseOffice}

def mainloop():
	gameStart()

	while True:
		print "\nYou enter the hallway." #probably take this out and add "exit to hallway" to text printed after elaving a room
		nextAction = getAction()
		if nextAction == "help":
			print "this is a placeholder" #print helpStr  <-- This will be defined in another python file/function
		elif nextAction == "stats":
			print "\nName: " + mainChar.name
			print "HP: " + mainChar.health + "/10" #fsr this doesn't work
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
	print "You just failed your finals! You were supposed to be able to go home at 2:20, but now you are going to be held at HTHS for the rest of the summer. The only way to get out is to escape — but you have to figure out how. You are currently stuck in the CSE room, staring at unfinished Python code that you must complete. Until you do, there will be no food or water provided. It wouldn’t be too bad, except that the Python assignment is absolutely impossible. You have no clue how to complete it."
	print "\nThe clock on the wall reads 2:30. Mr. Hanas is sitting at his table, fiddling with a six-sided die in his hand. You notice a 20-sided die sitting on the table next to you, left there by a Dungeons and Dragons player."
	#Mr. Hanas boss fight
	return

def getAction(room=None):
	actions = {}
	print "\nWhat do you do?"
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
	for each in actions:
	    print "\"" + each + "\"" + ": " + actions[each]
	userIn = raw_input().strip().lower()
	if userIn in actions:
	    return userIn
	else:
	    return "nope"


if __name__ == "__main__": # this automatically runs the program when executed (opened in a shell)
	mainloop()