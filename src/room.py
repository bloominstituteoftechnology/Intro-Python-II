# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, passage):
        self.name = name
        self.description = description
        self.passage = passage
#contents

'''outside = Room("Outside Cave Entrance", "North of you, the cave mount beckons.", {passage})

foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", {passage})

overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", {passage})

narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", {passage})

treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", {passage})'''
