# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items_stored = []
    
    def __str__(self):
        return f' At "{self.name} , "{self.description}"'

    def placed_item(self, item):
        self.items_stored.append(item)