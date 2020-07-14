

# This is the file where the game loop is found
# This file is called in the adv.py file.

from room import Room
#from os import system, name
import sys
from adv import fareWell, clear_screen ,room  # this is the dictionary of the rooms
import textwrap 
from getchar import getch



# This the is the string that is used in the function
# print_instructions_and_get_input
instructString = """
    To move: press \"n\", \"s\", \"e\", \"w\"

"""
# This is just to find out if they have entered in 
# some letters or words that are valid with our game
allowedLettersorWords = ["north", "n", "south", "s", "east", "e", "west", "w", "q", "quit"]

# This is a list of the action for two word values

# This is the method that will print out what the 
# player can do and then and get the input
def print_instructions_and_get_input():
    print(theString)
    # will be using the getch to get the char only




# This method will do that action that was inputted by the user
def perform_user_action(wordList):
    if len(wordList) == 2:
        pass # This where the two word values are 

# This is the function that will print the current room 
# and then will also print the description of the room
def print_room_and_descrip(thePlayer):
    r = thePlayer.current_room
    # using the textwrapper to wrap the function
    wrapper = textwrap.TextWrapper(width=50)
    theString = wrapper.fill(r.description)
    clear_screen()
    answer = input(f"You are in the {r.name}\ntheString\n\n\n\n{instructString}\n")

# This function will check to see if the one word is valid
def is_valid(word):
    if word.isalpha():
        if word  in allowedLettersorWords:
            return True
    
    return False
# This function will return false if there was an error such as 
# if the user has input something not valid
# Will return a True if the input was valid and no error occured
def parse_user_input(theInput):
    # making the input as a list so that we can then check one word
    # at a time if needed
    theList = theInput.split()
    if len(theList) == 1: #  here it is a one word input
        if is_valid(theList[0]):
            # Need to do the action that is asked for



# This is the method that will be used in as the loop for the game
def play_game(thePlayer):
    while True:
       # Will now be playing the game will show the current room
        # calling the function that will print out the location where the 
        # player is and instruction for what to do
        theInput = print_room_and_descrip(thePlayer)

        # calling the function that will parse the info entered in 
        parse_user_input(theInput=theInput)