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
import random

"""
Starts and Ends Game
"""
'''
To Do:
    battle mode function (displays battle mode option when applicable but have yet to make a function that starts the actual battle)
    implement battle mode function in main code
    add key parameter to boss NPCs
    figure out display text for rooms after bosses are defeated
    alternative description/blurbs for storage
    extra actions for each room
    120/130 divider stuff
    fix storage description issue (nurse's office)
'''
mainChar = None
endStr = "\n\t(+)  "

roomList = {"120":Rm120, "125":Rm125, "130":Rm130, "145":ChemLab, "155":Bio, "170":CSE, "185":Rm185, 
		"tech":TechLab, "main":MainOffice, "nurse":NurseOffice}

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
				            print "\nYou left the room and returned to the hallway."
				            break
				        elif userAction in room.getStorageNames():
				            furniture = room.getStorage(userAction)
				            roomStorage(room, furniture) #possibly change take item function so room doesn't need to be parameter? see below
				        elif userAction == "battle":
				            print "\nYou entered a battle!"
				            battleMode()
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
	    #add actions
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
		    for NPC in NPCs:
		        if NPC.__class__.__name__ == "boss":
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

def displayItems():
    print "\nThese are your items:\n"
    itemsList = mainChar.getItemsDict()
    for item in itemsList.keys():
        print "\t" + item + ": " + itemsList[item][0] + " (x" + str(itemsList[item][1]) + ")"

def checkGenericAction(action):
    if action == "help":
	print "this is a placeholder" #print helpStr  <-- This will be defined in another python file/function
	return True
    elif action == "stats":
	print "\nName: " + mainChar.name
	print "HP: " + str(mainChar.health) + "/10"
	return True
    elif action == "items":
        displayItems()
	print "\nYou have a total of %d items in your inventory and a carrying capacity of %d items."%(len(mainChar.getItems()), mainChar.space)
	print "You have a total of %d special key(s)."%(len(mainChar.keys))
	return True
    return False

def checkRoom(room):
    if not room.getLock() == "none":
        print "\nThe room is locked. Use item? (y/n)"
        userIn = raw_input(endStr).strip().lower()
        if userIn == "y":
            displayItems()
            print "\nChoose an item to use."
	    nextIn = raw_input(endStr).strip().lower()
	    if nextIn in mainChar.getItemNames():
	       if nextIn == room.getLock():
	           print "\nYou unlocked the room."
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
            grunthaner()
            return False
    if room == ChemLab:
        if Goggles in mainChar.getItems() and SafetyRules in mainChar.getItems() and Apron in mainChar.getItems():
            pannapara("quiz")
            if not quizpass:
                print "You returned to the hallway."
                return False
        else:
            pannapara("missing")
            return False
    if not room.isLight():
	print "\nIt is too dark to see anything. Use item? (y/n)"
	userIn = raw_input(endStr).strip().lower()
        if userIn == "y":
            displayItems()
            print "\nChoose an item to use."
	    nextIn = raw_input(endStr).strip().lower()
	    if nextIn in mainChar.getItemNames():
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
    itemsList = furniture.getItemsDict()
    for item in itemsList.keys():
        print "\t" + item + ": " + itemsList[item][0] + " (x" + str(itemsList[item][1]) + ")"
    if len(furniture.getItems()) == 0:
        print "\tThe " + furniture.getName() + " is empty."
    print "\nRetrieve or deposit items? (Type \"r\" to retrieve, \"d\" to deposit, and \"n\" for neither."
    userIn = raw_input(endStr).strip().lower()
    if userIn == "r":
        print "\nWhich item?"
        itemIn = raw_input(endStr).strip().lower()
        status = room.takeItem(itemIn, furniture, mainChar) #attempt to take item
        if status == "Done":
            print "\nYou have successfully retrieved the item."
        elif status == -2: #if the object is not found within the storage
            print "There is no such object here."
    elif userIn == "d":
        displayItems()
        print "\nPlease choose an item to deposit."
        itemIn = raw_input(endStr).strip().lower()
        status = room.depositItem(itemIn, furniture, mainChar)
        if status == "Done":
            print "\nYou have successfully deposited the item."
        elif status == -2:
            print "This " + furniture.getName() + " cannot hold any more items."
        elif status == -3:
            print "This is not an object you possess."
    else:
        print "\nYou did not retrieve or deposit anything."

def battleMode(): #write battle mode stuff!
    pass

quizpass = False
preplab = False

def pannapara(a):
    if a == "quiz":
        if not quizpass:
            questions = {"Should you attempt to catch falling objects in the lab? (y/n)":"n",
                        "more questions":"answers"} #add more questions
            print "\nMs. Pannapara appears and says: \"Before you enter the lab, you need to know all the safety rules!\""
            ask = random.choice(questions.keys())
            print ask
            userIn = raw_input(endStr).strip().lower()
            if userIn == questions[ask]:
                print "\nCorrect!"
                global quizpass
                quizpass = True
            else:
                print "\nSorry, incorrect."
    elif a == "missing":
	print "\nMs. Pannapara appears! She says: \"You can’t enter the chem lab! You don’t have goggles, an apron, and/or the list of safety rules!\""
	print "Approach anyways? (y/n)"
	userIn = raw_input(endStr).strip().lower()
	if userIn == "y":
	    print "\nMs. Pannapara hands you a graded micro-mole lab. You lose 1 HP."
	    health = mainChar.removeHealth(1)
	    print "You have " + str(health) + "/10 HP left."
	    print "You are forced out to the hallway."
	else:
	    print "\nYou exit to the hallway."
    elif a == "prep":
	print "\nMs. Pannapara says: \"Students are forbidden to enter the prep room!\""
	print "Approach anyways? (y/n)"
	userIn = raw_input(endStr).strip().lower()
	if userIn == "y":
	    if preplab:
		print "Ms. Pannapara assigns you a Gas Law Marathon Lab. You lose 8 HP."
		health = mainChar.removeHealth(8)
		print "You have " + str(health) + "/10 HP left."
	    else:
		print "Ms. Pannapara hands you a graded micro-mole lab. You lose 1 HP."
		health = mainChar.removeHealth(1)
	        print "You have " + str(health) + "/10 HP left."
	elif userIn == "n":
	    pass
	global preplab
	preplab = True

def grunthaner():
    print "\nMs. G shows up and says: Safety first! \"Don’t come forward even one more step unless you have all the required items to enter the tech lab!\""
    print "Approach anyways? (y/n)"
    userIn = raw_input(endStr).strip().lower()
    if userIn == "y":
	print "Ms. G hands you a technical drawing assignment. You lose 1 HP."
	health = mainChar.removeHealth(1)
	print "You have " + str(health) + "/10 HP left."
	print "You are forced out to the hallway."
    else:
	print "\nYou exit to the hallway."

if __name__ == "__main__": # this automatically runs the program when executed (opened in a shell)
	mainloop()
