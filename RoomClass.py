from StorageClass import *
from UserClass import *
from ItemClass import *

"""
Creates the rooms 
"""

class Room:
    def __init__(self, name, tag, furniture, description, NPCs=[], light=True, lock="none"):
        """
        :param name: room name
        :param tag: room tag (number if exists, keyword if otherwise)
        :param furniture: list of furniture to look in
        :param description: string description of the room
        :param NPCs: list of NPCs in the room
        :param light: bool if the lights are on
        :param lock: if locked, param should match name of key to unlock
        """
        self.name = name
        self.tag = tag
        self.furniture = furniture
        self.NPCs = NPCs
        self.light = light
        self.description = description
        self.lock = lock
        
    def takeItem(self, item, storage, user):
        """
        Look at Furniture from a Room
        :param item: the item the user wants to take
        :param storage: the storage to look at
        :param user: the user looking at the furniture
        Errors
            -1: Storage does not exist
            -2: Object does not exist in the furniture
            -3: User has no excess storage
        """
        items = storage.getItems()
        obj = None
        for thing in items:
            if item == thing.getName():
                obj = thing       
        
        if storage in self.furniture:
            if len(user.getItems()) < user.getSpace():
                if obj in storage.getItems():
                    storage.remove(obj)
                    user.addItem(obj)
                else:
                    return -2 #object not found
            else:
                return -3 #user has no excess storage
        else:
            return -1
        return "Done"
    
    def depositItem(self, item, storage, user=None):
        """
        Look at Furniture from a Room
        :param item: the item the user wants to deposit
        :param storage: the storage to look at
        :param user: the user looking at the furniture
        Errors
            -1: User is trying to litter
            -2: Storage is out of space
            -3: User does not possess item
        """
        if storage == self.getFloor() and user != None:
            return -1
        if user != None:
            items = user.getItems()
            obj = None
            for thing in items:
                if item == thing.getName():
                    obj = thing       
        
            if storage in self.furniture:
                if obj in user.getItems():
                    if len(storage.getItems()) < storage.getSpace():
                        storage.add(obj)
                        user.removeItem(obj)
                    else:
                        return -2 #storage is out of space
                else:
                    return -3 #user does not possess item
            else:
                return -1
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
    
    def getStorageNames(self):
        names = []
        for each in self.furniture:
            names.append(each.getName())
        return names
    
    def getName(self):
        return self.name
    
    def getTag(self):
        return self.tag
    
    def getDescription(self):
        return self.description
    
    def getNPCs(self):
        return self.NPCs
    
    def isLight(self):
        return self.light
    
    def getLock(self):
        return self.lock
    
    def unlock(self):
        self.lock = "none"
    
    def getFloor(self):
        for furniture in self.furniture:
            if "floor" in furniture.getName():
                return furniture
    
"""
Example code
"""
#chemLab = Room("Chemistry Lab", 140, [])

#chemDrawer = Storage("Drawer", 4, ["One chemical", "Other chemical"], "A dark drawer containing mysterious substances")

#chemLab.addStorage(chemDrawer)