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
    
    def attack(self):
        if self.attack == "roll":
            return random.randint(1,7)
    
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
            return user.addHealth(1)
        elif self.action == "heal all":
            user.health = 10