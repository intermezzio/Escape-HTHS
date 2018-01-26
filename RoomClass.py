
"""
Creates the rooms 
"""

class Room:
    
    def __init__(self, name, number, objs, key=False, light=True, lock=None):
        """
        :param name: room name
        :param number: room number
        :param objects: array of objects to look in
        :param key: bool if there's a key to escape the room
        :param lock: ?not decided yet
        """
        self.name = name
        self.number = number
        self.objs = objs
        self.key = key
        self.light = True
        
    def pickObj(self, obj, user):
        if obj in self.objs:
            if user.space > 0:
                self.objs.remove(obj)
                user.objects.append(obj)
            else:
                return "No space available"
        else:
            return "Object not found"
        return "Done"
                
    
    
"""
Example code
"""
chemLab = Room("Chemistry Lab", 140, ["One chemical", "Other chemical"])