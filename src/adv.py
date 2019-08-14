from player import Player
from room import Room

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


# for key, value in room.items():
#     print(value.name)
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
zach = Player("Zach", "outside")
player_input = ""

# Write a loop that:
while player_input.lower() != "exit":
    player_input = ""
    for key, value in room.items():
        if key == zach.room:
            current_room = {"name": value.name, "desc": value.description }
# * Prints the current room name
            print(f'Current Room: {current_room["name"]}\n  Description: {current_room["desc"]}')
    player_input = input("Please Select a Direction, 'N,S,E,W': ")
    if player_input.lower() == "n" and room[zach.room].n_to:
        for key, value in room.items():
            if current_room['name'] == room[zach.room].name:
                if value.name == room[zach.room].n_to.name:
                    zach.room = key
    elif player_input.lower() == "s" and room[zach.room].s_to:
        for key, value in room.items():
            if current_room['name'] == room[zach.room].name:
                if value.name == room[zach.room].s_to.name:
                    zach.room = key
    elif player_input.lower() == "e" and room[zach.room].e_to:
        for key, value in room.items():
            if current_room['name'] == room[zach.room].name:
                if value.name == room[zach.room].e_to.name:
                    zach.room = key
    elif player_input.lower() == "w" and room[zach.room].w_to:
        for key, value in room.items():
            if current_room['name'] == room[zach.room].name:
                if value.name == room[zach.room].w_to.name:
                    zach.room = key
    else:
        print("The selected direction doesn't exist for this room")


# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
