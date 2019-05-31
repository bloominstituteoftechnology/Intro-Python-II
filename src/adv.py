from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

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


# Items to add to rooms
item = {
    "cheese": Item("cheese", "a piece of cheddar cheese packaged and sealed"),
    "bat": Item("bat", "a wood baseball bat for self defense"),
    "gum": Item("gum", "a pack of gum for bad breath"),
    "lightsaber": Item("lightsaber", "a lightsaber energy sword, the weapon of choice for Jedis"),
    "bag": Item("bag", "a bag to collect booty and get rich!"),
    "mouse": Item("mouse", "a dead and dry mouse is the only thing left behind..."),
}

# adding items to rooms
room['outside'].add_item(item["cheese"])
room['foyer'].add_item(item["bat"])
room['foyer'].add_item(item["gum"])
room['overlook'].add_item(item["lightsaber"])
room['narrow'].add_item(item["bag"])
room['treasure'].add_item(item["mouse"])


# Main
# Make a new player object that is currently in the 'outside' room.

# _______ Intro Message _____________________
print("//////////////////////////////////")
print("////// Welcome to THE MAZE //////")
print("/////////////////////////////////\n")

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

# Begining of REPL (Read, Evaluate, Print, Loop)
# will wait for response from user and according to it
# proceed to process move and print out description of room
# or print out message in case move fails
# then wait for user input again

# print('INPUT GIVEN BY USER:', cmd.strip(' '))

cmds = ['n', 's', 'e', 'w', 'q']
curr_player = Player("P1", room["outside"])

#_____ REPL __________________________________
while True:
    room = curr_player.current_room
    print(f"------------------\nYour current location is the {room.name}.\n")
    print("..."+room.description+"..\n------------------\n")
    
    # checking player inventory
    if len(curr_player.player_inventory) < 1:
        print("Your inventory of items is null.")
    else:
        print(f"This is your inventory of items:\n{curr_player.player_inventory}\n")

    print(f"Items found here:\n{room.items_list}\n")

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    print("To move around choose from [n]North, [s]South, [e]East, or [w]West.\nOr [q] to Quit from The Maze\n")
    cmd = input("Where would you like to go to begin?: ")
    
    # splitting inputs/parsing
    # getting a list from split()
    cmd = cmd.split()
    if len(cmd) == 1:
        action = cmd[0]
    elif len(cmd) == 2:
        action = cmd[0]
        item = cmd[1]
    
    # quitting if "q" as input
    if cmd[0] == "q":
        exit()
    
    # moving to room according to direction imput
    # by instantiating "move_player" method from "Player" class
    elif (action != "q") & (cmd[0] in cmds):
        curr_player.move_player(cmd[0])
    
    # getting item: add to "player_inventory" & remove from room
    elif (action == "take") or (action == "get"):
        if item in room.items_list:
            curr_player.get_item(item)
            room.remove_item(item)
    # dropping item: add to room & remove from "player_inventory"
    elif action == "drop":
        if item in curr_player.player_inventory:
            room.add_item(item)
            curr_player.drop_item(item)

    else:
        print("Invalid command. Please try again.")

    # print(f'Your current location is the {curr_player.location.title}.')
    # print("..."+curr_player.location.description+"..")
    # print(f"Items here:")
    # curr_player.location.list_items()
    # cmd = input("\nWhere would you like to go now?\n ([n]North, [s]South, [e]East, or [w]West.\nOr [q] to Quit): ")



