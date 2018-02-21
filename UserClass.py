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
		elif self.health < maximum_health:
			self.health = maximum_health
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