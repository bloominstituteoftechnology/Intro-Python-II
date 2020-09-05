# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.name = name.replace(' ', '_')  # One 'word' names
        self.description = description
        self.items = []
    
    def addItem(self, item):
        self.items.append(item)