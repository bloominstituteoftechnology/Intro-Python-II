# Implement a class to hold item information. This should have name and
# description attributes.


class Item():

    def __init__(self, name, desc):
        # Initialize name and desc during creation.
        self.name = name
        self.desc = desc

    def __str__(self):
        return f'{self.name}: {self.desc}'
