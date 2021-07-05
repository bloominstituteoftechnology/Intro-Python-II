from room import Room
from player import Player
from item import Item
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
# Mains_tp
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

user_input = ""

while user_input != 'q':
    print(player.room.name)
    print(player.room.description)

    user_input = input("Give a command: ")

    if user_input == 'i' or user_input == "inventory":
            print(player.items)

    if user_input == 'q':
        print("Thanks for playing")
        break

    if len(user_input) == 1:
        if user_input == 'n' or user_input == 'N':
            if player.room.n_to != None:
                player.room = player.room.n_to
            else:
                print("You can not move in this direction, please try again")
        elif user_input == 's' or user_input == 'S':
            if player.room.s_to != None:
                player.room = player.room.s_to
            else:
                print("You can not move in this direction, please try again")

        elif user_input == 'e' or user_input == 'E':
            if player.room.e_to != None:
                player.room = player.room.e_to
            else:
                print("You can not move in this direction, please try again")

        elif user_input == 'w' or user_input == 'W':
            if player.room.w_to != None:
                player.room = player.room.w_to
            else:
                print("You can not move in this direction, please try again")
        
        else:
            print("Please enter a valid input or q to quit. Valid input examples: N, S, E, W")
    else:
        command = user_input.split()
        if len(command) == 2:
            if command[0] == 'get' or command[0] == 'take':
                for item in player.room.items:
                    if command[1] == item.name:
                        player.room.removeItem(item)
                        player.addItem(item)
                        item.on_take()
                else:
                    print("The item is not available in the room")
            elif command[0] == 'drop':
                for item in player.items:
                    if command[1] == item.name:
                        player.removeItem(item)
                        player.room.addItem(item)
                        item.on_drop
                    
        else:
            print("Error please enter a valid command")

        