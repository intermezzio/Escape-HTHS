import random
from UserClass import *
from StorageClass import *

"""
Creates NPC's (bosses).
"""

class boss:
    def __init__(self, name, description, attack, health, drops):
        """
        :param name: boss name
        :param description: boss description
        :param attack: method of attacking
        :param health: boss healthpoints
        :param health: healthpoints boss has
        :param drops: what the boss will drop after defeat
        """
        self.name = name
        self.description = description
        self.attack = attack
        self.health = health
        self.maxHealth = health
        self.drops = drops
    
    def getDamage(self):
        """
        Returns damage done by boss
        """
        if self.attack == "roll":
            return 1
        if self.attack == "supercomputer" or self.attack == "math":
            return random.randint(1,3)
        if self.attack == "detention":
            return random.randint(1,4)
    
    def attackStr(self, user):
        """
        :param user: user object
        Returns a String to display to the screen
        """
        if self.attack == "roll":
            roll = random.randint(1,6)
            if roll == 1:
                return "\nMr. Hanas has rolled a 1! He fails to attack you!"
            else:
                damage = self.getDamage()
                user.removeHealth(damage)
                return "\nMr. Hanas rolled above a 1! You have taken " + str(damage) + " point of damage!"
        if self.attack == "supercomputer":
            damage = self.getDamage()
            user.removeHealth(damage)
            return "\nMr. B has used his supercomputer to lower your GPA! You have taken " + str(damage) + " point(s) of damage!"
        if self.attack == "math":
            damage = self.getDamage()
            user.removeHealth(damage)
            return "\nThe mob of calculus problems swarms around you and confuses you! You have taken " + str(damage) + " points of damage!"
        if self.attack == "detention":
            damage = self.getDamage()
            user.removeHealth(damage)
            return "\nMr. Bals has called your parents and given you detention! You have taken " + str(damage) + " point(s) of damage!"
    
    def takeDamage(self, damage):
        """
        :param damage: damage done to boss
        subtracts damage from boss' health, checks to see whether or not boss dies, returns drops if death occurs
        """
        self.health = self.health - damage
        if self.health > 0:
            return self.health
        else:
            return self.drops
    
    def takeDrop(self, drop):
        """
        :param drop: drop to be removed
        removes drop from boss
        """
        self.drops.remove(drop)
    
    def moveDrops(self, room):
        """
        :param room: room that boss is in
        takes all dropps and puts them on floor of room
        """
        floor = room.getFloor()
        for drop in self.drops:
            floor.add(drop)
            self.takeDrop(drop)
    
    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description
    
    def getHealth(self):
        return self.health
    
    def getDrops(self):
        return self.drops
    
    def getDropsDict(self):
        """
	returns dictionary as shown:
	key    value
	name   description
	"""
	itemDict = dict()
	for item in self.drops:
	   itemDict[item.getName()] = item.getDescription()
	     
	return itemDict
    
    def resetHealth(self):
        self.health = self.maxHealth
