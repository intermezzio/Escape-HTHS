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
import sys

"""
Starts and Ends Game
"""

mainChar = None #global variable to hold user object
endStr = "\n\t(+)  " #variable used to format user input query

roomList = {"125":Rm125, "140":ChemLab, "155":Bio, "170":CSE, "180":Rm180, "185":Rm185, 
		"tech":TechLab, "main":MainOffice, "nurse":NurseOffice} #list of rooms, displayed when asking user to choose room

def mainloop(): #function with loop that runs until program stops
    gameStart() #beginning scene
	
    while True: #loop runs always
        nextAction = getAction()
        if checkGenericAction(nextAction): #check for generic action (stats, items)
            pass
        elif nextAction == "escape": #if action is escape
            if len(mainChar.keys) == 4: #does the user have all four keys?
                break #if so, break loop. Ends program.
            else:
                print "\nYou don't have all the special keys." #if user doesn't have all of the keys, notify user
        elif nextAction == "room": #if action is room
            print "\nList of Rooms:"
            for room in roomList: #print every room on a new line
                print "\"" + room + "\"" + ": " + roomList[room].name
            userIn = raw_input(endStr).strip().lower() #take in user's chosen room
            if userIn in roomList: #check to see if inputted room is in room list
                room = roomList[userIn] #get the room name
                canEnter = checkRoom(room) #check to see if the room is locked, returns Boolean
                if canEnter: #if room is unlocked
                    print "\n" + room.getDescription()
                    while True:
                        userAction = getAction(room=room) #get room actions
                        if checkGenericAction(userAction): #pass if generic action
                            pass
                        elif checkSpecialAction(userAction): #pass if special action
                            pass
                        elif userAction == "leave": #if action is leave
                            print "\nYou left the room and returned to the hallway."
                            break #break while loop, actions provided will no longer be associated with room
                        elif userAction in room.getStorageNames(): #if user chooses to open storage
                            furniture = room.getStorage(userAction)
                            roomStorage(room, furniture) #run program for interacting with furniture
                        elif userAction == "battle": #if user chooses to battle
                            print "\nYou have entered battle!"
                            victory = battleMode(room) #returns Boolean based on whether or not user wins battle
                            if victory: #if user wins
                                pass
                            else:
                                break #means flee, or leave room.
                        else:
                            print "\nSorry, action not recognized." #corresponds to action if in room
            else:
                print "\nSorry, room not recognized."
        else:
            print "\nSorry, action not recognized." #corresponds to first action, if not in room
            
    print "\nCongrats! You escaped HTHS!" #prints when loop is broken, marks end of program

def gameStart(): #game introduction
    print "Welcome to Escape HTHS!" # introduction text
    name = raw_input("What is your name?" + endStr) # take in name of the user
    items = [] # items the user starts with
    keys = [] # keys that user starts with (none)
    global mainChar
    mainChar = User(name, items, keys, 10) #make user class
    mainChar.addItem(Die) #user starts with a die
    print "\nYou just failed your finals! You were supposed to be able to go home at 2:20, but now you are going to be held at HTHS for the rest of the summer. The only way to get out is to escape - but you have to figure out how. You are currently stuck in the CSE room, staring at unfinished Python code that you must complete. Until you do, there will be no food or water provided. It wouldn't be too bad, except that the Python assignment is absolutely impossible. You have no clue how to complete it."
    print "\nThe clock on the wall reads 2:30. Mr. Hanas is sitting at his table, fiddling with a six-sided die in his hand. You notice a 20-sided die sitting on the table next to you, left there by a Dungeons and Dragons player."
    print "\nIf you want to escape, you have no choice but to challenge Mr. Hanas now! He has 5 HP!"
    print "\nYou have entered battle!"
    battleMode(CSE) #enter battle in CSE room
    print "You look around Room 170. There is a storage bin in the front of the room, near Mr. Hanas's desk. The impossible Python assignment is still on your computer."
    while True:
        userAction = getAction(CSE) #get user's action
        if checkGenericAction(userAction): #pass if generic action
            pass
        elif checkSpecialAction(userAction): #pass if special action
            pass
        elif userAction == "leave": #if action is leave, leave
            print "\nYou left the room and returned to the hallway."
            break
        elif userAction in CSE.getStorageNames(): #if user chooses to interact with furniture
            furniture = CSE.getStorage(userAction) #get furniture object
            roomStorage(CSE, furniture) #run interacting with storage function
        else:
            print "\nSorry, action not recognized."

