# -*- coding: utf-8 -*-
from NpcClass import *
from UserClass import *
from RoomClass import *
from StorageClass import *
from ItemClass import *
from Initialize import *
import re
import random
from time import sleep

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

roomList = {"120/130":Rm120130, "125":Rm125, "140":ChemLab, "155":Bio, "170":CSE, "180":Rm180, "185":Rm185, 
		"tech":TechLab, "main":MainOffice, "nurse":NurseOffice}

def mainloop():
	gameStart()
	
	while True:
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
				        elif checkSpecialAction(userAction):
				            pass
				        elif userAction == "leave":
				            print "\nYou left the room and returned to the hallway."
				            break
				        elif userAction in room.getStorageNames():
				            furniture = room.getStorage(userAction)
				            roomStorage(room, furniture) #possibly change take item function so room doesn't need to be parameter? see below
				        elif userAction == "battle":
				            print "\nYou have entered battle!"
				            victory = battleMode(room)
				            if victory:
				                pass
				            else:
				                break
				            
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
	items = [] # items the user starts with
	keys = [] # keys that user starts with (none)
	global mainChar
	mainChar = User(name, items, keys, 10)
	mainChar.addItem(Die)
	print "\nYou just failed your finals! You were supposed to be able to go home at 2:20, but now you are going to be held at HTHS for the rest of the summer. The only way to get out is to escape - but you have to figure out how. You are currently stuck in the CSE room, staring at unfinished Python code that you must complete. Until you do, there will be no food or water provided. It wouldn't be too bad, except that the Python assignment is absolutely impossible. You have no clue how to complete it."
	print "\nThe clock on the wall reads 2:30. Mr. Hanas is sitting at his table, fiddling with a six-sided die in his hand. You notice a 20-sided die sitting on the table next to you, left there by a Dungeons and Dragons player."
	print "\nIf you want to escape, you have no choice but to challenge Mr. Hanas now!"
	print "\nYou have entered battle!"
	victory = battleMode(CSE)
	if victory:
	    CSE.unlock()
	    print "You look around Room 170. There is a storage bin in the front of the room, near Mr. Hanas's desk. The impossible Python assignment is still on your computer."
	    while True:
	       userAction = getAction(CSE)
	       if checkGenericAction(userAction):
	           pass
	       elif checkSpecialAction(userAction):
	           pass
	       elif userAction == "leave":
	           print "\nYou left the room and returned to the hallway."
	           break
	       elif userAction in CSE.getStorageNames():
	           furniture = CSE.getStorage(userAction)
	           roomStorage(CSE, furniture)
	       else:
	           print "\nSorry, action not recognized."
	else:
	    print "will battle mode take care of what happens if you fail"
	return

def getAction(room=None, battle=False):
	actions = {}
	print "\nWhat do you do?"
	if battle:
	    actions["attack"] = "Attack with your weapon"
            actions["change weapon"] = "Open your backpack to see your weapons"
            actions["heal"] = "Open your backpack to see your healing items"
            actions["stats"] = "View your stats"
            actions["flee"] = "Run out of the room. Note that the boss' health will reset if you flee."
	elif room == None:
		actions["room"] = "Enter a room"
		actions["stats"] = "View your stats"
		actions["items"] = "View and use items"
		actions["escape"] = "Escape HTHS!"
	else: #rooms should probably also have a dictionary with actions, esp 120/130
		actions = room.getSpecialActions()
		for each in room.getStorages():
			actions[each.getName()] = each.getDescription()
		NPCs = room.getNPCs()
		if len(NPCs) > 0:
		    for NPC in NPCs:
		        if NPC.__class__.__name__ == "boss":
		            actions["battle"] = "Enter battle"
		actions["stats"] = "View your stats"
		actions["items"] = "View your items"
		actions["leave"] = "Leave room"
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
    if action == "stats":
	print "\nName: " + mainChar.name
	print "HP: " + str(mainChar.health) + "/10"
	return True
    elif action == "items":
        displayItems()
	print "\nYou have a total of %d items in your backpack and a carrying capacity of %d items."%(len(mainChar.getItems()), mainChar.space)
	print "You have a total of %d special key(s)."%(len(mainChar.keys))
	return True
    return False

def checkSpecialAction(action):
    if action == "program":
        print "\nNinety nine little bugs in the code,"
        print "Ninety nine little bugs,"
        print "Take one down, patch it around,"
        print "One hundred fifty two bugs in the code!"
        return True
    elif action == "skeleton":
        print "\nYou seem to hear a whisper. \"Find me amongst the ghosts…\""
        return True
    elif action == "prep":
        pannapara("prep")
        return True
    elif action == "sleep":
        for i in range(3):
            print "\nZzz...",
            sleep(2)
        print "\nYou took a short nap."
        return True
    else:
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
    print "\n" + furniture.getReturnText()
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
            print "\nThere is no such object here."
        elif status == -3:
            print "\nSorry, your backpack is full. You will have to deposit an item in order to take a new one."
    elif userIn == "d":
        displayItems()
        print "\nPlease choose an item to deposit."
        itemIn = raw_input(endStr).strip().lower()
        status = room.depositItem(itemIn, furniture, mainChar)
        if status == "Done":
            print "\nYou have successfully deposited the item."
        elif status == -1:
            print "\nLITTERING IS NOT ALLOWED!"
        elif status == -2:
            print "\nThis " + furniture.getName() + " cannot hold any more items."
        elif status == -3:
            print "\nThis is not an object you possess."
    else:
        print "\nYou did not retrieve or deposit anything."

