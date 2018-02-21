"""
Creates and edits user information.
"""

class User:
	def __init__(self, name, items, keys, health, space = 10):
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
	
	def addHealth(self, points):
		"""
		Adds health points to user's health.
		:param points: points to be added to health
		Errors
			-1: Health is already at maximum
		"""
		maximum_health = 10
		if self.health <= maximum_health - points:
			self.health = self.health + points
			return self.health
		elif self.health < maximum_health:
			self.health = maximum_health
			return self.health
		else:
			return -1
	
	def removeHealth(self, points):
		"""
		Removes health points from user's health.
		:param points: points to be removed from health
		"""
		self.health = self.health - points
		if self.health <= 0:
			#GameOver
			pass

	def getItems(self):
		return self.items

	def getSpace(self):
		return self.space
	
	def upgradeSpace(self):
	        if self.space == 10:
	            self.space = 15
	            return "You got a bigger backpack!"
	        else:
	            return "You already upgraded your backpack!"
	        