# Implement a class to hold room information. This should have name and
# description attributes.

# room = {
#     'outside':  Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons"),


class Room:
    """The room class contains a constructor to instanciate a new room.
    The room contains a method to print it's description. Trigger the
    method on this room when a player enters"""
    def __init__(self, name, description, inventory):
        self.name = name
        self.description = description
        self.inventory = inventory
