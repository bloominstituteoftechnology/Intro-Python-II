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

# Declare Items
axe = Item("axe", "It glows and radiates heat to the enemy hearts")
shield = Item("shield", "Crafted from Ancient Olympian God Zeus")
armor = Item("armor", "Impenetrable armor crafted from Olympian God Poseidon ")

# A room to place items
room['overlook'].items = [shield]
room['foyer'].items = [axe]
room['narrow'].items = [armor]
#
# Main
#
name_player = input("Welcome adventurer. Your name is?:")
# Make a new player object that is currently in the 'outside' room.
player1 = Player(name_player, room['outside'])

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

def getitem():
    item_choice = input("What do you want to do? Ex: get axe: ").split()
    # check if item choice 2 is equal to one of the item.names in the players current room's items.
    for i in player1.current_room.items:
        if item_choice[1] == i.name and item_choice[0] == "get":
            player1.items.append(i)
            player1.current_room.items.remove(i)
        else:
            print("Option not available.")

def update_room():
    print(player1.current_room)
    if len(player1.current_room.items) > 0:
        getitem()
        print(player1)

def invalid_direction():
    print("Cannot move in that direction.")
    
player_choice = ''
while player_choice != 'q':
    print(f"Current location: { player1.current_room.name }")
    print(player1.current_room.description)
    player_choice = input("Choose a direction to move.  Enter n, s, e, or w: ")
    if player_choice == 'n':
        if  player1.current_room.n_to is not None:
            player1.current_room = player1.current_room.n_to
            update_room()
        else:
            invalid_direction()
    elif player_choice == 's':
        if  player1.current_room.s_to is not None:
            player1.current_room = player1.current_room.s_to
            update_room()
        else:
            invalid_direction()
    elif player_choice == 'e':
        if  player1.current_room.e_to is not None:
            player1.current_room = player1.current_room.e_to
            update_room()
        else:
            invalid_direction()
    elif player_choice == 'w':
        if  player1.current_room.w_to is not None:
            player1.current_room = player1.current_room.w_to
            update_room()
        else:
            invalid_direction()
    elif player_choice == 'q':
        print("Not a valid direction.")
    else:
        print("Thanks for playing. Exiting game.")