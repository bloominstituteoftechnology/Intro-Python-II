from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Rock", "medium sized rock"), Item("Stick", "fallen tree twig")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Sword", "sword of iron")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Cape", "raggedy cape"), Item("Eggs", "3 eggs inside a bird nest")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Boots", "someone's old shoes"), Item("Bones", "animal remais")]),

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
player_one = Player('Zelda', room['outside'])

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
directions = ['n', 'e', 's', 'w']
get_commands = ['take', 'get']
drop_command = ['drop']
inventory_command = ['i', 'inventory']

def text_adventure_game():
    active_game = True
    while active_game == True:
        print(f'\n{"*" * 58}')
        player_one.room.print_room_info()
        player_one.room.room_items()
        selection = input(
            f"\nWhat would you like to do? Or press 'q' to quit ")
        command = selection.split(' ', 1)
        if command[0].lower() in get_commands:
            player_one.on_take(command[0], command[1])
        elif command[0].lower() in drop_command:
            player_one.on_drop(command[0], command[1])
        elif selection in inventory_command:
            player_one.check_inventory()  
        elif selection in directions:
            player_one.move_to(selection)
        elif selection == 'q':
            print(f'\n{"*" * 58}\n')
            print(f"Game Over!".center(58, ' '))
            print(f'\n{"*" * 58}\n')
            active_game = False

text_adventure_game()
