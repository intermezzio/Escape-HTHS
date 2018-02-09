
"""
Storage ex. Chest, Drawer

"""

class Storage:
    def __init__(self, name, space, objects, description):
        self.name = name
        self.space = space
        self.objects = objects
        self.description = description
        self.used = len(objects)

"""
Example code
"""
chemDrawer = Storage("Drawer", 4, ["One chemical", "Other chemical"], "<description>")