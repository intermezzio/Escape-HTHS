
"""
Storage ex. Chest, Drawer

"""

class Storage:
    def __init__(self, name, space, items, description):
        self.name = name
        self.space = space
        self.items = items
        self.description = description
    
    def getName(self):
        return self.name
        
    def getDescription(self):
        return self.description
"""
Example code
"""
chemDrawer = Storage("Drawer", 4, ["One chemical", "Other chemical"], "<description>")