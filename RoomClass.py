from StorageClass import *
from UserClass import *
from ItemClass import *

"""
Creates the rooms 
"""

class Room:
    
    def __init__(self, name, number, furniture, description, NPCs=None, key=False, light=True, lock=None):
        """
        :param name: room name
        :param number: room number
        :param furniture: list of furniture to look in
        :param description: string description of the room
        :param NPCs: list of NPCs in the room
        :param key: bool if there's a key to escape the room
        :param light: bool if the lights are on
        :param lock: ?not decided yet
        """
        self.name = name
        self.number = number
        self.furniture = furniture
        self.NPCs = NPCs
        self.key = key
        self.light = light
        self.description = description
        
    def takeItem(self, item, storage, user):
        """
        Look at Furniture from a Room
        :param furniture: the furniture to look at
        :param item: the item the user wants to take
        :param user: the user looking at the furniture
        Errors
            -1: Furniture does not exist
            -2: Object does not exist in the furniture
            -3: User has no excess storage
        """
        if storage in self.furniture:
            if user.space > 0:
                if item in storage:
                    self.furniture.remove(item)
                    user.items.append(item)
                else:
                    return -2
            else:
                return -3
        else:
            return -1 # Object Not Found 
        return "Done"
        
    def getStorage(self, storageName):
        """
        Returns Furniture in a Room by Name
        :param storageName: the name of the piece of furniture
        Errors
            +1: Objects are hidden
            -1: Storage does not exist
        """
        if not self.light:
            return 1
        for storage in self.furniture:
            if storage.getName() == storageName:
                return storage
        return -1
        
    def addStorage(self, storage):
        self.furniture += [storage]
        return 0
    #def addroom(self, room)
    
    def turnlightOn(self):
        self.light = True
        return 0
    
    def turnlightOff(self):
        self.light = False
        return 0
        
    def getStorages(self):
        if not self.light:
            return []
        return self.furniture
        
    def getName(self):
        return self.name
    
    def getNumber(self):
        return self.number
        
    def isLight(self):
        return self.light
"""
Example code
"""
#chemLab = Room("Chemistry Lab", 140, [])

#chemDrawer = Storage("Drawer", 4, ["One chemical", "Other chemical"], "A dark drawer containing mysterious substances")

#chemLab.addStorage(chemDrawer)