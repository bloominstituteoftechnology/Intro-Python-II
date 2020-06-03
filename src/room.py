# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description

    def __str__(self):
        return f"current room: {self.name}, description: {self.description}"