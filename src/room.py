from item import Item
# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items): 
        self.name = name
        self.description = description
        self.items = items
       
    def __str__(self):
        output = self.name
        for i in self.items:
            output += "\n" str(i)

        return output
       

