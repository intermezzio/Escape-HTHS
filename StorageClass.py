
"""
Storage ex. Chest, Drawer

"""

class Storage:
    def __init__(self, name, space, items, description, key=None):
        self.name = name
        self.space = space
        self.items = items
        self.description = description
    
    def getName(self):
        return self.name
        
    def getDescription(self):
        return self.description
    
    def getKey(self, user):
        if self.key == None:
            return -1
        else:
            return user.addKey(self.key)
"""
Example code
"""
chemDrawer = Storage("Drawer", 4, ["One chemical", "Other chemical"], "<description>")