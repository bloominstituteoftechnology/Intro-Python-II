from room import Room
from os import system, name
import sys
from game import Game
from player import Player
from buildRooms import room



### ----------------------------------------------####
# I have moved the rooms dictionary into the buildRooms file
# I also moved the linking of the rooms  in to the build rooms file
### ---------------------------------------------- ###


#
# Main
#


###
# some of the methods that are used in the game logic

# instanciating a game
game = Game(Player())




### THE GAME LOOP IS FOUND IN GAME.PY ###


# Make a new player object that is currently in the 'outside' room.


# STARTING of the GAME here


# this is an flag to see if this is the first time to play the game
first_time = 1

while True:
    # the inner loop of if you wanto to play the game
    if first_time:
        game.check_if_play()
    
    theName = game.okay_play()

    # putting giving the player a name and putting him in the outside room
    game.player.current_room = room["outside"]
    game.player.playerName = theName
    
    
    game.play_game() # this is the real loop for the game





   
# Write a loop that:  #####------ This loop will be found in the game.py file ------#####
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
