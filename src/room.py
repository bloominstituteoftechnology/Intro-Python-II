# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

        self.n_to: Room = None
        