def getAction(room=None, battle=False): #display possible actions and receive user input
    actions = {} #dictionary to hold displayed actions
    print "\nWhat do you do?"
    if battle: #if in battle mode
        actions["attack"] = "Attack with your weapon"
        actions["change weapon"] = "Open your backpack to see your weapons"
        actions["heal"] = "Open your backpack to see your healing items"
        actions["stats"] = "View your stats"
        actions["flee"] = "Run out of the room. Note that the boss' health will reset if you flee."
    elif room == None: #if user not in a room
        actions["room"] = "Enter a room"
        actions["stats"] = "View your stats"
        actions["items"] = "View your items and special keys"
        actions["escape"] = "Escape HTHS!"
    else: #if user in a room and not in battle
	hasBoss = False #is there a boss in the room?
	if room.getNPCs() != None: #if there are no NPCs in the room
	    hasBoss = True
        if hasBoss: #if there is a boss, only other option is "Enter Battle"
		    actions["battle"] = "Enter battle"
	else:
	    actions = room.getSpecialActions() #get extra actions of room
	    for each in room.getStorages(): #get storage items of room
	        actions[each.getName()] = each.getDescription()
	        
        actions["stats"] = "View your stats"
        actions["items"] = "View your items and special keys"
        actions["leave"] = "Leave room"
    for each in actions: #print each action in a list
	print "\"" + each + "\"" + ": " + actions[each]
    userIn = raw_input(endStr).strip().lower() #get user action
    if userIn in actions:
	return userIn
    else:
	return "nope"

def displayItems(): #displays items as list of names, descriptions, and quantities
    print "\nThese are your items:\n"
    itemsList = mainChar.getItemsDict()
    for item in itemsList.keys():
        print "\t" + item + ": " + itemsList[item][0] + " (x" + str(itemsList[item][1]) + ")"

def checkGenericAction(action): #check for "stats" or "items" action
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

def checkSpecialAction(action): #check for room-specific actions
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
        mainChar.addHealth(10)
        print "\nYou took a short nap. Full health has been restored."
        return True
    else:
        return False

def checkRoom(room): #check to see if a room is accessible
    if not room.getLock() == "none": #check to see if a room is locked, prompt user to unlock if possible
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
    if room == TechLab: #check to see if user has prerequisites to enter tech lab
        if Goggles in mainChar.getItems() and SafetyRules in mainChar.getItems():
            pass
        else:
            grunthaner()
            return False
    if room == ChemLab: #check to see if user has prerequisites to enter chem lab
        if Goggles in mainChar.getItems() and SafetyRules in mainChar.getItems() and Apron in mainChar.getItems():
            pannapara("quiz")
            if not quizpass:
                print "You returned to the hallway."
                return False
        else:
            pannapara("missing")
            return False
    if not room.isLight(): #check to see if lighting is adequate
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

def roomStorage(room, furniture): #print what's inside storage
    print "\n" + furniture.getReturnText()
    spkey = furniture.getKey(mainChar)
    if spkey != -1: #check for special key. If there, notify user
        print "\nSpecial Key obtained!"
        print "You now have %d special key(s)."%(len(mainChar.getKeys()))
    print "\nList of Items:" #print list of items in furniture
    itemsList = furniture.getItemsDict()
    for item in itemsList.keys():
        print "\t" + item + ": " + itemsList[item][0] + " (x" + str(itemsList[item][1]) + ")"
    if len(furniture.getItems()) == 0: #if furniture is empty, state so. Only allow user to deposit items
        print "\tThe " + furniture.getName() + " is empty."
        print "\nDeposit an item? (y/n)"
        userIn = raw_input(endStr).strip().lower()
        while userIn != "y" and userIn != "n":
            userIn = bad()
        if userIn == "y":
            userIn = "d"
    else: #prompt user on whether or not they wish to deposite or receive, or neither
        print "\nRetrieve or deposit items? (Type \"r\" to retrieve, \"d\" to deposit, and \"n\" for neither."
        userIn = raw_input(endStr).strip().lower()
        while userIn != "r" and userIn != "d" and userIn != "n":
            userIn = bad()
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

def battleMode(room): #battle loops
    boss = room.getNPCs() #get the room's boss object and set it equal to variable boss
    print boss.getDescription() #print boss description
    weapon = chooseWeapon() #allow user to choose weapon
    if weapon == None:
        return False #if the user has no weapons, user must leave (return false)
    print "\nReady yourself!"
    battle = True
    while battle:
        battle = battleOptions(room, weapon, boss) #loop runs as long as battle has not ended
    if room.getNPCs() == None: #if boss was defeated, return true, meaning boss defeated
        return True
    else:
        return False #return False, meaning "flee" was chosen

