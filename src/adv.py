from room import Room
from player import Player
from item import Item
# Declare all the rooms

item = [
    Item("radio", ""),
    Item("old battery", "damn thing must have fell out the radio"),
    Item("Knife", "better be careful"),
    Item("key", "huh might need that later"),
    Item("paper", "It Reads: Those who enter do not leave")
]


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [
                        item[1]
                     ]),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",

                     [
                         item[3],
                         item[4]
                     ]),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     [
                         item[2]
                     ]),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     [
                         item[0]
                     ]),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     [
                         item[4]
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
player = Player("Muamer", room ['outside'], [item[0]])

def show_welcome_message():
    welcome_message = "\nWelcome to the game!\n"
    print(welcome_message)
    print(f"{player.player_name}, you are currently at the {player.current_room.name}, and we need you to go to th- chhhh your radio loses contact...\nyour items: {player.inventory[0].item_name} and your will to find a way home.\n")
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
    "inventory": "inventory",
    "search": "search"
}

show_welcome_message()
while True:
    current_room = player.current_room
    move = input("\nType N, S, E, or W to move\nType search to search a room\nType get item name to pick up item\nType drop item name to drop an item >>>")
    
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
    #         print("\nthe path is blocked by rubble! Try again.\n")
    # elif move == "e":
    #     if current_room.e_to is not None:
    #         player.current_room = current_room.e_to
    #     else:
    #         print("\nYou fell thew the floor! Try again.\n")
    # elif move == "w":
    #     if current_room.w_to is not None:
    #         player.current_room = current_room.w_to
    #     else:
    #         print("\nYou went through an illusion!  Try again.\n")
   
    elif "get" in move: 
        item = move[4:]

        for x in range(len(current_room.items)):
            if item == current_room.items[x].item_name:
                player.inventory.append(current_room.items[x])
                print(f"\nyou have picked up {current_room.items[x]}")
                del current_room.items[x]
                break
            else:
                print("\nItem not in room")
        
        if len(current_room.items) == 0:
            print("\nItem not in room")
    elif "drop" in move:
        item = move[5:]

        for x in range(len(player.inventory)):
            if item == player.inventory[x].item_name:
                current_room.items.append(player.inventory[x])
                print(f"\nyou have dropped {player.inventory[x]}")
                del player.inventory[x]
                break
            else:
                print("Don't have item to drop")

    elif move == "i" or move == "inventory":
        for x in range(len(player.inventory)):
            print(f"\n{player.inventory[x]}")

    elif move == "search":
        for x in range(len(current_room.items)):
            print(f"\nYou Found:\n{current_room.items[x]}")
               
    elif move == "q":
        print("\nGame has quit\n")
        exit()