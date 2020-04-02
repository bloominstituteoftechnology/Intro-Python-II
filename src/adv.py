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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

"""
  | V | T
  | F _ N
  | O |
"""

fork = Item("Fork", "An eating utensil")
axe = Item("Axe", "A beat up old battle axe")
torch = Item("Torch", "An unlit torch")
match = Item("Match", "A match for starting a fire")

room['outside'].items = []
room['foyer'].items = [torch]
room['overlook'].items = [match]
room['narrow'].items = [axe, fork]
room['treasure'].items = []

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_1 = Player(room["outside"])

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
def get_action(player):
    action = input("What would you like to do? (n, s, e, w or q to quit) ").lower()
    while action != "q" and action != "quit":
        if len(action.split(" ")) > 1:
            do(action, player)
        else:
            move(player, action)
        print(player.current_room)
        action = input("What would you like to do? (n, s, e, w or q to quit) ").lower()
    print("Bye!")

def move(player, direction_choice):
    if direction_choice == "n":
        player.try_north()
    elif direction_choice == "s":
        player.try_south()
    elif direction_choice == "e":
        player.try_east()
    elif direction_choice == "w":
        player.try_west()
    elif direction_choice == "i" or direction_choice == "inventory":
        player.print_items()
    else:
        print("I don't understand. Please try again.")

def do(action, player):

    if "take" in action or "get" in action:
        item_names = [item.name.upper() for item in player.current_room.items]
        if action.split()[1].upper() in item_names:
            item = [item for item in player.current_room.items if item.name.upper() == action.split()[1].upper()]
        player.get_item(item[0])
    elif "drop" in action:
        item_names = [item.name.upper() for item in player.items]
        if action.split()[1].upper() in item_names:
            item = [item for item in player.items if item.name.upper() == action.split()[1].upper()]
        player.drop_item(item[0])
    elif "move" in action or "go" in action:
        direction = action.split()[-1]
        move(player, direction)
    else:
        move(player, action)

get_action(player_1)