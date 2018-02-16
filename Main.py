from NpcClass import *
from UserClass import *
from RoomClass import *
from ItemClass import *

"""
Starts and Ends Game
"""

def createObjects():
    furniture = ["front cabinet", "back cabinet", "front desk", "phone charging station"]
    Rm170 = RoomClass.Room("CSE Classroom", 170, furniture, True) 
    Hanas = NpcClass.boss("Mr. Hanas", "roll", 1, None)
    