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

    def clone(self, name=self.name, function=self.function, description=self.description):
    	"""
		Creates a copy of an object (ex. create two different items of the same type without referring to the same section in memory)
		All attributes can be changed as optional parameters
    	"""
    	clone = Item(name, function, description)
    	return clone