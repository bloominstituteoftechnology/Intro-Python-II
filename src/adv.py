from room import Room
from player import Player
from item import Item

# Declare all the rooms

words = [
    ['sword', 'pointy sword'],
    ['lantern', 'light source'],
    ['rock', 'i dunno'],
    ['chest', 'might have something in it'],
    ['bucket', 'what this?'],
    ['rope', 'this might be useful']
]

items = [Item(item[0], item[1]) for item in words]

print(items)

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage",  """The narrow passage bends here from west
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
def get_room_with_ifs(cmd, current_room):
    if cmd.lower() == 'n':
        if player.current_room.n_to is not None:
            player.current_room = player.current_room.n_to

            # Prints the current room name
            print(f"You are in the: {player.current_room.name}")
            # Prints the current description
            print(player.current_room.description)
            print(bracket)
        else:
            print("invalid direction")
    elif cmd.lower() == 's':
        if player.current_room.s_to is not None:
            player.current_room = player.current_room.s_to

            # Prints the current room name
            print(f"You are in the: {player.current_room.name}")
            # Prints the current description
            print(player.current_room.description)
            print(bracket)
        else:
            print("invalid direction")
    elif cmd.lower() == 'e':
        if player.current_room.e_to is not None:
            player.current_room = player.current_room.e_to

            # Prints the current room name
            print(f"You are in the: {player.current_room.name}")
            # Prints the current description
            print(player.current_room.description)
            print(bracket)
        else:
            print("invalid direction")
    elif cmd.lower() == 'w':
        if player.current_room.w_to is not None:
            player.current_room = player.current_room.w_to

            # Prints the current room name
            print(f"You are in the: {player.current_room.name}")
            # Prints the current description
            print(player.current_room.description)
            print(bracket)
        else:
            print("invalid direction")
    

def get_room(cmd, current_room):
    moving = cmd + '_to'
    return getattr(current_room, moving, None)

cmd = input("Hi! type your name to start the game:")
player = Player(cmd.lower(), room['outside'])
print(player)
print(f"You are in the: {player.current_room.name}")
print(player.current_room.description)
# player = Player(cmd, "outside")
print(
    "Enter a key to continue ... \n [n]orth \n [s]outh \n [e]ast \n [w]est \n or [q]uit")

directions = ['n', 's', 'w', 'e']

while  True:
    
    bracket = '\n**********************************\n'
  
    print(player.current_room)
    print(bracket)
    cmd = input("Where do you want to go? -> ")
    

    if cmd in directions:
        new_room = get_room(cmd, player.current_room)
        if new_room is not None:
            player.move_player(new_room)
        else:
            print("You can't move any farther in that diraction.")

    elif cmd.lower() == 'q':
        print('Exit the game')
        break
    else:
        print("invalid direction")


def find_item(name, current_room):
    for i in current_room.inventory:
        if i.name == name:
            return i
    return None



def move_to(direction, current_room):
    attribute = direction + '_to'

    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)
    
    else:
        print("Not a valid room")
        return current_room



