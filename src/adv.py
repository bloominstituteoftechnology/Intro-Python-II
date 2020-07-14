from room import Room
from os import system, name
import sys
from game import play_game

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

intro = """
        Welcome to the mighty adventure game!
        Would you like to start an adventure?
        Press "y or yes" if you would like to play the game.
        Press "n or no" if your not adventureous.
        """
###
# some of the methods that are used in the game logic

## function that will be used to clear the screen of the terminal when wanted
def clear_screen():
    if name == "nt":
       _= system('cls')
    else:
        _ = system("clear")

def fareWell():
    # cleaing the screen
    clear_screen()

    print("""
        Goodbye, Hope to see you again!\n\n
        """)
    sys.exit()


def add_explan():
    # this function will first need to clear the 
    # screen
    clear_screen()
    print(
        """
        You need to make sure that you put the right input in!\n
        """
    )
    



def check_if_play():
    while True:
        answer = input(intro)
        if answer.isalpha():
            if answer.lower()[0] == "y":
                break
            elif answer.lower()[0] == "n":
                # Will be calling the farewell and then
                # exit the program
                fareWell()
        # will add this if they have input somthing that is 
        # not right
        add_explan()

    


def okay_play():
    clear_screen()
    print("""
        Okay, let play!


    """)







# Make a new player object that is currently in the 'outside' room.


# STARTING of the GAME here

#Putting the game loop here
# this is an flag to see if this is the first time to play the game
first_time = 1

while True:
    # the inner loop of if you wanto to play the game
    if first_time:
        check_if_play()
    
    okay_play()

    # calling the game loop here:
    # The game loop I am putting in a new file called game just to keep this less
    # full of stuff
    play_game()




   
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
