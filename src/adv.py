# Global Imports
import os
import textwrap

# Local Imports
from location import Location
from player import Player
from item import Item, Card, Feature

# Declare all the locations

location = {
    'atrium':  Location("Central Atrium",
                     """Four identical archways sit equidistant along the walls of this immense circular
 room. Bright rays of light beam down from the soaring glass dome roof above. 
 Emblazoned on the smokey white marble floor is a giant, red, greek LAMBDA...
 Above each archway is a cardinal direction (N, S, E, W).
 """),

    'beauty':    Location("Hall of Beauty", """Dim light filters in from the south. Dusty
passages run north."""),

    'nerve': Location("Corridor of Nerve", """This hallway has no walls, just open air and a drop off with 
no visible bottom. There is a doorway to the south."""),

    'grit':   Location("Chamber of Grit", """The smell of sweat fills the air and the ground is covered in sand. 
Footprints dot the sand in a frantic mess. There is a doorway to the east."""),

   'gate':   Location("Gate", """There is a flat white wall to the north with colored slots, big enough for a card, cut into into.
There is a doorway to the west."""),

    'treasure': Location("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link locations together

# atrium
location['atrium'].n_to = location['beauty']
location['atrium'].s_to = location['nerve']
location['atrium'].w_to = location['grit']
location['atrium'].e_to = location['gate']

# nerve
location['beauty'].s_to = location['atrium']

# nerve
location['nerve'].n_to = location['atrium']

# grit
location['grit'].e_to = location['atrium']

# gate
location['gate'].w_to = location['atrium']

location['treasure'].n_to = location['gate']

# Declare all items
item = {
    'red_card_1':  Card("Red", '''A thin red card with a scrap of beige tape peeling off on one side. Labeled "1".'''),
    'blue_card_1': Card("Blue", '''A bulky blue card with a blackened corner that suggests a recent encounter with 
fire.'''),
    'atrium_statues': Feature("statues", "Marble", '''Each statue in the room depicts a famous spartan. There are four. You read
the following names and epithets, one on each statue: 

Queen Gorgo (wits), Leonidas I (nerve), Helen of Troy (beauty), Xanthippus(grit)''')
}

# Link items to locations
location['atrium'].items = [item['atrium_statues']]
location['beauty'].items = [item['red_card_1']]
location['nerve'].items = [item['blue_card_1']]

# Declare Player
player = Player('Chosen One', location['atrium'])

# Global Methods

# Clear Screen
clear = lambda: os.system('cls')
clear()

# Enter to Continue
def enter_to_continue():
    input('--\nPress Enter to Continue...')

# Movement Error Message
def invalid_direction():
    print(chr(27) + "[2J") # Scroll screen down so that the next loop begins at the top of the screen.
    print('You are unable to see a way to move in that direction!')
    enter_to_continue()


# Command Groups:

# System
quit_command = ("q", "quit", "esc", "end") # Quit Commands
help_command = ("h", "help")

# Movement
move_command = ("walk", "go", "move", "travel", "venture", "proceed", "n", "s", "e", "w") # Movement Commands
move_direction = { # Movement Objects
    'north': ("northward", "north", "n"),
    'south': ("southward", "south", "s"),
    'east': ("eastward", "east", "e"),
    'west': ("westward", "west", "w")
}

# Items
get_item_command = ("get", "take", "pickup") # Get Item Commands
drop_item_command = ("drop", "discard") # Drop Item Commands
check_item_command = ("check", "examine", "inspect")

# Player
inventory_command = ("i", "inventory", "bag")

#
# Intro
#

print(r'''   
             /\    
            /  \   
           / /\ \  
          / /  \ \ 
         /_/    \_\

Welcome to Lambda Adventure! 
============================
''')

player_name = input('Please enter your name: ')
player.name = player_name

print(chr(27) + "[2J") # Scroll screen down so that the next loop begins at the top of the screen.

print(r'''   
             /\    
            /  \   
           / /\ \  
          / /  \ \ 
         /_/    \_\

Welcome to Lambda Adventure! 
============================

Last night you struggled to fall asleep.

But at the exact moment when you did, after watching the minutes on your clock
buzz by, an impression was left in the back of your eyes like a bright white
light, in the shape of a Greek Lambda...

When you awake, you will be in your bed no longer...

Your adventure will have begun...

You will be able to enter commands below. 

Tip: After you awake, enter 'q' to sleep forever (quit) or 'h' for some help.''')
input('--\nPress Enter to Wake Up...')
print(chr(27) + "[2J") # Scroll screen down so that the next loop begins at the top of the screen.

#
# Main
#

# Make a new player object that is currently in the 'outside' location.

# Write a loop that:
#
# * Prints the current location name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the location there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:

    # Location Name
    print(f'You find yourself at the {player.location.name}. \n')

    # Location Description
    location_description_wrapper = textwrap.TextWrapper(80)
    current_location_description = location_description_wrapper.wrap(player.location.description)
    for line in current_location_description:
        print(line)
    
    # Location Items
    if (len(player.location.items) > 0):
        print("\nYou see the following: ")
        for item in player.location.items:
            print(item.name)

    # Main Input + Convert to Lowercase and a List
    print('________________________________________________________________________________')
    command = input("Enter Command Here: ")
    command = command.lower().split(" ", 1)

    # Define Command Action
    command_action = command[0]

    # Define Command Object and Object Type and Descriptor
    if len(command) == 1:
        command_object = ""
    else:
        command_object = command[1]
        
        # Check if command_object is more than one word
        command_object_item = command_object.split(" ")

        # If command_object is one word, assume that word is the item type
        if len(command_object_item) == 1:
            item_type = command_object_item[0]
            item_descriptor = None

        # If command_object is more than one word, assume that the second 
        # word is the item type and the first word is a descriptor
        else:
            item_type = command_object_item[1]
            item_descriptor = command_object_item[0]
    

    #
    # Commands --------------------------------------------------------------------------------
    #

    #
    # System Commands
    #

    # Commands to Quit Game
    if command_action in quit_command:
        break

    # Commands for Help
    elif command_action in help_command:
        print(f'''
Are you lost, {player.name}?

Commands are made of two words: an action, and an object.
- The action is what you want to do. 
- The object, which is sometimes optional, is what the action should 
be done to.
    
i.e. search room
- 'search' is the action, and 'room' is the object.

Alternatively, this could be written as 'search' because the object 
is sometimes optional.''')
        enter_to_continue()
        print(chr(27) + "[2J") # Scroll screen down so that the next loop begins at the top of the screen.

    #
    # Movement Commands
    #

    # Check if Command Was a Movement Command
    elif command_action in move_command:
        
        # Check Movement Type and Whether Movement is Valid
        
        # North
        if command_action == "n" or command_object in move_direction['north']:
            if hasattr(player.location, 'n_to'):
                player.location = player.location.n_to
            else:
                invalid_direction()

        # South 
        elif command_action == "s" or command_object in move_direction['south']:
            if hasattr(player.location, 's_to'):
                player.location = player.location.s_to
            else:
                invalid_direction()

        # East
        elif command_action == "e" or command_object in move_direction['east']:
            if hasattr(player.location, 'e_to'):
                player.location = player.location.e_to
            else:
                invalid_direction()

        # West
        elif command_action == "w" or command_object in move_direction['west']:
            if hasattr(player.location, 'w_to'):
                player.location = player.location.w_to
            else:
                invalid_direction()
        
        else:
            invalid_direction()

    #
    # Item Commands
    #

    # Get Item
    elif command_action in get_item_command:
        
        # Get a list of all items with a type that matches the provided type
        location_item_type = [item for item in player.location.items if item.type == item_type]

        if len(location_item_type) == 0:
            print(f"\n{command_object.capitalize()} does not exist at your location.")
            enter_to_continue()
        
        elif (location_item_type[0].can_get == True):
            # If there is only one item of the provided type, Get Item
            if len(location_item_type) == 1:
                location_item_type[0].on_get(player)
                enter_to_continue()

            else: # If there is more than one item of the provided type...

                # If player did not provide a descriptor, prompt player to choose one
                if item_descriptor == None:
                    print(f'''\nWhat type of {item_type}?''')
                    for item in location_item_type:
                        print(item.descriptor)
                    item_descriptor = input('Enter one of the above options: ')

                # Get item with the provided descriptor if it exists in the location
                if item_descriptor in [item.descriptor.lower() for item in location_item_type]:
                    for index, item in enumerate(location_item_type):
                        if item.descriptor.lower() == item_descriptor:
                            location_item_type[index].on_get(player)
                    enter_to_continue()
                else:
                    print(f'Unable to pick up {item_descriptor} {item_type}.')
        else:
            print(f"You can't pick up {item_type}!")
            enter_to_continue()

    # Drop Item
    elif command_action in drop_item_command:
        
        # Get a list of all items with a type that matches the provided type
        player_item_type = [item for item in player.items if item.type == item_type]
        
        if len(player_item_type) == 0:
            print(f"\n{command_object.capitalize()} does not exist in your inventory.")
            enter_to_continue()

        # If there is only one item of the provided type, Drop Item
        elif len(player_item_type) == 1:
            player_item_type[0].on_drop(player)
            enter_to_continue()

        else: # If there is more than one item of the provided type...

            # If player did not provide a descriptor, prompt player to choose one
            if item_descriptor == None:
                print(f'''\nWhat type of {item_type}?''')
                for item in player_item_type:
                    print(item.descriptor)
                item_descriptor = input('Enter one of the above options: ')

            # Drop item with the provided descriptor if it exists in player inventory
            if item_descriptor in [item.descriptor.lower() for item in player_item_type]:
                for index, item in enumerate(player_item_type):
                    if item.descriptor.lower() == item_descriptor:
                        player_item_type[index].on_drop(player)
                enter_to_continue()
            else:
                print(f'\nUnable to drop {item_descriptor} {item_type}.')
    
    # Check Item
    elif command_action in check_item_command:
        
        # Get a list of all items in player inventory and location with a type that 
        # matches the provided type
        player_location_item_type = [item for item in player.items if item.type == item_type] + [item for item in player.location.items if item.type == item_type]
        
        if len(player_location_item_type) == 0:
            print(f"\n{command_object.capitalize()} must be nearby for you to inspect it!")
            enter_to_continue()

        # If there is only one item of the provided type, Check Item
        elif len(player_location_item_type) == 1:
            player_location_item_type[0].on_check(player)
            enter_to_continue()

        else: # If there is more than one item of the provided type...

            # If player did not provide a descriptor, prompt player to choose one
            if item_descriptor == None:
                print(f'''\nWhat type of {item_type}?''')
                for item in player_location_item_type:
                    print(item.descriptor)
                item_descriptor = input('Enter one of the above options: ')

            # Check item with the provided descriptor if it exists in player inventory
            if item_descriptor in [item.descriptor.lower() for item in player_location_item_type]:
                for index, item in enumerate(player_location_item_type):
                    if item.descriptor.lower() == item_descriptor:
                        player_location_item_type[index].on_check(player)
                enter_to_continue()
            else:
                print(f'\nUnable to check {item_descriptor} {item_type}.')

    #
    # Player
    #

    # Inventory
    elif command_action in inventory_command:
        player.inventory()
        enter_to_continue()

    elif command_action == "search" or (command_action == "search" and command_object == "room"):
        print("You don't see anything other than the obvious!")
        enter_to_continue()
    
    else:
        print("\nThis isn't the time for that kind of nonsense!")
        enter_to_continue()

    print(chr(27) + "[2J") # Scroll screen down so that the next loop begins at the top of the screen.