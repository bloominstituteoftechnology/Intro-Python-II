from textwrap import fill
from item import Item
from player import Player
from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", {'n': 'foyer'}),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east. Propped against the west wall lies the decaying remains
of a long lost explorer.""", {'s': 'outside', 'n': 'overlook', 'e': 'narrow'},
['sword']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", {'s': 'foyer'}, ['potion']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", {'w': 'foyer', 'n': 'treasure'},
['feather', 'nuts']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", {'s': 'narrow'}, ['mushroom']),
}

items = {
    'sword': Item("Stone Sword", "A heavy and primitive stone sword"),

    'potion': Item("Potion Bottle", """A effervescent bottle of glowing green liquid
    with a "Drink Me" label"""),

    'feather': Item("Eagle Feather", """The tail feather of a golden eagle split nearly
    in half."""),

    'nuts': Item("Mixed Nuts", "A pouch full of mixed nuts still in their shell"),

    'mushroom': Item("Miracle Cap", """A phosphorescent mushroom, beautiful but smells like 
    rotten fish.""")
}
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


player = Player("outside")

user_input = ""

while user_input != "q":
    
    location = player.get_location()
    current_room = room[location]
    
    print(current_room.name)
    print(fill(current_room.description))
    
    if len(current_room.inventory) == 0:
        print("The room contains no items.")
    else:
        print("The room contains the following items:", ", ".join(current_room.inventory))

    prompt_txt = """
    You may take/drop an item by entering take [item name] or drop [item name].
    Enter i to get a list of items you are carrying. 
    Enter a direction n/s/e/w to move to another room.
    Enter q to quit: 
    """
    user_input = input(prompt_txt).lower()
    split_txt = user_input.split()
    
    if len(split_txt) < 2:
        if user_input == "i":
            if len(player.inventory) == 0:
                print("Your pockets are currently empty.")
            else:
                print("You are carrying: ", ", ".join(player.inventory))
                for item in player.inventory:
                    print(items[item])
        elif user_input in current_room.exits:
            next_room = current_room.exits[user_input]
            player.set_location(next_room)
        elif user_input != 'q':
            print("That is not a valid input. Please try again.")
        else:
            print("Thank you for playing my adventure game.")
    
    elif len(split_txt) >= 2:
        if split_txt[0] == "take":
            if split_txt[1] in current_room.inventory:
                current_room.take_item(split_txt[1])
                player.take_item(split_txt[1])
                items[split_txt[1]].on_take()
            else:
                print("That item is not located in this room.")
        elif split_txt[0] == "drop":
            if split_txt[1] in player.inventory:
                current_room.drop_item(split_txt[1])
                player.drop_item(split_txt[1])
                items[split_txt[1]].on_drop()
            else:
                print("You are not carrying this item.")

            


