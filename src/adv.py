from room import Room
from player import Player

# Declare all the rooms

outside = Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons")
foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""")
overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")
narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""")
treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")


# Link rooms together

outside.connect(room=foyer, direction='n')
foyer.connect(room=outside, direction='s')
foyer.connect(room=overlook, direction='n')
foyer.connect(room=narrow, direction='e')
overlook.connect(room=foyer, direction='s')
narrow.connect(room=foyer, direction='w')
narrow.connect(room=treasure, direction='n')
treasure.connect(room=narrow, direction='s')



if __name__ == "__main__":
    # Make a new player object that is currently in the 'outside' room.

    player_1 = Player(outside)

    # Write a loop that:

    run = True

    while run:
        player_1.look()
        direction = input('Where do you go? (n, e, s, w or quit with "q") ')
        if direction == 'q':
            print('Bye!')
            break
        player_1.move(direction=direction)
        print('\n')