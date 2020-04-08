# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits

    def get_room(self):
        return self.name

    def get_description(self):
        return self.description


       