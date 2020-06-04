# Implement a class to hold information. This should have a name and 
#description attributes

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return (f"{self.name}, item description: {self.description}")