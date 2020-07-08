from room import Room
from player import Player
from direction import Direction
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

room['outside' ].n_to = room['foyer']
room['foyer'   ].s_to = room['outside']
room['foyer'   ].n_to = room['overlook']
room['foyer'   ].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'  ].w_to = room['foyer']
room['narrow'  ].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to room

room['foyer'].items = [
    Item("Silver Sword", "A magical sword")
]

room['overlook'].items = [
    Item("Binoculars", "Multicoated eco-glass lenses"),
    Item("Tent", "6 Person Dome Tent")
]

room['narrow'].items = [
    Item("Book", "Spell book"),
    Item("Toy Car", "Hot Wheel drag racing car"),
    Item("Laptop", "16\" MacBoo Pro")
]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

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

user_input: str = ""
verb:       str = None
object:     str = None

while verb != "Q":
    print(player.current_room)
    user_input = input("What direction do you want to go? ")

    # Break user input down into a verb and object
    first_space = user_input.find(" ")
    if first_space > 0:
        verb   = user_input[:first_space].strip().upper()
        object = user_input[first_space:].strip()
    else:
        verb   = user_input.strip().upper()
        object = None

    print(f"verb: \'{verb}\', object: \'{object}\'")

    valid_input = False 
    for direction in Direction:
        if verb == direction.value:
            player.move(direction)
            valid_input = True

    found = False 

    if valid_input == False:
        if verb == "G" or verb == "GET" or verb == "T" or verb == "TAKE":
            for item in player.current_room.items:
                if object.lower() == item.name.lower():
                    player.get(item)
                    found = True 

            if found == False: 
                print(f"I couldn't find a {object} in the {player.current_room.name}.")

            valid_input = True

        elif verb == "D" or verb == "DROP":
            for item in player.items:
                if object.lower() == item.name.lower():
                    player.drop(item)
                    found = True 

            if found == False: 
                print(f"I couldn't find a {object} in your satchel.")

            valid_input = True

        elif verb == "I" or verb == "INVENTORY":
            player.invetory()
            valid_input = True

    if verb == "H" or valid_input == False:
        print("[N]orth, [S]outh, [E]ast, [W]est, [G]et, [T]ake, [D]rop, [I]nventory, [Q]uit, [H]elp\n") 

print("Thank you for playing.")
