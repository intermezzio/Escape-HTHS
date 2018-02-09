from StorageClass import *
"""
Creates the rooms 
"""

class Room:
    
    def __init__(self, name, number, furniture, key=False, light=True, lock=None):
        """
        :param name: room name
        :param number: room number
        :param objects: array of furniture to look in
        :param key: bool if there's a key to escape the room
        :param lock: ?not decided yet
        """
        self.name = name
        self.number = number
        self.furniture = furniture
        self.key = key
        self.light = True
        
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
            #if user.space > 0:
                if item in storage:
                    self.furniture.remove(item)
                    user.objects.append(item)
                else:
                    return -2
            #else:
                return -3
        else:
            return -1 # Object Not Found 
        return "Done"
        
    #def addroom(self, room)
    #def turnlightOn
    
"""
Example code
"""
chemLab = Room("Chemistry Lab", 140, ["One chemical", "Other chemical"])