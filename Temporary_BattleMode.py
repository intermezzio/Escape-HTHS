from NpcClass import *
from UserClass import *
from RoomClass import *
from StorageClass import *
from ItemClass import *
from Initialize import *

def battleMode(room):
    boss = None
    for NPC in room.getNPCs(): #get the room's boss object and set it equal to variable boss
        if NPC.__class__.__name__ == "boss":
            boss = NPC
    print "\nThese are your weapons:\n" #print weapons
    itemsList = mainChar.getWeapons()
    for item in itemsList:
        print "\t" + item + ": " + itemsList[item]
    if len(itemsList == 0): #if there are no weapons, print notification to user, then leave room.
        print "You have no weapons! You cannot fight. You must leave the room."
        return False
    else:
        print "\nChoose your weapon!"
    weaponIn = raw_input(endStr).strip().lower() #get weapon
    weapon = None
    if weaponIn in itemsList(): #set weapon equal to chosen weapon object, if user possesses
        for item in mainChar.getItems():
            if item.getName() == weaponIn:
                weapon = item
        print "Ready yourself!"
        battle = True
        while battle:
            battle = battleOptions(room, weapon, boss)
        if boss.getHealth() == 0:
            return True
        else:
            return False
    else: #if user does not possess weapon, notify user and allow them to try again
        print "Sorry, weapon not recognized. Choose another weapon."
        battleMode(room)
            
def battleOptions(room, weapon, boss):
    while mainChar.getHealth() > 0:
        action = getAction(room, True)
        if action == "attack":
            name = weapon.getName()
            damage = weapon.attack()
            bossRet = boss.takeDamage(damage)
            print "Your " + name + "has inflicted " + str(damage) + " points of damage!"
            if isinstance(bossRet, int):
                print "\n" + boss.getName() + "has " + str(bossRet) + " hitpoints left!"
                print boss.attack(mainChar)
            else:
                print "Congratulations! You have defeated " + boss.getName() + "."
                drops = boss.getDropsDict()
                print "\n " + boss.getName() + "has dropped the following items:\n" #print drops
                for drop in drops:
                    print "\t" + drop + ": " + drops[drop]
                
                print "\nWhich items would you like to take? Separate item names with a comma, type \"none\" if you do not want any of the items."
                print "\nItems that are not taken will be left on the floor of this room."
                userIn = raw_input(endStr).strip().lower() #get wanted drops
                if userIn == "":
                    userIn = blank()
                if userIn == "none":
                    for item in boss.getDrops():
                        room.depositItem(item, room.getStorage("floor"))
                else:
                    wantedDrops = []
                    while len(userIn) > 0:
                        if userIn[0] == "," or userIn[0] == " ":
                            userIn == userIn[1:]
                        else:
                            comma = userIn.find()
                            if comma == -1:
                                wantedDrops.append(userIn)
                                break
                            else:
                                wantedDrops.append(userIn[0:comma])
                                userIn = userIn[comma+1:]
                    for drop in wantedDrops:
                        dropObj = None
                        for item in drops:
                            if drop == item.getName():
                                dropObj = item
                            
                        ret = mainChar.addItem(dropObj)
                        if ret == -1:
                            boss.moveDrops(boss.getDrops())
                            print "Sorry, your backpack is full! Remaining drops have been left on the floor."
                            
                        else:
                            boss.moveDrops(drop)
                            print dropObj.getName() + " has been added to your backpack."
                    
                    return True
                                               
                
        elif action == "use healing item":
            print "print this for now"
        elif action == "stats":
            checkGenericAction(action)
            return True
        elif action == "flee":
            print "You have fled the room."
            return False