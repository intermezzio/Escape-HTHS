"""
Creates Items and Furniture.
"""

class item:
    def __init__(self, name, function, description):
        """
        :param name: name of item
        :param function: function of item
        """
        self.name = name
        self.function = function
        self.description = description