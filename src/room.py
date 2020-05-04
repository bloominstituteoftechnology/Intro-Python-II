# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    name = None
    description = None

    def __init__(self, name, description):
        self.name = name
        self.description = description
