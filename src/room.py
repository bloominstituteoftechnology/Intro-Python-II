# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    """ A class for rooms """

    def __init__(self, name, description):
        self.name = name
        self.description = description


    def __str__(self):
        return f"You are in room {self.name}, this room is {self.description}"
