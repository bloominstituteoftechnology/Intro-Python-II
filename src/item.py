# Implement a class to hold item information. This should have name and description attributes.

""" 
The Magical Items. Don't put on the ring. Trust me.

Attributes:
-name
-description

"""

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f"Item: {self.name} \n Description: {self.description}"