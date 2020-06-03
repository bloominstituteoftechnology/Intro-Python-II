from room import Room
from player import Player
from item import Item
from os import system, name
# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", "Dim light filters in from the south. Dusty"
                           " passages run north and east."),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling "
                                       "into the darkness. Ahead to the north, a light flickers in "
                                       "the distance, but there is no way across the chasm."),

    'narrow': Room("Narrow Passage", "The narrow passage bends here from west "
                                     "to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure "
                                         "chamber! Sadly, it has already been completely emptied by "
                                         "earlier adventurers. The only exit is to the south."),
}

# This allows me to 1. Make use of auto complete and 2. Avoid potential typo-related bugs
out = 'outside'
foy = 'foyer'
over = 'overlook'
nar = 'narrow'
trea = 'treasure'

# Easy formatting
br = '----------------------------'

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# One easy function to display a "Map" to the user
def showDirections(current):
    north = "North: " + current.n_to.name if current.n_to != None else "There's no path North"
    east = "East: " + current.e_to.name if current.e_to != None else "There's no path East"
    sout = "South: " + current.s_to.name if current.s_to != None else "There's no path South"
    west = "West: " + current.w_to.name if current.w_to != None else "There's no path West"
    print()
    print(north)
    print(east)
    print(sout)
    print(west)
    print()

# This method will clear the terminal so the game remains legible
def clear():
    # For Windows
    if name == 'nt':
        system('cls')
    # For Mac
    else:
        system('clear')

# Method to allow for however many inputs the user may want to provide
def get_input():
    pick = input("Action to take:").split()
    if len(pick) <= 0 or len(pick) > 2:
        return "-1"
    else:
        s1 = f"{str(pick[0]).lower()}"
        s2 = ", " if len(pick) < 2 else "," + str(pick[1]).lower()
        return s1 + s2

# Define new player
player1 = Player("Hector", room[out])

# Add item to entrance
pot = Item('HPPOT', 'HP Potion')
room[out].add_item(pot)


while True:
    # print(br)
    clear()
    print(br)
    print(f"Info:")
    print(f"\tCurrent room: \t{player1.current_room.name}")
    print(f"\t\t{player1.current_room.description}")
    player1.current_room.items_in_room()
    print(br)

    userSaid = get_input()
    choice = userSaid.split(',')[0].lower()

    if choice == "n":
        player1.current_room = player1.current_room.n_to

    elif choice == "e":
        player1.current_room = player1.current_room.e_to

    elif choice == "s":
        player1.current_room = player1.current_room.s_to

    elif choice == "w":
        player1.current_room = player1.current_room.w_to

    elif choice == "m":
        showDirections(player1.current_room)
        if input("[Enter] to close map\t"): break

    elif choice == "i":
        player1.show_inventory()

    elif choice == "q":
        break

    elif choice.startswith("get") or choice.startswith("take"):
        picked = int(userSaid.split(',')[1]) if userSaid.split(',')[1].isdigit() else 0
        length = len(player1.current_room.items)
        if picked > 0 and picked <= len(player1.current_room.items):
            player1.take(player1.current_room.pickup_item(picked))
            print()
            player1.show_inventory()
            if input("\n[Enter] to close Inventory\t"): continue
        else:
            input('Invalid Input... Enter to continue ')
            continue

    else:
        input("Invalid input... Enter to continue")


