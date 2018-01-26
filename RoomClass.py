
"""
Creates the rooms 
"""

class Room:
    
    def __init__(self, name, number, objects, key=False, lock=None):
        """
        :param name: room name
        :param number: room number
        :param objects: array of objects to look in
        :param key: bool if there's a key to escape the room
        :param lock: ?not decided yet
        """
        self.name = name
        self.number = number
        self.objects = objects
        self.key = key
        
    
    
    
"""
Example code
"""
chemLab = Room("Chemistry Lab", 140, ["One chemical", "Other chemical"], False, None)