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

# Make a new player object that is currently in the 'outside' room.

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
# current_room = "outside"D
name = input("Please enter your name: ")
current_room = 'outside'
# print(player1)

while True:
    # print("Hello!!")
    # break
    player1 = Player(name, current_room)
    GameRoom = Room(room[current_room].name, room[current_room].description)
    # print(player1)
    print("You are currently at " + GameRoom.name + " and " + GameRoom.description)
    # break
    direction = input('Which direction would you like to go?(n/s/e/w): ')

    if direction == "q":
        break

    elif current_room == "outside":
        if direction =="n":
            current_room = "foyer"
            # break
        else:
            print("That way is blocked choose another ")
            continue
            # break

    elif current_room == "foyer":
        if direction == "s":
            current_room = "outside"
        elif direction == "n":
            current_room = "overlook"
        elif direction == "e":
            current_room = "narrow"
        else:
            print("Cannot go that way choose another: ")
            continue

    elif current_room == "overlook":
        if direction == "s":
            current_room = "foyer"
        elif direction == "n":
            print("You fall to your death game over!")
            break
        else:
            print("You cannot go that way choose another: ")
            continue

    elif current_room == "narrow":
        if direction == "w":
            current_room = "foyer"
        elif direction == "n":
            current_room = "treasure"
        elif direction == "e":
            print("You hit a wall ouch! Can't go that way choose another: ")
            continue
        else:
            print("You cannot go that way choose another: ")
            continue

    elif current_room == "treasure":
        if direction == "s":
            current_room = "narrow"
        else:
            print("You cannot go that way choose another: ")
            continue