def battleMode(room):
    boss = None
    for NPC in room.getNPCs(): #get the room's boss object and set it equal to variable boss
        if NPC.__class__.__name__ == "boss":
            boss = NPC
    print boss.getDescription()
    weapon = chooseWeapon()
    if weapon == None:
        return False
    print "\nReady yourself!"
    battle = True
    while battle:
        battle = battleOptions(room, weapon, boss)
    if boss.getHealth() == 0:
        #room.defeatBoss(boss)
        return True
    else:
        return False

def chooseWeapon():
    while True:
        print "\nThese are your weapons:\n" #print weapons
        itemsList = mainChar.getWeapons()
        for item in itemsList:
            print "\t" + item + ": " + itemsList[item]
        if len(itemsList) == 0: #if there are no weapons, print notification to user, then leave room.
            print "You have no weapons! You cannot fight. You must leave the room and exit to the hallway."
            return None
        else:
            print "\nChoose your weapon!"
        weaponIn = raw_input(endStr).strip().lower() #get weapon
        if weaponIn in itemsList: #set weapon equal to chosen weapon object, if user possesses
            for item in mainChar.getItems():
                if item.getName() == weaponIn:
                    return item
        else: #if user does not possess weapon, notify user and allow them to try again
            print "\nSorry, weapon not recognized. Choose another weapon."
            
def battleOptions(room, weapon, boss):
    while boss.getHealth() > 0 and mainChar.getHealth() > 0:
        action = getAction(room=room, battle=True)
        if action == "attack":
            name = weapon.getName()
            damage = weapon.attack()
            bossRet = boss.takeDamage(damage)
            if damage == 0:
                print "\nYou have rolled a 1! You inflicted no damage."
            else:
                print "\nYour " + name + " has inflicted " + str(damage) + " point(s) of damage!"
            if isinstance(bossRet, int):
                print boss.getName() + " has " + str(bossRet) + " hitpoint(s) left!"
                print boss.attackStr(mainChar)
            else:
                print "\nCongratulations! You have defeated " + boss.getName() + "."
                if boss.getName() == "Mr. Hanas":
                    print "\nThe door to this room is now unlocked."
                drops = boss.getDropsDict()
                print "\n " + boss.getName() + " has dropped the following item:\n" #print drops
                for drop in drops:
                    print "\t" + drop + ": " + drops[drop]
                
                print "\nWould you like to take the item? (y/n)"
                print "\nIf you don't take the item, it will be left on the floor of this room."
                userIn = raw_input(endStr).strip().lower() #get wanted drops
                if userIn == "":
                    userIn = blank()
                elif userIn != "n" and userIn != "y":
                    while userIn != "n" and userIn != "y":
                        bad()
                if userIn == "n":
                    boss.moveDrops(room)
                    print "\nThe item has dropped to the floor."
                    room.defeatBoss(boss)
                    return False
                elif userIn == "y":
                    ret = mainChar.addItem(boss.getDrops()[0])
                    if ret == -1:
                        boss.moveDrops(room)
                        print "\nSorry, your backpack is full! The item has been left on the floor."
                        room.defeatBoss(boss)
                        return False
                    else:
                        name = boss.getDrops()[0].getName()
                        boss.takeDrop(boss.getDrops()[0])
                        print "\nThe " + name + " has been added to your backpack."
                        room.defeatBoss(boss)
                    
                    return False
                                               
        elif action == "change weapon":
            weapon = chooseWeapon()        
        elif action == "heal":
            print "print this for now"
        elif action == "stats":
            checkGenericAction(action)
            return True
        elif action == "flee":
            if room == CSE:
                print "\nThe door is locked! You cannot flee."
            else:
                boss.resetHealth()
                print "\nYou have fled the room into the hallway."
                return False
        else:
            print "\nSorry, action not recognized."
            return True
    if mainChar.getHealth() == 0:    
        print "Oh no, you died!"
        return False
    else:
        return True

quizpass = False
preplab = False

def pannapara(a):
    if a == "quiz":
        if not quizpass:
            questions = {"Should you attempt to catch falling objects in the lab? (y/n)":"n",
                        "Should you eat or drink in the lab? (y/n)":"n",
                        "Should you leave an open flame unattended? (y/n)":"n",
                        "Should you perform any unauthorized experiments? (y/n)":"n"} #add more questions
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
	print "\nMs. Pannapara says: \"Students are forbidden from entering the prep room!\""
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

def blank():
    userIn = ""
    while len(userIn) == 0:
        print "Uh oh, the previous input was blank! Please enter an acceptable input."
        userIn = raw_input(endStr).strip().lower()
    
    return userIn

def bad():
    userIn = ""
    print "Sorry, that is not an acceptable input. Please try again."
    userIn = raw_input(endStr).strip().lower()
    return userIn

if __name__ == "__main__": # this automatically runs the program when executed (opened in a shell)
	mainloop()
