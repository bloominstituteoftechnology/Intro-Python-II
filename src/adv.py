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


# Declaring Items

items = {
    'boots': Item("Boots", "Perfect for muddy adventures!"),
    'lantern': Item("Lantern", "Perfect for lighting up dark places!"),
    'sword': Item("Sword", "Perfect for protecting yourself!")
}
room['outside'].add_items(items['boots'])
room['foyer'].add_items(items['sword'])
room['overlook'].add_items(items['lantern'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input('What is your name, Adventurer? ')
player = Player(name, room['outside'])

print(f'Welcome {name}. Begin your adventure from {player.current_room} \n')
print(room['outside'].show_items())

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

while True:
    current_room = player.current_room
    print(f"{current_room.description}")
    nextMove = input("Enter your next move n, s, e, w, t to pick up item, d to drop item, i to see iventory, or q for quit: ")

    # Setting it up for the user to make moves or quit
    if nextMove == "n":
        if current_room.n_to is not None:
            player.current_room = current_room.n_to
            print("You chose to go North!")
        else:
            print("There is not room that way; please try again!")
    
    elif nextMove == "s":
        if current_room.s_to is not None:
            player.current_room = current_room.s_to
            print("You chose to go South!")
        else:
            print("There is not room that way; please try again!")
    
    elif nextMove == "e":
        if current_room.e_to is not None:
            player.current_room = current_room.e_to
            print("You chose to go East!")
        else:
            print("There is not room that way; please try again!")
    
    elif nextMove == "w":
        if current_room.w_to is not None:
            player.current_room = current_room.w_to
            print("You chose to go West!")
        else:
            print("There is not room that way; please try again!")
    # Picking up an item
    elif nextMove == "t":
        for item in player.current_room.items:
            print(player.pickupItem(item))

        print(player.items)
    # Dropping the item
    elif nextMove == "d":
        for item in player.items:
            if item.name == item:
                player.dropItem(item)
    # To see what items the player has            
    elif nextMove == "i":
        print(player.show_inventory())

    # Adding the ability to quit
    elif nextMove == "q":
        print("Thank you for playing! See you soon!")
        exit()
    # Adding an error message
    else:
        print("Please enter n, s, e, w to make a move, t to pick up an item, d to drop an item or i to see iventory or q to quit!")
