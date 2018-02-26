import random
"""
Creates Items and Furniture.
"""

class Item:
	def __init__(self, name, damage, description):
		"""
		:param name: name of item
		:param damage: possible damage of item
		:param description: description of item
		"""
		self.name = name
		self.damage = damage
		self.description = description

	def getName(self):
	    """
	    Returns name
	    """
	    return self.name
	
	def getDamage(self):
	    """
	    Returns damage
	    """
	    return self.getDamage

	def attack(self):
	    """
	    Returns the amount of damage dealt
	    Returns None if not a weapon
	    """
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
	    """
	    Returns amount healed
	    """
	    return self.damage * -1

	def getDescription(self):
	    """
	    Returns description
	    """
	    return self.description

	def clone(self, name="", damage=None, description=""):
		"""
		Creates a copy of an object (ex. create two different items of the same type without referring to the same section in memory)
		All attributes can be changed as optional parameters
		"""
		clName = name if name != "" else self.name
		clDamage = damage if damage != None else self.damage
		clDescription = description if description else self.description

		clone = Item(clName, clDamage, clDescription)
		return clone

'''
Pencil = Item("Pencil", 1, "A writing utensil.")
print "Name:\t\t" + Pencil.getName()
#print "Description:\t" + Pencil.getDescription()
print "Function:\t" + str(Pencil.attack())

Pen = Pencil.clone(name = "Pen")
print "Name:\t\t" + Pen.getName()
#print "Description:\t" + Pen.getDescription()
print "Function:\t" + str(Pen.attack())
'''