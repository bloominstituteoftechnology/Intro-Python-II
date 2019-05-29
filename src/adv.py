import random
from room import Room
from player import Player
from adv_save import load_results, save_results



# global vars
save_file = "adv_save.txt"

# Declare all the rooms
room = {
    'outside':  Room("outside the Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("in the Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("at the Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("in a narrow passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("in the Treasure Chamber!", """You've found the long-lost treasure
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


# _________ init  _______________
# Make a new player object that is currently in the 'outside' room.
curr_player = Player("Player1", room['outside'])

# _______ welcome message _______
# results = load_results()
# wins = int(results[0])
# ties = int( results[1])
# losses = int(results[2])
# initialize CLI
print("Welcome to Astrillia !")
print("You are currently "+curr_player.curr_room.name)
print(curr_player.curr_room.description)

print("Where would you like to go?..")
com_mand = input("choose: [n]North [s]South [e]East [w]West   [q]Quit\n",)

# gamplay loop: Waits for user input and decides what to do.
# Prints the curr_room
#        and description (the textwrap module might be useful here).
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

while not com_mand == "q":  # If the user enters "q", quit the game.
    if com_mand == "n":
        print('you head north...')
    elif com_mand == "s":
        print('you head south...')
    elif com_mand == "e":
        print('you head east...')
    elif com_mand == "w":
        print('you head west...')
    else:
        print("Invalid selection. Please try again.")
    
    # print updated location
    # print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))

    # prompt user to make another selection
    com_mand = input("choose: [n]North [s]South [e]East [w]West   [q]Quit\n")

# game over 
# save_results(wins, ties, losses)
print('thanks for playing!!....')