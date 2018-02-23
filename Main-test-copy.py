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
To Do:
    battle mode function (displays battle mode option when applicable but have yet to make a function that starts the actual battle)
    implement battle mode function in main code
    guardian stuff
    alternative description/blurbs for storage
    extra actions for each room
    120/130 divider stuff
    fix storage description issue (nurse's office)
'''
mainChar = None
endStr = "\n\t(+)  "

roomList = {"120":Rm120, "125":Rm125, "130":Rm130, "145":ChemLab, "155":Bio, "170":CSE, "185":Rm185, 
		"tech":TechLab, "main":MainOffice, "nurse":NurseOffice}

preplab = False

def mainloop():
	gameStart()

	while True:
		print "\nYou enter the hallway." #take this out after code is finished
		nextAction = getAction() # we shouldn't have code like this running in the main method, the getAction should take care of it
		if checkGenericAction(nextAction):
		    pass
		elif nextAction == "escape":
			if len(mainChar.keys) == 4:
			    break
			else:
			    print "\nYou don't have all the special keys."
			    print "but us creators need a way to quit lol"
			    break #REMOVE THIS WHEN FINISHED WITH CODE
		elif nextAction == "room":
			print "\nList of Rooms:"
			for room in roomList:
				print "\"" + room + "\"" + ": " + roomList[room].name
			userIn = raw_input(endStr).strip().lower()
			if userIn in roomList:
				room = roomList[userIn]
				canEnter = checkRoom(room)
				if canEnter:
				    print "\n" + room.getDescription()
				    while True:
				        userAction = getAction(room=room)
				        if checkGenericAction(userAction):
				            pass
				        elif userAction == "leave":
				            break
				        elif userAction in room.getStorageNames():
				            furniture = room.getStorage(userAction)
				            roomStorage(room, furniture) #possibly change take item function so room doesn't need to be parameter? see below
				        else:
				            print "\nSorry, action not recognized."
			else:
				print "\nSorry, room not recognized."
		else:
			print "\nSorry, action not recognized."
	print "\nCongrats! You escaped HTHS!"

def gameStart():
	print "Welcome to Escape HTHS!" # introduction text
	name = raw_input("What is your name?" + endStr) # name of the user
	items = [] # items the user starts with (none)
	keys = [] # keys that user starts with (none)
	global mainChar
	mainChar = User(name, items, keys, 10)
	print "\nYou just failed your finals! You were supposed to be able to go home at 2:20, but now you are going to be held at HTHS for the rest of the summer. The only way to get out is to escape - but you have to figure out how. You are currently stuck in the CSE room, staring at unfinished Python code that you must complete. Until you do, there will be no food or water provided. It wouldn't be too bad, except that the Python assignment is absolutely impossible. You have no clue how to complete it."
	print "\nThe clock on the wall reads 2:30. Mr. Hanas is sitting at his table, fiddling with a six-sided die in his hand. You notice a 20-sided die sitting on the table next to you, left there by a Dungeons and Dragons player."
	#Mr. Hanas boss fight
	return

def getAction(room=None, battle=False):
	actions = {}
	print "\nWhat do you do?"
	if battle:
	    print "battle action list!"
	    #program battle mode stuff
	elif room == None:
		actions["room"] = "Enter a room"
		actions["stats"] = "View your stats"
		actions["items"] = "View and use items"
		actions["escape"] = "Escape HTHS!"
	else: #rooms should probably also have a dictionary with actions, esp 120/130
		for each in room.getStorages():
			actions[each.name] = each.description #should add another parameter for this text?
		NPCs = room.getNPCs()
		if len(NPCs) > 0:
		    names = []
		    for NPC in NPCs:
		        names.append(NPC.getName())
		    if "Mr. Hanas" in names or "Mr. B" in names or "Mr. Bals" in names:
		        actions["battle"] = "Enter battle"
		
		actions["stats"] = "View your stats"
		actions["items"] = "View and use items"
		actions["leave"] = "Leave room"
	actions["help"] = "Get help text"
	for each in actions:
		print "\"" + each + "\"" + ": " + actions[each]
	userIn = raw_input(endStr).strip().lower()
	if userIn in actions:
		return userIn
	else:
		return "nope"

def checkGenericAction(action):
    if action == "help":
	print "this is a placeholder" #print helpStr  <-- This will be defined in another python file/function
	return True
    elif action == "stats":
	print "\nName: " + mainChar.name
	print "HP: " + str(mainChar.health) + "/10"
	return True
    elif action == "items":
        print "\nThese are your items:\n"
	for item in mainChar.getItems():
	   print "\t" + item.getName() + ": " + item.getDescription()
	print "\nYou have a total of %d items in your inventory and a carrying capacity of %d items."%(len(mainChar.getItems()), mainChar.space)
	print "You have a total of %d special key(s)."%(len(mainChar.keys))
	return True
    return False

def checkRoom(room):
    if not room.getLock() == "none":
        print "\nThe room is locked. Use item? (y/n)"
        userIn = raw_input(endStr).strip().lower()
        if userIn == "y":
            print "\nThese are your items:"
            item_names = []
	    for item in mainChar.getItems():
	       item_names.append(item.getName())
	       print "\t" + item.getName()
	    nextIn = raw_input(endStr).strip().lower()
	    if nextIn in item_names:
	       if nextIn == room.getLock():
	           print "\nYou unlocked the room."
	           #remove key from items?
	           room.unlock()
	       else:
	           print "\nSorry, that item cannot be used to unlock the room."
	           print "You returned to the hallway."
	           return False
	    else:
	       print "\nSorry, you do not possess this item."
	       print "You returned to the hallway."
	       return False
	       
	else:
	    print "\nYou did not use an item."
	    print "You returned to the hallway."
	    return False
    if room == TechLab:
        if Goggles in mainChar.getItems() and SafetyRules in mainChar.getItems():
            pass
        else:
            print "Ms. G guardian stuff"
            #call function or code in guardian stuff
            return False
    if room == ChemLab:
        if Goggles in mainChar.getItems() and SafetyRules in mainChar.getItems() and Apron in mainChar.getItems():
            print "Ms. Pannapara gives quiz"
            #call function to give quiz
            #probably put in global variable about whether or not quiz has been taken
        else:
            pannapara(1)
            #call function or code in guardian stuff
            return False
    if not room.isLight():
	print "It is too dark to see anything. Use item? (y/n)"
	userIn = raw_input(endStr).strip().lower()
        if userIn == "y":
            print "\nThese are your items:"
            item_names = []
	    for item in mainChar.getItems():
	       item_names.append(item.getName())
	       print "\t" + item.getName()
	    nextIn = raw_input(endStr).strip().lower()
	    if nextIn in item_names:
	       if nextIn == "lightbulb":
	           print "\nYou replaced the lightbulb, so the lighting works now."
	           mainChar.removeItem(Lightbulb)
	           room.turnlightOn()
	       else:
	           print "\nSorry, that item cannot be used as a light source."
	           print "You returned to the hallway."
	           return False
	    else:
	        print "\nSorry, you do not possess this item."
	        print "You returned to the hallway."
	        return False
	else:
	    print "\nYou did not use an item."
	    print "You returned to the hallway."
	    return False
    return True

def roomStorage(room, furniture):
    print "\n" + furniture.getDescription()
    spkey = furniture.getKey(mainChar)
    if spkey != -1:
        print "\nSpecial Key obtained!"
        print "You now have %d special key(s)."%(len(mainChar.getKeys()))
    print "\nList of Items:"
    for item in furniture.getItems():
        print "\t" + item.getName() + ": " + item.getDescription()
    if len(furniture.getItems()) == 0:
        print "\tThe " + furniture.getName() + " is empty."
    print "Retrieve or deposit items? (Type \"r\" to retrieve, \"d\" to deposit, and \"n\" for neither."
    userIn = raw_input(endStr).strip().lower()
    if userIn == "r":
        print "Which item?"
        itemIn = raw_input(endStr).strip().lower()
        status = room.takeItem(itemIn, furniture, mainChar) #attempt to take item
        if status == "Done":
            print "You have successfully retrieved the item."
        elif status == -2: #if the object is not found within the storage
            print "There is no such object here."
    elif userIn == "d":
        print "\nThese are your items:\n"
	for item in mainChar.getItems():
	   print "\t" + item.getName() + ": " + item.getDescription()
        print "\nPlease choose an item to deposit."
        itemIn = raw_input(endStr).strip().lower()
        status = room.depositItem(itemIn, furniture, mainChar)
        if status == "Done":
            print "You have successfully deposited the item."
        elif status == -2:
            print "This " + furniture.getName() + " cannot hold any more items."
        elif status == -3:
            print "This is not an object you possess."
    else:
        print "You did not retrieve or deposit anything."

def battleMode(): #write battle mode stuff!
    pass

def pannapara(a):
    if a == 1:
	print "Ms. Pannapara appears! She says: \"You can’t enter the chem lab! You don’t have goggles, an apron, and/or the list of safety rules!\""
	print "Approach anyways? (y/n)"
	userIn = raw_input(endStr).strip().lower()
	if userIn == "y":
	    print "Ms. Pannapara hands you a graded micro-mole lab. You lose 1 HP."
	    health = mainChar.removeHealth(1)
	    print "You have " + str(health) + " hp left."
	elif userIn == "n":
	    print "You exit to the hallway."
    elif a == 2:
	print "Ms. Pannapara says: \"Students are forbidden to enter the prep room!\""
	print "Approach anyways? (y/n)"
	userIn = raw_input(endStr).strip().lower()
	if userIn == "y":
	    if preplab:
		print "Ms. Pannapara assigns you a Gas Law Marathon Lab. You lose 8 HP."
		health = mainChar.removeHealth(8)
		print "You have " + str(health) + " hp left."
	    else:
		print "Ms. Pannapara hands you a graded micro-mole lab. You lose 1 HP."
		health = mainChar.removeHealth(1)
	        print "You have " + str(health) + " hp left."
	elif userIn == "n":
	    pass
	preplab = True

if __name__ == "__main__": # this automatically runs the program when executed (opened in a shell)
	mainloop()
