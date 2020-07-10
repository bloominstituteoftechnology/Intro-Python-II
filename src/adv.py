from room import Room
from player import Player
from item import Item

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

#add test comment

items = {
    "sword": Item("sword", "This is a sword"),
    "silver": Item("silver", "These are silver coins"),
    "bow": Item("bow", "Bows and arrows"),
    "sabre": Item("sabre", "This is an ancient sabre"),
    "treasure": Item("treasure", "Empty but still something than nothing.")
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

room['foyer'].add_item('sword')
room['outside'].add_item('silver')
room['overlook'].add_item('bow')
room['narrow'].add_item('sabre')
room['treasure'].add_item('treasure')

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Pete', room['outside'])
# room1 = Room()
# print(room1)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#

# Write a loop that:

while True:
    print(player)

    print("Enter direction : ")
    # print("North     : n")
    # print("South     : s")
    # print("East      : e")
    # print("West      : w")
    # print("To Quit   : q")
    print("To pick up an item : take <item-name>")
    print("To drop  an item : drop <item-name>")

    direction = input("Enter the new direction that you want to take :")
    words = direction.strip().lower().split(" ")

    # ripple = direction.split()
    # print(ripple)

    # This is direction or 'q'
    if len(words) == 1:
        if direction not in ["n", "s", "e", "w", "q"]:
            print("Enter valid direction")
            continue

        # if direction is q, break
        if direction == "q":
            print("Goodbye!")
            break

        # if direction == "n":
        # check if room has north direction room.
        # r is current room : payer.current_room
        # if r.to_n is not None:
        # move to r.to_n : player.current_room = r.to_n
        # else:
        #  you can't move

        current_room = player.current_room
        if direction == "n":
            if current_room.n_to is None:  # if player's current room has no room in north direction
                print("Can't move")
                continue
            else:
                player.current_room = current_room.n_to

        elif direction == "s":
            if current_room.s_to is None:
                print("Can't Move")
                continue
            else:
                player.current_room = current_room.s_to

        elif direction == "e":
            if current_room.e_to is None:
                print("Can't Move")
                continue
            else:
                player.current_room = current_room.e_to

        elif direction == "w":
            if current_room.w_to is None:
                print("Can't Move")
                continue
            else:
                player.current_room = current_room.w_to


# drop or pick up items
    elif len(words) == 2:
        print(len(words))
        if words[0] == "take":
            print("pick up object " + words[1])
            if words[1] not in player.current_room.get_items():
                print("This object is not in this room")
                continue
            else:
                player.current_room.delete_item(words[1])
                player.add_item(words[1])
        elif words[0] == "drop":
            print("drop off object " + words[1])
            if words[1] not in player.get_items():
                print("player doesn't have " + {words[1]} + ",he can't drop")
                continue
            else:
                player.delete_item(words[1])
                player.current_room.add_item(words[1])

        else:
            print("Invalid command")
            continue

        if words[1] not in items.keys():
            print("Select a valid  object")
            continue

        #if we come here, it means word[0] is either take or drop and words[1] is a valid
        #item that we have.

    else:
        print("Invalid command")
        continue