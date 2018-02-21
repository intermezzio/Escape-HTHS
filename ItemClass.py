import random
"""
Creates Items and Furniture.
"""

class Item:
	def __init__(self, name, damage, description, size=1):
		"""
		:param name: name of item
		:param damage: possible damage of item
		"""
		self.name = name
		self.damage = damage
		self.description = description
		self.size = size

	def getName(self):
		return self.name

	def attack(self):
		if self.damage == 0:
		    return None
		elif self.damage == 1 or self.damage == 2:
		    return self.damage
		elif self.damage == 3:
		    return random.randint(3,5)
		elif self.damage == 10:
		    randomInt = random.randint(1,4)
		    if randomInt == 1:
		        return 10
		    else:
		        return 0
	
	def heal(self):
	    return self.damage

	def getDescription(self):
		return self.getDescription

	def clone(self, name="", damage=None, description=""):
		"""
		Creates a copy of an object (ex. create two different items of the same type without referring to the same section in memory)
		All attributes can be changed as optional parameters
		"""
		clName = name if name > 0 else self.name
		clDamage = damage if damage != None else self.damage
		clDescription = description if description else self.description

		clone = Item(clName, clDamage, clDescription)
		return clone

Pencil = Item("Pencil", 1, "A writing utensil.")
print "Name:\t\t" + Pencil.getName()
#print "Description:\t" + Pencil.getDescription()
print "Function:\t" + str(Pencil.attack())

Pen = Pencil.clone(name = "Pen")
print "Name:\t\t" + Pen.getName()
#print "Description:\t" + Pen.getDescription()
print "Function:\t" + str(Pen.attack())
