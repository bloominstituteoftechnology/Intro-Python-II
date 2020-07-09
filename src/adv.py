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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newPlayer = Player('Ben', room['outside']) 

def check_move(move):
    current = newPlayer.room
    if current.__dict__[f'{move}_to'] == None:
        print("\n**There's nothing there!**")
    else:
        newPlayer.room = current.__dict__[f'{move}_to']

while True:
    current = newPlayer.room
    print(current)
    movement_choice = ['n', 'e', 's', 'w']
    print(
        f"\n****Hello {newPlayer.name}. your current location is {current}****")
    choice = input(
        f"what would you like to do? Move: [n, e, s, w]  q(quit): ")
    if choice in movement_choice:
        check_move(choice)
    elif choice == "q":
        print("Thanks for playing!")
        exit()
    else:
        print("\nForbidden movement input.")

# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