def chooseWeapon(): #allow user to choose weapon
    while True: #loops until weapon is chosen
        print "\nThese are your weapons:\n" #print weapons
        itemsList = mainChar.getWeapons() #getUser weapons
        for item in itemsList:
            print "\t" + item + ": " + itemsList[item] #print weapons
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
    while boss.getHealth() > 0 and mainChar.getHealth() > 0: #while both boss and user are alive
        action = getAction(room=room, battle=True) #get battle action
        if action == "attack": #if user chooses to attack
            name = weapon.getName() #get weapon name
            damage = weapon.attack() #get weapon damage
            bossRet = boss.takeDamage(damage) #inflict damage on boss, returns drops if dead, hp left if alive
            if damage == 0: #if damage is zero, dice rolled zero
                print "\nYou have rolled a 1! You inflicted no damage."
            else: #display how much damage inflicted
                print "\nYour " + name + " has inflicted " + str(damage) + " point(s) of damage!"
            if isinstance(bossRet, int): #if bossRet is an integer, display number of hp left, have boss attack
                print boss.getName() + " has " + str(bossRet) + " hitpoint(s) left!"
                print boss.attackStr(mainChar)
                return True
            else: #if boss is defeated, congrats
                print "\nCongratulations! You have defeated " + boss.getName() + "."
                if boss.getName() == "Mr. Hanas":
                    print "\nThe door to this room is now unlocked."
                drops = boss.getDropsDict() #get dictionary of drop to display
                print "\n " + boss.getName() + " has dropped the following item:\n" #print drops
                for drop in drops:
                    print "\t" + drop + ": " + drops[drop]
                print "\nWould you like to take the item? (y/n)"
                print "\nIf you don't take the item, it will be left on the floor of this room."
                userIn = raw_input(endStr).strip().lower() #get wanted drop
                if userIn == "": #if blank, ask for re-enter until not blank
                    userIn = blank()
                elif userIn != "n" and userIn != "y": #if not n or y, ask for re-enter until it is n or y
                    while userIn != "n" and userIn != "y":
                        userIn = bad()
                if userIn == "n": #if n, drop item to floor
                    boss.moveDrops(room)
                    print "\nThe item has dropped to the floor."
                elif userIn == "y": #if y, try to take item
                    ret = mainChar.addItem(boss.getDrops()[0])
                    if ret == -1: #if return is -1, backpack is full, notify user
                        boss.moveDrops(room)
                        print "\nSorry, your backpack is full! The item has been left on the floor."
                    else:
                        name = boss.getDrops()[0].getName()
                        boss.takeDrop(boss.getDrops()[0])
                        print "\nThe " + name + " has been added to your backpack."
                
                room.defeatBoss()    
                return False #to battleOption loop
                                        
        elif action == "change weapon":
            weapon = chooseWeapon()        
        elif action == "heal":
            print "\nThese are your bandaids:\n" #print bandaids
            itemsList = mainChar.getHealingItems()
            for item in itemsList:
                print "\t" + item + ": " + itemsList[item]
            if len(itemsList) == 0: #if there are no bandaids, print notification to user, then get actions again
                print "You have no bandaids! You cannot heal yourself."
            else:
                print "\nWould you like to use a bandaid? (y/n)"
                userIn = raw_input(endStr).strip().lower()
                if userIn == "y":
                    print "You have successfully used the bandaid."
                    print "You have " + str(mainChar.useBandaid()) + " health points."
                elif userIn == "n":
                    pass
                else:
                    while userIn != "y" and userIn != "n":
                        userIn = bad()

        elif action == "stats": #display stats, return True to stay in loop
            checkGenericAction(action)
            return True
        elif action == "flee":
            if room == CSE: #prevent fleeing from first room
                print "\nThe door is locked! You cannot flee."
            else: #reset boss health and return false to indicate no longer in battle
                boss.resetHealth()
                print "\nYou have fled the room into the hallway."
                return False
        else: #if action not recognized, ask for action again
            print "\nSorry, action not recognized."
            return True
    if mainChar.getHealth() <= 0: #if user health is zero or falls below zero, end program   
        print "Oh no, you died!"
        userDeath()
    else:
        return True

quizpass = False
preplab = False

def pannapara(a): #takes in string to determine what action to take next
    if a == "quiz": #if string is "quiz", give user quiz on safety rules
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
    elif a == "missing": #if string is "missing", do not allow user into the safety lab
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
    elif a == "prep": #if string is "prep", do not allow students into the prep lab. More serious offense than safety lab.
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

def grunthaner(): #is called when Mr. G has to defend the tech lab.
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

def blank(): #when the user inputs blank, this is called until they don't input blank.
    userIn = ""
    while len(userIn) == 0:
        print "Uh oh, the previous input was blank! Please enter an acceptable input."
        userIn = raw_input(endStr).strip().lower()
    
    return userIn

def bad(): #when the user makes a bad input, this is called until they make a good input.
    userIn = ""
    print "Sorry, that is not an acceptable input. Please try again."
    userIn = raw_input(endStr).strip().lower()
    return userIn

def userDeath(): #If the user dies, this is called and the program ends.
    print "\nGame over."
    sys.exit()

if __name__ == "__main__": # this automatically runs the program when executed (opened in a shell)
	mainloop()
