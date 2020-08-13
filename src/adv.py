from room import Room
from player import Player
from item import Item

"""
MVP 1 done

MVP 2 
Make rooms able to hold multiple items : DONE
Make the player able to carry multiple items : DONE
Add items to the game that the user can carry around : DONE
Add get [ITEM_NAME] and drop [ITEM_NAME] commands to the parser
MORE ON THIS:
Add a new type of sentence the parser can understand: two words.

Until now, the parser could just understand one sentence form:

verb

such as "n" or "q".

But now we want to add the form:

verb object

such as "take coins" or "drop sword".

Split the entered command and see if it has 1 or 2 words in it to determine if it's the first or second form.

? x = input("Enter comma-separated numbers: ").split(',')
* EG if it is north, the lenght of returned list should be 1, else two

Implement support for the verb get followed by an Item name. This will be used to pick up Items.

If the user enters get or take followed by an Item name, look at the contents of the current Room to see if the item is there.

If it is there, remove it from the Room contents, and add it to the Player contents.

If it's not there, print an error message telling the user so.

Add an on_take method to Item.

Call this method when the Item is picked up by the player.

on_take should print out "You have picked up [NAME]" when you pick up an item.

The Item can use this to run additional code when it is picked up.

Add an on_drop method to Item. Implement it similar to on_take.

Implement support for the verb drop followed by an Item name. This is the opposite of get/take.

Add the i and inventory commands that both show a list of items currently carried by the player.

"""
# Declare all the rooms
valid_inputs = ['q', 'n', 's', 'e', 'w']

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

items = {
    'sword': Item("Sword", "Mighty sword"),
    'coins': Item("Coins", "Gold is worth much in these parts"),
    'skull': Item("Dead man", "The sxull of traveler"),
    'food': Item("Mushroom", "Stay healthy in these times"),
    "elixr": Item("Elixr", "Inhale for good omens")

}

room['foyer'].items = [items['sword'], items['skull']]
room['treasure'].items = [items['coins'], items['skull'], items['elixr']]
room['narrow'].items = [items['food']]
room['narrow'].items = [items['elixr']]



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
user = input("Hey friend, are you ready for your adventure time. If so, enter your name else, press q to quit: ")
if user == 'q':
    raise "Exit game"

user_input = ''
valid_input = ['n', 's', 'e', 'w', 'q']

player = Player(user, room['outside'])

# Write a loop that:
while user_input != 'q':
    current_room = player.current_room
# Prints the current room name
    print(f"\n{user} has entered the {player.current_room.name}.\n\n")
# Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)
    print(f"Items: {current_room.items}")

# Waits for user input and decides what to do.
    user_input = input('\nWhich way do you want to do or go?\n'
                      'Directions: [n] North [s] South [e] East [w] West\n'
                      'Items: take (item), drop (item), or inspect (item)\n'
                      '[i] Inventory\n'
                      'or [q] Quit:\n')
    print("\n")
#   
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

    if user_input == "n":
        if current_room.n_to is not None:
            player.current_room = current_room.n_to
        else:
            #  handle error
            pass

    elif user_input == "s":
        if current_room.s_to is not None:
            player.current_room = current_room.s_to
        else:
            #  handle error
            pass

    elif user_input == "e":
        if current_room.e_to is not None:
            player.current_room = current_room.e_to
        else:
            #  handle error
            pass

    elif user_input == "w":
        if current_room.w_to is not None:
            player.current_room = current_room.w_to
        else:
            #  handle error
            pass
        
    elif "take" in user_input:
        # add item to player inventory
        # remove item from room
        action = user_input.split()
        print(action)
        # action_verb = action[0]
        # action_item = action[1]
        # player.take(action_item)
        
        # CALL HERE for item on take
        print("Take me jesus")
    
    elif "take" in user_input:
        # add item to player inventory
        # remove item from room
        action = user_input.split()
        print(action)
        # action_verb = action[0]
        # action_item = action[1]
        # player.take(action_item)
        
        # CALL HERE for item on take
        print("Take me jesus")
    
    elif "drop" in user_input:
        # item from player to the items list on the room object
        # remove action item from player
        print("Drop it like its hot")
#
# If the user enters "q", quit the game.

#  Add a REPL parser to `adv.py` that accepts directional commands to move the player
#   * After each move, the REPL should print the name and description of the player's current room
#   * Valid commands are `n`, `s`, `e` and `w` which move the player North, South, East or West
#   * The parser should print an error if the player tries to move where there is no room.