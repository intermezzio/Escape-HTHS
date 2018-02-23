
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
    
    def getSpace(self):
        return self.space
    
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
    
    def getItemsDict(self):
	    """
	    returns dictionary as shown:
	        key    value
	        name   [description, quantity]
	    """
	    itemDict = dict()
	    for item in self.items:
	        try:
	            itemDict[item.getName()][1] += 1
	        except KeyError:
	           itemDict[item.getName()] = [item.getDescription(), 1]
	    return itemDict
    
    def remove(self, item):
        self.items.remove(item)
    
    def add(self, item):
        self.items.append(item)
    
"""
Example code
"""
chemDrawer = Storage("Drawer", 4, ["One chemical", "Other chemical"], "<description>")