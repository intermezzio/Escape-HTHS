import random
from UserClass import *

"""
Creates NPC's.
"""

class boss:
    def __init__(self, name, attack, health, drops):
        """
        :param name: boss name
        :param attack: method of attacking
        :param health: boss healthpoints
        :param health: healthpoints boss has
        :param drops: what the boss will drop after defeat
        """
        self.name = name
        self.attack = attack
        self.health = health
        self.drops = drops
    
    def getDamage(self):
        """
        Returns damage done by boss
        """
        if self.attack == "supercomputer":
            return random.randint(1,3)
        if self.attack == "detention":
            return random.randint(1,4)
    
    def attack(self):
        """
        Returns a tuple, the first value being the text to display to the screen, and the second value being the amount of damage taken.
        """
        if self.attack == "supercomputer":
            damage = self.getDamage()
            return ("Mr. B has used his supercomputer to lower your GPA! You have taken " + str(damage) + " points of damage!", damage)
        if self.attack == "detention":
            damage = self.getDamage()
            return ("Mr. Bals has called your parents and given you detention! You have taken " + str(damage) + " points of damage!", damage)
    
    def takeDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return self.health
        else:
            return self.drops
    
class angel:
    def __init__(self, name, action):
        """
        :param name: angel name
        :param action: action taken to aid user
        """
        self.name = name
        self.action = action
    
    def action(self, user):
        if self.action == "heal":
            userHealth = user.addHealth(1)
            return self.name + " has healed one point of damage! Your current health is " + str(userHealth) + "."
        elif self.action == "heal all":
            user.addHealth(10)
            return "Mrs. Finley has brought you back to full health! (10 hp)"