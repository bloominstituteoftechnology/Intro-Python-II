from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",None, None, None, None),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",None, None, None, None),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",None, None, None, None),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",None, None, None, None),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",None, None, None, None),


}
room['outsude'] = Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",None, None, None, None)

# Link rooms together



room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#Dictionary of items
items = {
    'sword' : Item("sword", "This is a sword"),
    'coin'  : Item('coin', "These are gold coins"),
    'arrow' : Item("arrow","Here is the arrow"),
    "hammer":Item ("hammer","This is na hammer"),
    "anklet" :Item("anklet","Here is the anklet")
}

room['foyer'].add_item('sword')
room['outside'].add_item('coin')
room['overlook'].add_item('arrow')
room['narrow'].add_item('hammer')
room['treasure'].add_item('anklet')


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player= Player("IronMan",room["outside"])


# Write a loop that:
while True:
    print(new_player)


    print("Enter direction : ")
    print("North     : n")
    print("South     : s")
    print("East      : e")
    print("West      : w")
    print("To Quit   : q")
    print("To pick up an item : take <item-name>")
    print("To drop  an item : drop <item-name>")

    direction = input("Enter the new direction that you want to take :")
    words = direction.strip().lower().split(" ")

    if len(words) == 1: #This is direction or 'q'
        if direction not in ["n", "s", "e", "w", "q"]:
            print("Enter valid direction")
            continue

        # if direction is q, break
        if direction == "q":
            print("Game is Over!,Quit the game")
            break

        # if direction == "n":
        # check if room has north direction room.
        # r is current room : payer.current_room
        # if r.to_n is not None:
        # move to r.to_n : player.current_room = r.to_n
        # else:
        #  you can't move

        current_room = new_player.current_room
        if direction == "n":
            if current_room.n_to is None:  # if player's current room has no room in north direction
                print("Can't move")
                continue
            else:
                new_player.current_room = current_room.n_to

        elif direction == "s":
            if current_room.s_to is None:
                print("Can't Move")
                continue
            else:
                new_player.current_room = current_room.s_to

        elif direction == "e":
            if current_room.e_to is None:
                print("Can't Move")
                continue
            else:
                new_player.current_room = current_room.e_to


        elif direction == "w":
            if current_room.w_to is None:
                print("Can't Move")
                continue
            else:
                new_player.current_room = current_room.w_to

    elif len(words) == 2:#drop or pick up items
        if words[0] == "take":
            print("pick up object "+ words[1])
            if words[1] not in new_player.current_room.getItems():
                print("This object is not in this room")
                continue
            else:
                new_player.current_room.delete_item(words[1])
                new_player.add_item(words[1])
        elif words[0] =="drop":
            print("drop off object " + words[1])
            if words[1] not in new_player.get_items():
                print("player doesn't have " + {words[1]}+",he can't drop")
                continue
            else:
                new_player.delete_item(words[1])
                new_player.current_room.add_item(words[1])

        #words[0] is the command : take or drop, if it is neither, give error and continue
        #word[1] is item to take or drop. Make sure this is a n valid item, amd also shoild be there in room
        else:
            print("Invalid command")
            continue
        #check if words[1] exists in diectionary as key or not
        if words[1] not in items.keys():
            print("Select a valid  object")
            continue

        #if we come here, it means word[0] is either take or drop and words[1] is a valid
        #item that we have.



    else:
        print("Invalid command")
        continue




# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
