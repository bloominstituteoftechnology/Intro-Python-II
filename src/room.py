# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, loot=[]):
        self.name = name
        self.description = description
        self.loot = loot

    def __repr__(self):
        return f"{self.name}, {self.description}"
