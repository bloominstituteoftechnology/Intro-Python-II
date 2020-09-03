from room import Room
from player import Player
import sys
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

def the_quest ():
    #Title
    print("Welcome to your Quest!")
    print("Find the Treasue and win the game!")

    #Chose Player name
    Hero = input("What is your players name? ")

    #Player Location
    p1 = Player(Hero,'outside')
    print("Welcome " + Hero + " you are" + " " + p1.location)
    direction = input("Chose which direction, n (North) , e (East),w (West) ,s (South), press q to quit ")
    
    while True:
        #outside
        if p1.location == 'outside' and direction == 'n':
            p1 = Player(Hero,'foyer')
            print(Hero + " you are located " + " "+ p1.location)
        
            #foyer
        elif p1.location == 'foyer' and direction == 's':
                p1 = Player(Hero,'outside')
                print(Hero + " you are located " + " "+ p1.location)
        elif p1.location == 'foyer' and direction == 'n':
                 p1 = Player(Hero,'overlook')
                 print(Hero + " you are located " + " "+ p1.location)
                 
             #overlook foyer n
        elif p1.location == 'overlook' and direction == 's':
                     p1 = Player(Hero,'foyer')
                     print(Hero + " you are located " + " "+ p1.location)
                   
        
        elif p1.location == 'foyer' and direction == 'e':
                p1 = Player(Hero,'narrow')
                print(Hero + " you are located " + " "+ p1.location)
            
   
                #narrow foyer e
        elif p1.location == 'narrow' and direction == 'w':
                    p1 = Player(Hero,'foyer')
                    print(Hero + " you are located " + " "+ p1.location)
                    
        elif p1.location == 'narrow' and direction == 'n':
                    p1 = Player(Hero,'treasure')         
                    print('YOU FOUND THE TREASURE!!')
                    break
           
        if direction == 'q':
            print("Goodbye " + Hero)
            break
        else:
            print("Wrong direction, your are located" + " " + p1.location)
            direction = input("Chose which direction, n (North) , e (East),w (West) ,s (South), press q to quit ")
        
      



the_quest()

    