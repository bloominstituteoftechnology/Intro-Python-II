from room import Room
from player import Player
from item import Item
import random

# Declare all the items

powerUps = [
    ['sword', 'sharp sword'],
    ['lantern', 'light source'],
    ['rock', 'break stuff'],
    ['chest', 'keep your gold'],
    ['bucket', 'get water'],
    ['rope', 'tie a knot']] 
items = [Item(item[0], item[1]) for item in powerUps]
actions = {'take':'took', 'drop':'dropped'}

# Declare all the rooms
[print(n) for n in items]
print('\n')
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", None, [items[random.randint(0,5)], items[random.randint(0,5)]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", None, [items[random.randint(0,5)], items[random.randint(0,5)]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", None, [items[random.randint(0,5)], items[random.randint(0,5)]]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", None, [items[random.randint(0,5)], items[random.randint(0,5)]]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", None, [items[random.randint(0,5)], items[random.randint(0,5)]]),
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
# Main - Developed by Ben Hakes
#

# Overlook       Treasure
#   ||              ||
# Foyer     ===   Narrow
#   ||
# Outside               

# Make a new player object that is currently in the 'outside' room.
player_name = str(input("Please enter the name of player\n"))
player = Player(player_name, room['outside'])
possibleMoves = {"n", "s", "e", "w"}
directionPrompt = f'Press a cardinal direction key [n],[s],[e],[w] to move, [i] to see your inventory, or [q] to quit.'
takePickupPrompt = f'Enter [take] [item_name] or [drop] [item_name] to add or remove an item from the player\'s items.'

# Write a loop that:
cmd = "c"

# def get_room_with_ifs(cmd, room: Room):
#     # get the string input
#     # turn that into a class property
#     # 'n' -> current_room.n_to
#     if cmd == "n":
#         return current_room.n_to
#     elif cmd == "s":
#         return current_room.s_to
#     elif cmd == "e":
#         return current_room.e_to
#     else:
#         return current_room.w_to


def get_room(cmd: str, room: Room) -> Room:
    # create concatenated string of direction + _to
    moving = cmd + '_to'
    return getattr(room, moving, None)

# gameplay loop
# If the user enters "q", quit the game.
while not cmd == "q":

    # Prints the current room name
    # Prints the current description (the textwrap module might be useful here).
    print("\n<****--------****>")
    print(f'You are in the {player.room.name} room, Sir {player.name}.')
    print(f'{player.room.description}.\n')
    print(f'Your inventory includes:')
    [print(n) for n in player.items]
    print(f'\nItems in the room include:')
    [print(n) for n in player.room.items]
    print("<****--------****>\n")

    # Waits for user input and decides what to do.
    room_items = [n.name for n in player.room.items]
    player_items = [n.name for n in player.items]
    cmd = str(input(f'{directionPrompt}\n{takePickupPrompt}\n'))
    
    cmd_strs = cmd.split()


    if len(cmd_strs) == 2:
        if cmd_strs[0] in actions.keys():
            if cmd_strs[1] in room_items or cmd_strs[0] == 'drop' and cmd_strs[1] in player_items:
                itemToSend = [n for n in items if n.name == cmd_strs[1]]
                player.on_action(cmd_strs[0], itemToSend[0])
                player.room.on_action(cmd_strs[0], itemToSend[0])
            else:
                print("\n*****Error*****\nThat item is not in this room.\n*****Error*****\n")
        else:
            print("That is not an action.")
    else:
        if cmd == "q":
            break
        elif cmd == "i":
            player.print_inventory()
        elif cmd in possibleMoves:

            # If the user enters a cardinal direction, attempt to move to the room there.
            new_room = get_room(cmd, player.room)
            if new_room is not None:
                player.move_player(new_room)
            else:
                print("\n*****Error*****\nThere is no room in that direction. Try again.\n*****Error*****")
        else:
            # Print an error message if the movement isn't allowed.
            print("\n***** ERROR *****")
            print("The key you entered is not an allowed move.")
            print("Please try again with an allowed move [n,s,e,w].")
            print("***** ERROR *****\n")
            
            enteredValue = str(input(f'{directionPrompt}\n'))
  
