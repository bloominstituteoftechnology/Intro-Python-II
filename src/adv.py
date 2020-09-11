from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["Torch"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["Coins", "Map", "Shield"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["Sword", "Coins", "Potion"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["Compass"]),

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

player = Player("Stephen The Magnificently Benevolent", room['outside'])

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

active = True

print(f"Welcome to {player.name} to the ADVENTURE GAAAAAAAAME! \n\nYou have been chosen to complete a quest of epic proportions, also known as an EPIC QUEST!\n\n{player.current_room.description}.\n\nStep to the north to enter the cave!\n\n***Press N to move North")
print(player.current_room.name)
while player.current_room.name is "Outside Cave Entrance":
    first_move = input()
    if first_move is "N":
        player.current_room = player.current_room.n_to
    else:
        "I'm sorry that move isn't allowed!"

print(f'{player.name} steps north, into the {player.current_room.name}....\n{player.current_room.description}\n')

print("If you're ever too scared to go on, enter q in any prompt! Bwahahahaha!!!!!")


while active is True:
    print(f"\nYou Are Here: {player.current_room.name}\n{player.current_room.description}\n")
    if len(player.current_room.items) > 0:
        print("There are items for plundering here!\n")
    print(f"What's your next move, {player.name}???")
    choice = input("Please choose 1 for move or 2 for change inventory:  ")
    if choice == "1":
        move = input("Please choose a direction. N, S, E, or W:  ")
        if move == "N":
            if hasattr(player.current_room, 'n_to'):
                player.current_room = player.current_room.n_to
            else:
                print("I'm sorry that move isn't allowed!\n")
        elif move == "S":
            if hasattr(player.current_room, 's_to'):
                player.current_room = player.current_room.s_to
            else:
                print("I'm sorry that move isn't allowed!\n")
        elif move == "E":
            if hasattr(player.current_room, 'e_to'):
                player.current_room = player.current_room.e_to
            else:
                print("I'm sorry that move isn't allowed!\n")
        elif move == "W":
            if hasattr(player.current_room, 'w_to'):
                player.current_room = player.current_room.w_to
            else:
                print("I'm sorry that move isn't allowed!\n")
        else:
            print("I'm sorry that's not a valid move! Try again!\n")
    if choice == "2":
        print(f"\n{player.name}'s current inventory:")
        print(*player.inventory, sep=', ')
        print(f"\nThese are the items in {player.current_room.name}:")
        print(*player.current_room.items, sep=', ')
        action, obj = input("\nWhat do you want to do? 'Take Coins' or 'Drop Sword':  ").split()
        if action == "Take":
            player.inventory.append(obj)
            player.current_room.items.remove(obj)
        if action == "Drop":
            print("\nWhich item do you want to discard?")
            print(player.inventory)
            player.inventory.remove(obj)
            player.current_room.items.append(obj)

            