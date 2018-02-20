"""
Creates Items and Furniture.
"""

class Item:
	def __init__(self, name, function, description):
		"""
		:param name: name of item
		:param function: function of item
		"""
		self.name = name
		self.function = function
		self.description = description

	def getName(self):
		return self.name

	def getFunction(self):
		return self.function

	def getDescription(self):
		return self.getDescription

	def clone(self, name="", function=None, description=""):
		"""
		Creates a copy of an object (ex. create two different items of the same type without referring to the same section in memory)
		All attributes can be changed as optional parameters
		"""
		clName = name if name > 0 else self.name
		clFunction = function if function != None else self.function
		clDescription = description if description else self.description

		clone = Item(clName, clFunction, clDescription)
		return clone

Pencil = Item("Pencil", "<insert function here>", "A writing utensil.")
print "Name:\t\t" + Pencil.getName()
#print "Description:\t" + Pencil.getDescription()
print "Function:\t" + Pencil.getFunction()

Pen = Pencil.clone(name = "Pen")
print "Name:\t\t" + Pen.getName()
#print "Description:\t" + Pen.getDescription()
print "Function:\t" + Pen.getFunction()
