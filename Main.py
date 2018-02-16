from NpcClass import *
from UserClass import *
from RoomClass import *
from ItemClass import *
from StorageClass import *

"""
Starts and Ends Game
"""

def createObjects():
    furniture = [StorageClass.Storage("front cabinet",2, None, "cabinet in the front of the room"),
                StorageClass.Storage("back cabinet",2, None, "cabinet in the back of the room"),
                StorageClass.Storage("front desk",2, None, "desk in the front of the room"),
                StorageClass.Storage("phone charging station",1,None, "phone charging station")]
    Rm170 = RoomClass.Room("CSE Classroom", 170, furniture, True) 
    Hanas = NpcClass.boss("Mr. Hanas", "roll", 1, None)
    