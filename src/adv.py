from room import Room
from player import Player
from item import Item
# Declare all the rooms
#Update for Branch
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons ..."),

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
room['overlook'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Main

items = {
    "sword": Item("Sword", "This is used to stab things."),
    "lantern": Item("Lantern", "This would be helpful in the dark."),
    "shovel": Item("Shovel", "This could be used to bludgen or dig.")



}

room['outside'].items.append(items["lantern"])
room['overlook'].items.append(items["sword"])
room['narrow'].items.append(items["shovel"])

# Make a new player object that is currently in the 'outside' room.
new_player = Player(player_name = "Ryan", current_room = room["outside"])
print("\nWelcome player! You may enter a direction in which to travel with n, s, e, w, and q to quit the game.\n\nYou may get, take, pickup items, or drop them.\n\n")
print(f"{new_player.player_name} is {new_player.current_room} \n")
print(new_player.current_room.list_items())

# Write a loop that:
while True: 
# * Prints the current room name
    
# * Prints the current description (the textwrap module might be useful here).

# * Waits for user input and decides what to do.
    selection = input("Enter a direction, command or Q to escape: ")
    user_selection = selection.lower().split(" ")
    if len(user_selection) == 1: 
        if selection == "q": 
            print("Have a good day. Thanks for playing.")
            break
        elif selection == "n" or selection == "s" or selection == "e" or selection == "w":
            new_player.move(selection)
            print(f"\n{new_player.player_name} is {new_player.current_room.room_name} \n{new_player.current_room.description}\n\n {new_player.current_room.list_items()}")
        elif selection == "i":
            new_player.print_items()
        else:
            print("That is not a proper command.")
    elif len(user_selection) == 2: 
        if user_selection[0] in ["take", "get", "pickup"]:
            if items[user_selection[1]]:
                new_player.pickup_item(items[user_selection[1]])
                
                print("\n\nYou have added a new item to inventory!\n")
                print(f"{new_player.player_name} is {new_player.current_room} \n")
                print(new_player.current_room.list_items())
            else:
                print("That isn't an item.")
        elif user_selection[0] == "drop": 
            if items[user_selection[1]]:
                new_player.drop_item(items[user_selection[1]])
                print("You dropped an item!")
                print(new_player.print_items())
                print(f"{new_player.player_name} is {new_player.current_room} \n")
                print(new_player.current_room.list_items())
            else: 
                print("That isn't an item.")
        else: 
            print("That is not a proper command.")
    else: 
        print("That is not a proper command.")

# If the user enters a cardinal direction, attempt to move to the room there.

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
