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

#adding items to rooms
room['outside'].add_item(Item("Rock", "It's a rock. Very effective!"))
room['outside'].add_item(Item("Arrow", "It's an Arrow. You are wildly unimpressed..."))
room['foyer'].add_item(Item("Map", "It's a Map. Your thirst for knowledge has been quenched!"))
room['narrow'].add_item(Item("Potion", "It's a Potion. Magic doesn't really exist though..."))
room['overlook'].add_item(Item("Key", "It's a Key. Now if there was only a lock..."))
room['treasure'].add_item(Item("Duck", "It's a Duck. At last...all of your problems have been solved!!!"))

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

class colors:
    blink = '\033[5m'
    red = '\033[91m'
    reset = '\033[0m'

def invalidSelection( sentence = "You cannot that way! Choose a different direction."):
    print(f'{colors.red}{colors.blink}\n{sentence}{colors.reset}')

player = Player(room['outside'])

print("You are currently outside of the cave")

def item_func():
    print("Items around are:")
    for item in player.current_room.items:
        print(f"{item.name}. ({item.description})")
item_func()

def commands():
    print("\n Please choose a direction...")
    return input("[n] North  [s] South  [e] East  [w] West [Take item] take item [Drop item] drop item [i] inventory [inventory] inventory  [q] Quit\n").lower()
command = commands()

splitCommand = command.split(' ')
# print("Split: ", splitCommand, len(splitCommand))

while not command == "q":
    splitCommand = command.split(' ')
    # print("Split: ", splitCommand, len(splitCommand))

    if len(splitCommand) == 1:
        if command == "i":
            player.get_inventory()
        if command == "inventory":
            player.get_inventory()
        if command == "n":
            if player.current_room.n_to == None:
                invalidSelection()
            else: 
                player.update_room(player.current_room.n_to)
        elif command == "s":
            if player.current_room.s_to == None:
                invalidSelection()
            else:
                player.update_room(player.current_room.s_to)
        elif command == "w":
            if player.current_room.w_to == None:
                invalidSelection()
            else:
                player.update_room(player.current_room.w_to)
        elif command == "e":
            if player.current_room.e_to == None:
                invalidSelection()
            else:
                player.update_room(player.current_room.e_to)
        else:
            invalidSelection()
    elif len(splitCommand) == 2:
        if splitCommand[0].lower() == "get":
            for item in player.current_room.items:
                if item.name.lower() == splitCommand[1].lower():
                    player.current_room.items.remove(item)
                    player.inventory.append(item)
                    item.on_take(item.name.lower())
        elif splitCommand[0].lower() == "drop":
            for item in player.inventory:
                if item.name.lower() == splitCommand[1].lower():
                    player.inventory.remove(item)
                    player.current_room.items.append(item)
                    item.on_drop(item.name.lower())
    else:
        print("Try a different command")

    print(f"\nLocation: {player.current_room.name} \n{player.current_room.description}\n")
    item_func()
    command = commands()
    # command = input("[n] north  [s] south  [e] east  [w] west   [q] Quit\n")
