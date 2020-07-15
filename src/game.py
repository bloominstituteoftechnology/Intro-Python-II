

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

possesions = ""
item_added_removed = ""
roomName = ""

class Game:

    def __init__(self, player=None):
        self.player = player

    # This is a place holder for the item that is added to the player or
    # removed from the room. It is added to the dictionary of the appended 
    # responces
    

    
    
    

    # This the is the string that is used in the function
    # print_instructions_and_get_input
    instructString = """
        To move: press \"n\", \"s\", \"e\", \"w\" or \"q\" to quit.
        To pick up an item enter ["take" or "get"] "name-of-item".
        To drop an item enter "drop" "name-of-item"
        Enter "inventory" or "i",  to show what things you have in your possesion. 

    """

    # This is just to find out if they have entered in 
    # some letters or words that are valid with our game
    allowedLettersorWords = ["north", "n", "south", "s", "east", "e", "west", "w", "q", "quit", 
                                "take", "drop", "inventory", "i", "get" ]

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
                0: "" ,# Nothing is added with this one
                3:  f"",
                4: f"You have added the ",
                5: f"You can't have the ",
                6: f"You have now dropped the ",
                7: f"You can't drop the ", 
                8: f"There is "



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




    def player_has_light(self):
        """
        This method will return true if the player has a
        light in their possesion.  Will return false otherwise
        """
        for item in self.player.playersItems:
            if item.description == "LightSource":
                return True
        return False





    def getRoomDescription(self):
        """ 
        This method will return the room description with the items 
        also that are in the room in the description.
        """
        s = self.list_Items("room")
        # Checking to see if the player has a light source
        light = self.player_has_light()
        if s == "You don't have anything in your possesion.\n\n":
            # checking to see if the player has a light source
            if light == False and self.player.current_room.is_light == False:
                return self.player.current_room.description + "  To see what " \
                                    "items are in a room, find a lightsource in a room and " \
                                        "pick it up."
            return self.player.current_room.description
        else:
            if light == False and self.player.current_room.is_light == False:
                return self.player.current_room.description + "To see what" \
                                    "items are in a room, find a lightsource in a room and" \
                                        "pick it up."
            s = self.player.current_room.description + " " + s
            return s



    #    This is the funtion that will list the items that the player has in 
    # possesion.  If there are no items in his posssesion, then it will say 
    # "You don't have anything in your possesion"
    def list_Items(self, player_or_room="player"):
        global possesions 
        itemsList = None
        if player_or_room == "player":
            itemsList = self.player.playersItems
        else:
            itemsList = self.player.current_room.items_in_room

        if len(itemsList) == 0:
           
            possesions = "You don't have anything in your possesion.\n\n"
            return possesions
        # the string to which the whole list will be returned
        s = ""    
        for i, item in enumerate(self.player.playersItems):
            s = s + item.name 
            if i < len(self.player.playersItems) - 1:
                s = s + ", "
        possesions = s + "\n\n"
        return possesions
            



    # This function will be used to find the integer that matches the user input
    def elemNum_of_list(self, wordList, userInput):
        for i in range(len(wordList)):
            if userInput == wordList[i]:
                return i
        # Will return if the input is somehow not in the wordlist
        return -1



    # This the function that will move direction
    def movePlayer(self, userInput):
        nextRoom = None
        # getting the current room the player is in
        theRoom = self.player.current_room
        direction = userInput.lower()[0]

        if direction == "n": # This means north
            # need to see if you can move north
            nextRoom = theRoom.n_to
        if direction == "s": # This means south
            nextRoom = theRoom.s_to
        if direction == "e": # This means east
            nextRoom = theRoom.e_to
        if direction == "w": # This means west
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
    def oneWordFunction(self, userInput):
        """
        This function will return -1 if there was an error and -2 if 
        the player wants to quit.  It can also return the number for the key to 
        print. This function is for only one word inputs.
        
        """
            # if the userinput is a q or a quit
            # then here we will perform the action to quit
        if userInput.lower()[0] == "q":
            return -2 # When returning 2 it is a signal 
                        # that they want to quit the game
        elif userInput.lower()[0] == "i":
            self.list_Items()
            return 3

        #elif userInput.lower()[0] == "r":
         #   self.listRoomItems()
        
        else:
            # sending to the function that is necessary
            return self.movePlayer(userInput)
            
        return -1 # This means that something was not right.



    # This is the function that will print the current room 
    # and then will also print the description of the room
    def print_room_and_descrip(self, theKey):
        r = self.player.current_room
        filler = ""
        self.clear_screen() # clearing the screen      
        if theKey == 3:
            filler = possesions
        elif theKey == 4:
            filler = f"{item_added_removed} to the items you hold.\n\n"
        elif theKey == 5:
            filler = f"{item_added_removed}, because it is not available to have.\n\n"
        elif theKey == 6:
            filler = f"{item_added_removed} on the ground in {roomName}\n\n"
        elif theKey == 7:
            filler = f"{item_added_removed} because you don't have one on you!\n\n"
        elif theKey == 8:
            filler = f"no light. You need to find a light source to be able to see what is in this room!\n\n"
        # using the textwrapper to wrap the function
        else:
            filler = ""
        wrapper = textwrap.TextWrapper(width=50)
        # This is getting the room description. It will add the items to the 
        # desription and return a complete string 
        description = self.getRoomDescription()
        theString = wrapper.fill(description)
        
        answer = input(f"{self.appendPrint[theKey]}{filler}{self.player.playerName}, you are in the {r.name}\n\n{theString}\n\n\n\n{self.instructString}\n")
        return answer



    # This function will check to see if the one word is valid
    def is_valid(self, word,):
        """
        Used to check if the words are valid words for input
        """
        if word.isalpha():
            # The words are all in lower case when reaching here
            if word  in self.allowedLettersorWords:
                return True
        
        return False


    # This is the function that will work on handling the 
    # inputs that are two words
    def twoWordFunction(self,wordInputList):
        # This is assigned to be used in the dictionary with the 
        # append strings
        global item_added_removed
        global roomName
        item_added_removed = wordInputList[1]
        if wordInputList[0] == 'take' or wordInputList[0] ==  "get":
            if self.player_has_light() == True or self.player.current_room.is_light == True:
                # Will check to see if the item is in the room
                for item in self.player.current_room.items_in_room:
                    if item.name == item_added_removed:
                    # Will add to the players items and remove from the rooms
                        self.player.addItem(item)
                        self.player.current_room.items_in_room.pop(item)
                        # adding the method on_take
                        item_added_removed = item.on_take()
                        return 4
                
                return  5
                
            else:
                return 8
        else:
            for item in self.player.playersItems:
                if item.name == item_added_removed:
                    self.player.current_room.items_in_room.append(item)
                    self.player.playersItems.pop(item)
                    roomName = self.player.current_room.name
                    item_added_removed = item.on_drop()
                    return 6
            return 7


    # This function will return false if there was an error such as 
    # if the user has input something not valid
    # Will return a True if the input was valid and no error occured
    def parse_user_input(self, theInput):
        # making the input as a list so that we can then check one word
        # at a time if needed
        # making just the lower case version of the word
        theInput = theInput.lower()
        theList = theInput.split()
        if self.is_valid(theList[0]): # This does not check to see if the items askec to drop or add are good
            
            if len(theList) == 1: #  here it is a one word input
                return self.oneWordFunction(theInput)
                
            else:
                return self.twoWordFunction(theList)
                # Need to do the action that is asked for
            
        return  1   # Will return this is the input was not valid 
            
            


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