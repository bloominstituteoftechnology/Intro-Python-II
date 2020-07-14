# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name):
        self.name = name
    
    def room_description(self, name):
        if self.name == 'outside':
            self.room_description == "Outside Cave Entrance", 
            "North of you, the cave mount beckons"
        elif self.name == 'foyer':
            print("""Foyer, Dim light filters in from the south. Dusty
passages run north and east.""")
        elif self.name == 'overlook':
            print("""Grand Overlook, A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")
        elif self.name == 'narrow passage':
            print( """Narrow Passage, The narrow passage bends here from west
to north. The smell of gold permeates the air.""")
        elif self.name == 'treasure':
            print("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

if __name__ == '__main__':
    player_1 = Room("outside")
    print(player_1.room_description)