from NpcClass import *
from UserClass import *
from RoomClass import *
from StorageClass import *
from ItemClass import *
from Initialize import *

def battleMode(room, boss): #write battle mode stuff!
    print "\nThese are your weapons:\n"
    itemsList = mainChar.getWeapons()
    for item in itemsList:
        print "\t" + item + ": " + itemsList[item]
    if len(itemsList == 0):
        print "You have no weapons! You cannot fight."
        return None #endBattle
    else:
        print "\nChoose your weapon!"
    weaponIn = raw_input(endStr).strip().lower()
    weapon = None
    if weaponIn in itemsList():
        for item in mainChar.getItems():
            if item.getName() == weaponIn:
                weapon = item
        if weapon.getDamage() > 0:
            print "Ready yourself!"
            battleOptions()
            
def battleOptions():
    while (hp>0):
        #put in getActions
        print "What do you do?"
        actions = {}
        actions["attack"] = "Attack with your weapon"
        actions["change weapon"] = "Open your backpack to see your weapons"
        actions["use healing item"] = "Open your backpack to see your healing items"
        actions["stats"] = "View your player stats"
        actions["flee"] = "Run out of the room. Note that the boss' health will reset if you flee."
        
        returned = input
        if/else statements through actions
        loop until change weapon OR a hp reaches 0
        go back to battle mode
        when boss hp = 0, code something