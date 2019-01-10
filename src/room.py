# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, item_list = []):
        self.name = name
        self.description = description
        self.item_list = item_list