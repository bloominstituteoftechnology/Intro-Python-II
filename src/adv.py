from room import Room
from player import Player

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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Items in rooms

room['foyer'].items = 'dust'
room['overlook'].items = 'sword'

#
# Main

# Make a new player object that is currently in the 'outside' room.

player = Player(input("Welcome! Please enter your name: "), room['outside'], [])


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

def pick_up_item(decision):
    if decision == 'y':
        player.inventory.append(player.current_room.items)
        player.current_room.items = None

def drop_item():
    drop = input("Would you like to drop any items from your inventory?(input item name to drop)")
    player.inventory.remove(drop)


def move_player(direction):
    error = "\nThere is no room here, please try again\n"
    if direction == 'n':
        if player.current_room.n_to is not None:
            player.current_room = player.current_room.n_to
        else:
            print(error)
    elif direction == 's':
        if player.current_room.s_to is not None:
            player.current_room = player.current_room.s_to
        else:
            print(error)
    elif direction == 'e':
        if player.current_room.e_to is not None:
            player.current_room = player.current_room.e_to
        else:
            print(error)
    elif direction == 'w':
        if player.current_room.w_to is not None:
            player.current_room = player.current_room.w_to
        else:
            print(error)
    elif direction == 'i':
       if player.inventory is not None:
           drop_item()

    

while True:
    print(f'Current Room: {player.current_room.name}\n \n{player.current_room.description}\n\n')
    print(f"Inventory: {player.inventory}")
    move = input("Move North(n), South(s), East(e), or West(w) \nItem Action(i) \nQuit Game(q)")
    move_player(move)
    if move == 'q':
        break
    elif player.current_room is not None:
        if player.current_room.items:
            pick_up = input("There's an item here, would you like to pick it up? (y/n)")
            current_item = player.current_room.items
            pick_up_item(pick_up)
            print(f"~~~~~{player.name}, you've picked up {current_item}~~~~~")
        continue
    else:
        print("This room does not exist. Please try again.")


