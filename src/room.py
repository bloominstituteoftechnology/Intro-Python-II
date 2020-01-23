# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.connections = {}
        self.items = {}

    def connect(self, room, direction):
        self.connections.update({direction:room})

    def __repr__(self):
        return self.name
    
