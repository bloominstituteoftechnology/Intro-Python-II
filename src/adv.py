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
# Main
#

# Make a new player object that is currently in the 'outside' room.

name = input("enter player's name\n>")
player = Player(name, room["outside"])
print(player)

# def try_direction(direction, room):
#     attr = direction + "_to"
#     if hasattr(room, attr):
#         return getattr(room, attr)
#     else:
#         print("you cant go that way")
#         return room 

while True:
    # print(player.room.name)
    # print(player.room.description)
    user_input = input("\n> ").lower()

    if len(user_input) == 1:
        if not user_input in ["n", "s", "e", "w", "q"]:
            print(f"that's not valid")
        elif user_input == "n":
            if True:
                player.room = player.room.n_to
                print(player.room)
            else:
                print("you can't move north")

        elif user_input == "s":
            if True:
                player.room = player.room.s_to
                print(player.room)
            else:
                print("you can't move south")

        elif user_input == "e":
            if True:
                player.room = player.room.e_to
                print(player.room)
            else:
                print("you can't move east")
        
        elif user_input == "w":
            if True:
                player.room = player.room.w_to
                print(player.room)
            else:
                print("you can't move west")
        # user_input = user_input[0][0]

        elif user_input == "q":
            break

    # elif len(user_input) == 4 or len(user_input) == 3:
    #     if not first_word in ["get", "drop"]:
    #         print(f"{user_input} is not an option")
    #     elif user_input == "get":
    #         player.inventory.append(item)
    #         print("grabbed item")
    #     elif user_input == "drop":
    #         player.inventory.remove(item)
    #         print("dropped item")

    # else:
    #     print("I don't understand that")
    #     continue
