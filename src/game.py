

# This is the file where the game loop is found
# This file is called in the adv.py file.

from room import Room
from player import Player
from os import system, name
import sys
import buildRooms
import textwrap 
from getchar import getch







# Will be making a class that is called game


class Game:

    def __init__(self, player=None):
        self.player = player



    # This the is the string that is used in the function
    # print_instructions_and_get_input
    instructString = """
        To move: press \"n\", \"s\", \"e\", \"w\" or \"q\" to quit

    """
    # This is just to find out if they have entered in 
    # some letters or words that are valid with our game
    allowedLettersorWords = ["north", "n", "south", "s", "east", "e", "west", "w", "q", "quit"]

    # This is a list of the action for two word values
    twoWordList = [""]


    # This is the one word list of actions
    # This list is used to help get the action to perform
    oneWordList = ["n", "s", "e", "w", "q"]

    # making a dictionary that is used to append to the 
    # print out each time
    appendPrint = {

                2: "You can\'t go in that direction! Choose somewhere else to go.\n\n",
                1: "Make sure that you are entering the correct info!\n\n",
                0: "" # Nothing is added with this one


    }

    intro = """
            Welcome to the mighty adventure game!
            Would you like to start an adventure?\n
            Press "y" if you would like to play the game.
            Press "n" if your not adventureous.
        """


        ## function that will be used to clear the screen of the terminal when wanted
    def clear_screen(self):
        if name == "nt":
            _= system('cls')
        else:
            _ = system("clear")

    def fareWell(self):
        # cleaing the screen
        self.clear_screen()

        print("""Goodbye, Hope to see you again!\n\n
            
            """)
        sys.exit()


    def add_explan(self):
        # this function will first need to clear the 
        # screen
        self.clear_screen()
        print(
            """You need to make sure that you put the right input in!\n
            
            """
        )
        



    def check_if_play(self):
        while True:

            print(self.intro)
            answer = getch()
            # decoding to use as a string b'a string'.decode('ascii')
            answer = answer.decode("ascii")
            if answer.isalpha():
                if answer.lower()[0] == "y":
                    break
                elif answer.lower()[0] == "n":
                    # Will be calling the farewell and then
                    # exit the program
                    self.fareWell()
            # will add this if they have input somthing that is 
            # not right
            self.add_explan()

        


    def okay_play(self):
        self.clear_screen()
        print("""
            Okay, let's play!


        """)

        theName = input("""
                        What do you want to be called during this game?\n
                        """)
        return theName




    # This function will be used to find the integer that matches the user input
    def elemNum_of_list(self, wordList, userInput):
        for i in range(len(wordList)):
            if userInput == wordList[i]:
                return i
        # Will return if the input is somehow not in the wordlist
        return -1



    # This the function that will move direction
    def movePlayer(self, direction):
        nextRoom = None
        # getting the current room the player is in
        theRoom = self.player.current_room
                
        if direction == 0: # This means north
            # need to see if you can move north
            nextRoom = theRoom.n_to
        if direction == 1: # This means south
            nextRoom = theRoom.s_to
        if direction == 2: # This means east
            nextRoom = theRoom.e_to
        if direction == 3: # This means west
            nextRoom == theRoom.w_to
            
        # now will check to see if the dircection is available
        if nextRoom == None:
            # print the message
            return 2
        else:
            # setting the new room for the player
            self.player.current_room = nextRoom
            return 0

            
            
    





    # This method will do that action that was inputted by the user
    def perform_user_action(self, userInput, numWords=None):
        """
        This function will return -1 if there was an error and -2 if 
        the player wants to quit.  It can also return the number for the key to 
        print. 
        
        """
        num = None
        wordList = None
        if numWords == 1:
            wordList = self.oneWordList
            # if the userinput is a q or a quit
            # then here we will perform the action to quit
            if userInput.lower()[0] == "q":
                return -2 # When returning 2 it is a signal 
                        # that they want to quit the game
        else:
            wordList = self.twoWordList
        # This where the one word values are performed
        # getting the integer of the element in the oneWordList
        num = self.elemNum_of_list(self.oneWordList, userInput)

        # sending to the function that is necessary
        if num >= 0 and num <= 3:
            return self.movePlayer(num)
            
        return -1 # This means that something was not right.



    # This is the function that will print the current room 
    # and then will also print the description of the room
    def print_room_and_descrip(self, theKey):
        r = self.player.current_room
        self.clear_screen() # clearing the screen      
       
        # using the textwrapper to wrap the function
        wrapper = textwrap.TextWrapper(width=50)
        theString = wrapper.fill(r.description)
        
        answer = input(f"{self.appendPrint[theKey]}{self.player.playerName}, you are in the {r.name}\n{theString}\n\n\n\n{self.instructString}\n")
        return answer



    # This function will check to see if the one word is valid
    def is_valid(self, word,):
        if word.isalpha():
            if word  in self.allowedLettersorWords:
                return True
        
        return False



    # This function will return false if there was an error such as 
    # if the user has input something not valid
    # Will return a True if the input was valid and no error occured
    def parse_user_input(self, theInput):
        # making the input as a list so that we can then check one word
        # at a time if needed
        
        number_of_words = None

        if self.is_valid(theInput):
            theList = theInput.split()
            if len(theList) == 1: #  here it is a one word input
                number_of_words = 1
            else:
                number_of_words = 2
                # Need to do the action that is asked for
            return self.perform_user_action(theInput, numWords=number_of_words)
        return 1   # Will return this is the input was not valid 
            
            


    # This is the method that will be used in as the loop for the game
    def play_game(self):
        print_key = 0 # This key is passed in to the print_room_and_description
                         # Will tell what type of message to print out
        while True:
        # Will now be playing the game will show the current room
            # calling the function that will print out the location where the 
            # player is and instruction for what to do
            theInput = self.print_room_and_descrip(print_key)

            # calling the function that will parse the info entered in 
            val = self.parse_user_input(theInput=theInput)
            if val == -2:
                self.fareWell()
                #break
            print_key = val