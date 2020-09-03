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
def set_up_rooms():
    room['outside'].n_to = room['foyer']
    room['foyer'].s_to = room['outside']
    room['foyer'].n_to = room['overlook']
    room['foyer'].e_to = room['narrow']
    room['overlook'].s_to = room['foyer']
    room['narrow'].w_to = room['foyer']
    room['narrow'].n_to = room['treasure']
    room['treasure'].s_to = room['narrow']

# Add items to rooms
def add_room_items():
    room['outside'].add_item(Item("Torch", f"A light to guide you through the darkness, {player.name}"))
    room['foyer'].add_item(Item("Shield", "A large oak shield painted red with a white chevron crossing it."))
    room['overlook'].add_item(Item("Map", "Perhaps this will help us find our way."))
    room['narrow'].add_item(Item("Sword", f"Arm yourself with knowledge, {player.name}, it may serve you better than steel!"))
    room['treasure'].add_item(Item("Book", "The Zen of Python, by Tim Peters\n Beautiful is better than ugly.\n Explicit is better than implicit.\n Simple is better than complex.\n Complex is better than complicated.\n Flat is better than nested.\n Sparse is better than dense.\n Readability counts.\n Special cases aren't special enough to break the rules.\n Although practicality beats purity.\n Errors should never pass silently.\n Unless explicitly silenced.\n In the face of ambiguity, refuse the temptation to guess.\n There should be one-- and preferably only one --obvious way to do it.\n Although that way may not be obvious at first unless you're Dutch.\n Now is better than never.\n Although never is often better than *right* now.\n If the implementation is hard to explain, it's a bad idea.\n If the implementation is easy to explain, it may be a good idea.\n Namespaces are one honking great idea -- let's do more of those!"))

#
# Main
#

directions = ['n', 's', 'e', 'w']
actions = ['take', 'drop']

# Make a new player object that is currently in the 'outside' room.
player_name = input('What is your name, adventurer? ')
player = Player(player_name, room['outside'])
print("To move around the map, press 'n', 'e', 's', 'w'. Look for items to help on your way. For help try 'Help' or 'h'.")
print(f"Good luck, {player.name}")
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

# print(f"{player.name}, you find yourself in {player.current_room.name}. \n{player.current_room.description}")
set_up_rooms()
add_room_items()
player.look()

while True:
    user_input = input(f"Where would you like to go {player.name}? ").lower().split()

    if len(user_input) > 2 or len(user_input) < 1:
        print(f"Sorry, {player.name}, that's not a valid one or two word command. Would you like 'help'?")
    
    elif len(user_input) == 2:
        if user_input[0] in actions:
            if user_input[0] == "t" or user_input[0] == "take":
                item = player.select_item(user_input[1])
                player.take(item)
            elif user_input[0] == "d" or user_input[0] == "drop":
                item = player.select_item(user_input[1])
                player.drop(item)
            
    
    else:
        if user_input[0] == "q" or user_input[0] == "quit":
            print(f"Thanks for playing {player.name}!") 
            break

        elif user_input[0] == "h" or user_input[0] == "help":
            print("Commands:\n'n' - Move North\n's' - Move South\n'e' - Move East\n'w' - Move West\n't' or 'take' '<item>' - Take Item\n'd' or 'drop' '<item>' - Drop Item\n'inv' or 'inventory' - Examine Inventory Items\n'l' or 'look' - Look around the current room\n'h' or 'help' - Help Menu\n'q' or 'quit' - Exit Game\n")
            continue

        elif user_input[0] == "l" or user_input[0] == "look":
            player.look()
            continue

        elif user_input[0] == "inv" or user_input[0] == "inventory":
                player.show_inventory()

        elif user_input[0] in directions:
            try:
                player.change_room(user_input[0])
                print(f"You are in the {player.current_room.name}. \n{player.current_room.description}")
            except AttributeError:
                print(f"{player.name}'s adventure lies elsewhere.'")

        else:
            print('Movement not allowed! Please enter a direction (n, s, e, w) to move around the map')
