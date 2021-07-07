# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description, location, items=[]):
        self.name = name
        self.description = description
        self.location = location
        self.items = items