"""
Creates and edits user information.
"""

class User:
	def __init__(self, name, items, keys, health, space = 5):
		"""
		:param name: user name
		:param items: items in backpack
		:param keys: keys user has attained
		:param health: healthpoints user has
		:param space: room in backpack
		"""
		self.name = name
		self.items = []
		self.keys = []
		self.health = health
		self.space = space
	
	def addKey(self, key):
		"""
		Adds discovered key to list of already discovered keys.
		Returns the number of keys discovered.
		:param key: key discovered
		"""
		self.keys.append(key)
		return len(self.keys)
	
	def removeItem(self, item):
		"""
		Removes an item from the backpack.
		Returns deleted item when done successfully.
		:param item: item to be removed
		Errors
			-1: Item is not in backpack
		"""
		try:
			index = self.items.index(item)
		except ValueError:
			return -1
		else:
			self.items.pop(index)
	
	def addItem(self, item):
            """
	    Adds an item to the backpack.
	    Returns added item when done successfully.
	    :param item: item to be added
	    Errors
	               -1: The backpack is full
            """
            if len(self.items) < self.space:
	       self.items.append(item)
	       return item
            else:
	       return -1
	
	def addHealth(self, points):
		"""
		Adds health points to user's health.
		:param points: points to be added to health
		returns health
		Errors
			-1: Health is already at maximum
		"""
		if points < 0:
		    points = points * -1
		maximum_health = 10
		if self.health == maximum_health:
		    return -1
		else:
		    self.health = min(maximum_health, self.health+points)
		    return self.health
	
	def removeHealth(self, points):
		"""
		Removes health points from user's health.
		:param points: points to be removed from health
		returns health
		Errors
		      -1: Health reached 0
		"""
		self.health = self.health - points
		if self.health <= 0:
		    #GameOver
		    return -1
		else:
		    return self.health

	def getItems(self):
	   return self.items
	  
	def getWeapons(self):
	    """
	    returns dictionary as shown:
	        key    value
	        name   description
	    """
	    itemDict = dict()
	    for item in self.items:
	        if item.getDamage() > 0 and item.getDamage() != 4:
	           itemDict[item.getName()] = item.getDescription()
	     
	    return itemDict
	
	def getHealingItems(self):
	    """
	    returns dictionary as shown:
	        key    value
	        name   description
	    """
	    itemDict = dict()
	    for item in self.items:
	        if item.getDamage() < 0:
	           itemDict[item.getName()] = item.getDescription()
	     
	    return itemDict
	
	def useBandaid(self):
	    self.addHealth(4)
	    items = self.items
	    bandaid = None
	    for item in items:
	        if item.getDamage() == -4:
	            bandaid = item
	   
	    self.items.remove(bandaid)
	    return self.health
	
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

	def getSpace(self):
		return self.space
	
	def upgradeSpace(self):
	        if self.space == 5:
	            self.space = 10
	            return "You got a bigger backpack!"
	        else:
	            return "You already upgraded your backpack!"
	
	def getName(self):
	    return self.name
	
	def getItemNames(self):
	    names = []
	    for item in self.items:
	        names.append(item.getName())
	    return names
		
	def changeName(self, name):
	    self.name = name
	
	def getKeys(self):
	    return self.keys
	   
	def getHealth(self):
	    return self.health