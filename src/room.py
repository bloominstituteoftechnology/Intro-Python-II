# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__ (self,roomName, description):
        self.roomName = roomName
        self.description = description

    def __str__(self):
        return f"This rooms name is {roomName} and the size is {size}"