from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

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
# if __name__ == "__main__":

# Make a new player object that is currently in the 'outside' room.
curr_player = Player("P1", room["outside"])

# _______ Intro Message _______
print("//////////////////////////////////")
print("////// Welcome to THE MAZE //////")
print("/////////////////////////////////\n")
print(f"Your current location is the {curr_player.location.title}.")
print("..."+curr_player.location.description+"..\n")
print("To move around choose from [n]North, [s]South, [e]East, or [w]West.\nOr [q] to Quit from The Maze\n")

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

# Begining of REPL (Read, Evaluate, Print, Loop)
# will wait for response from user and according to it
# proceed to process move and print out description of room
# or print out message in case move fails
# then wait for user input again
command = input("Where would you like to go to begin?: ")
# print('INPUT GIVEN BY USER:', command.strip(' '))

commands = ['n', 's', 'e', 'w', 'q']

# chosen_loc = None
# if cmd =='n':
#     chosen_loc = 'north'
# elif cmd == 's':
#     chosen_loc = 'south'
# elif cmd == 'e':
#     chosen_loc = 'east'
# elif cmd == 'w':
#     chosen_loc = 'west'

while command in commands: # quit game if 'q' entered
    if command == "q":
        break

    elif command == 'n':
        print(f'You have chosen to go North.\n')
        if curr_player.location.n_to == None:
                #curr_player.location = curr_player.location.n_to
                print("--> You are not able to go north based on your current location. <--\n")
        else:
            curr_player.location = curr_player.location.n_to
            #print("Not able to go north based on your current location.\n")

    elif command == 's':
        print('You have chosen to go South.\n')
        if curr_player.location.s_to == None:
                #curr_player.location = curr_player.location.n_to
                print("--> You are not able to go south based on your current location. <--\n")
        else:
            curr_player.location = curr_player.location.s_to
            #print("Not able to go north based on your current location.\n")

    elif command == 'e':
        print('You have chosen to go East.\n')
        if curr_player.location.e_to == None:
                #curr_player.location = curr_player.location.n_to
                print("--> You are not able to go east based on your current location. <--\n")
        else:
            curr_player.location = curr_player.location.e_to
            #print("Not able to go north based on your current location.\n")

    elif command == 'w':
        print('You have chosen to go West.\n')
        if curr_player.location.w_to == None:
                #curr_player.location = curr_player.location.n_to
                print("--> You are not able to go west based on your current location. <--\n")
        else:
            curr_player.location = curr_player.location.w_to
            #print("Not able to go north based on your current location.\n")

    print(f'Your current location is the {curr_player.location.title}.')
    print("..."+curr_player.location.description+"..")
    command = input("\nWhere would you like to go now?\n ([n]North, [s]South, [e]East, or [w]West.\nOr [q] to Quit): ")



