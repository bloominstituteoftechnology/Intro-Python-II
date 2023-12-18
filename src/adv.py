from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
#possible directions
# possible_directions = ['n', 'e', 'w', 's']
# Make a new player object that is currently in the 'outside' room.
# new_player = Player("Sal", room['outside'])
new_player = Player("Sal", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# print(player.current_room)
# player.print_current_location FIX

print(new_player)
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
# if cmd == 'q':
#         print("goodbye")
#         break
# print(f'\nCurrently in room: {self.current_room.name}\n')

selection = input('You are outside. To start journey make a move using n,e,w,s keys or quit using q:\n')
while(selection != 'q'):
    if new_player.current_room == room['outside'] and selection == 'n':
        new_player.current_room = room['foyer']
        print(new_player.current_room)

        if new_player.current_room == room['foyer'] and selection == 's':
            new_player.current_room = room['outside']
            print(new_player.current_room)
            selection = input('Where do you want to go? Select n,e,w,s to move or q to quit ')

        elif new_player.current_room == room['foyer'] and selection == 'n':
            new_player.current_room = room['overlook']
            print(new_player.current_room)
            selection = input('Where do you want to go? Select n,e,w,s to move or q to quit ')

            if new_player.current_room == room['foyer'] and selection == 'e':
                new_player.current_room = room['narrow']
                print(new_player.current_room)
                selection = input('Where do you want to go? Select n,e,w,s to move or q to quit ')

        elif new_player.current_room == room['overlook'] and selection == 's':
            new_player.current_room = room['foyer']
            print(new_player.current_room)
            selection = input('Where do you want to go? Select n,e,w,s to move or q to quit ')

            if new_player.current_room == room['narrow'] and selection == 'w':
                new_player.current_room = room['foyer']
                print(new_player.current_room)
                selection = input('Where do you want to go? Select n,e,w,s to move or q to quit ')

        elif new_player.current_room == room['narrow'] and selection == 'n':
            new_player.current_room = room['treasure']
            print(new_player.current_room)
            selection = input('Where do you want to go? Select n,e,w,s to move or q to quit ')

            if new_player.current_room == room['treasure'] and selection == 's':
                new_player.current_room = room['narrow']
                print(new_player.current_room)
                selection = input('Where do you want to go? Select n,e,w,s to move or q to quit ')



else:
    new_player.current_room = room['outside']
    selection = input('Wrong selection. The only way out it n. Select n or q to quit ')
