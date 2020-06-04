from room import Room
from player import Player
from item import Item

# Items

item = [
    Item('Badass Sword of Unity', 'This sword contains a lot of power, use it wisely'),
    Item('Killer Mace', 'This mace can deal a lot of damage, watch out!'),
    Item('Strong Shield', 'Ths shield will help you in combat!'),
    Item('Potion of Healthyness', 'This is just cocaine, pure Columbian cocaine.')
]

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [item[0],
                      item[1]
                      ]),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                    [item[2],
                     item[3]
                     ]),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     [item[3],
                      item[0]
                      ]),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     [item[1],
                      item[3]
                      ]),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     [item[1],
                      item[2]
                      ]),
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

def show_welcome_message():
    welcome_message = "Welcome to the game!"
    print(welcome_message)

show_welcome_message()

player = Player("Not Steve", room['outside'], [item[0]])
print(f"Your player: {player.player_name}, currently located at: {player.current_room.name}, Inside your inventory currently is: {player.inventory[0].item_name}")

def get_user_choice():
    choice = input("[n] north [s] south [e] east [w] west [q] quit\n")
    return choice_options[str(choice)]

choice_options = {
    "n": "north",
    "s": "south",
    "e": "east",
    "w": "west",
    "q": "quit",
    "get": "get item",
    "drop": "drop item",
    "i": "inventory",
    "inventory": "inventory"
}


while True:
    current_room = player.current_room
    # print(f"You are currently in {current_room.name}")
    # print(f"{current_room.description}")
    move = input("Select N, S, E, or W to move to the next room!\nType search to search a room!\nType get then the item name to get the item\nType drop then the item name to drop the item >>> ")

    if move in ["n", "s", "e", "w"]:
        player.travel(move)

    # if move == "n":
    #     if current_room.n_to is not None:
    #         player.current_room = current_room.n_to
    #     else:
    #         print("You hit a dead end!  Try again.")
    # elif move == "s":
    #     if current_room.s_to is not None:
    #         player.current_room = current_room.s_to
    #     else:
    #         print("You hit a dead end!  Try again.")
    # elif move == "e":
    #     if current_room.e_to is not None:
    #         player.current_room = current_room.e_to
    #     else:
    #         print("You hit a dead end!  Try again.")
    # elif move == "w":
    #     if current_room.w_to is not None:
    #         player.current_room = current_room.w_to
    #     else:
    #         print("You hit a dead end!  Try again.")

    elif "get" in move:
        item = move[4:]

        for x in range(len(current_room.items)):
            if item == current_room.items[x].item_name:
                player.inventory.append(current_room.items[x])
                print(f"You have picked up {current_room.items[x]}")
                del current_room.items[x]
                break
            else:
                print("Item not in room")

        if len(current_room.items) == 0:
            print("Item not in the room")

    elif "drop" in move:
        item = move[5:]

        for x in range(len(player.inventory)):
            if item == player.inventory[x].item_name:
                current_room.items.append(player.inventory[x])
                print(f"You have dropped {player.inventory[x]}")
                del player.inventoryp[x]
                break
            else:
                print("Don't have that item to drop!")

    elif move == "i" or move == "inventory":
        for x in range(len(player.inventory)):
            print(player.inventory[x])

    elif move == "search":
        for x in range(len(current_room.items)):
            print(f"You searched and found {current_room.items[x]}")

    elif move == "q":
        print("Game has quit")
        exit()