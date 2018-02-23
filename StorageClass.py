
"""
Storage ex. Chest, Drawer

"""

class Storage:
    def __init__(self, name, space, items, description, key="none"):
        self.name = name
        self.space = space
        self.items = items
        self.description = description
        self.key = key
    
    def getName(self):
        return self.name
    
    def getItems(self):
        return self.items
    
    def getDescription(self):
        return self.description
    
    def getKey(self, user):
        if self.key == "none":
            return -1
        else:
            num = user.addKey(self.key)
            self.key = "none"
            return num
    
    def remove(self, item):
        self.items.remove(item)
    
"""
Example code
"""
chemDrawer = Storage("Drawer", 4, ["One chemical", "Other chemical"], "<description>")