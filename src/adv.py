from room import Room
from item import Item
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", "Dim light filters in from the south.\n"
                              "Dusty passages run north and east.",
                     [Item('map', 'Map to another treasure chest in a different location')]),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness.\n"
                                       "Ahead to the north, a light flickers in the distance,\n"
                                       "but there is no way across the chasm.",
                     [Item('sword', "And old rusty blade, it's been here a while")]),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north.\n"
                                       "The smell of gold permeates the air.",
                     [Item('key', "Old rusty key, it has an inscription on it but it's worn off")]),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber!\n"
                                         "Sadly, it has already been completely emptied by earlier adventurers.\n"
                                         "The only exit is to the south.",
                     [Item('skeleton', "Only dusty bones remain in this room.")]),
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
player = Player('Chad', room['outside'])

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


def perform_move(command):
    if command in ['q', 'quit', 'exit']:
        print("\nThanks for playing!\n")
        global running
        running = False
    elif command in ['?', 'help']:
        print("\nValid commands: ['n': North, 's': South, 'e': East,\n"
              "'w': West, 'q, quit, exit': Quit, '?, help': Help]\n")
    else:
        next_room = player.move_to(command)
        if next_room is None:
            print("\nNo room in this direction.\n")
        elif next_room is room['treasure']:
            list = [i.name for i in player.items]
            if 'key' not in list:
                print("You're missing the key to get in. Please look for a key and come back.")
            else:
                player.current_room = next_room
        else:
            player.current_room = next_room


def perform_action(command):
    if command[0] in ['get', 'take', 'pickup']:
        for item in player.current_room.items:
            if item.name == command[1]:
                player.items.append(item)
                player.current_room.items.remove(item)


running = True

while running:
    print(f"\n{player.current_room.name}\n")
    print(f"{player.current_room.description}\n")
    if len(player.current_room.items) > 0:
        for item in player.current_room.items:
            print(f"Items: {item.name}, {item.description}")

    command = input('\nWhere do you want to go? Enter (n, s, e, or w; q to quit): ').split(' ')
    if len(command) > 1:
        perform_action(command)
        continue
    else:
        perform_move(command[0])
