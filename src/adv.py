import os
from room import Room
from player import Player

os.system( 'clear' )

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons" ),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""" ),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""" ),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""" ),
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

playing = True

name = input( 'What is your name? ' );

os.system( 'clear' )

player = Player( f'{name}' , 'outside' , room['outside'], 3 )

def move( direction ):
    os.system( 'clear' )

    if player.currentroom == 'outside':

        if direction == 'n':

            player.currentroom = 'foyer'
            player.roomdescription = room['foyer']

        else:

            print( 'you cant go that way' )

    elif player.currentroom == 'foyer':

        if direction == 'n':

            player.currentroom = 'overlook'
            player.roomdescription = room['overlook']

        if direction == 's':

            player.currentroom = 'outside'
            player.roomdescription = room['outside']

        if direction == 'e':

            player.currentroom = 'narrow'
            player.roomdescription = room['narrow']

        if direction == 'w':

            print( 'you cant go that way' )

    elif player.currentroom == 'overlook':

        if direction == 's':

            player.currentroom = 'foyer'
            player.roomdescription = room['foyer']

        else:
            os.system( 'clear' )
            print( f'{name} fell off a cliff. You lose one life' )
            player.hearts = player.hearts - 1
            

    else:
        os.system( 'clear' )
        print( 'try again' )

        

    
    # if player.currentroom == 'foyer':


while ( playing == True ):

    if player.hearts == 0:
        break

    print( 'Lives: ' + '❤️   '* player.hearts )
    print( f'User: {player.name}' )
    print( f'Current Room: {player.currentroom}' )
    print( f'Description: {player.roomdescription}' )

    direction = input( 'What direction do you want to go? ( n , s , e , w ) ' ).lower()

    move( direction )

    # if ( direction == 'n' ):
    #     os.system( 'clear' )

    #     player.currentroom = room['foyer']
    #     print( player.currentroom )


    # elif ( direction == 's' ):
    #     os.system( 'clear' )


    #     print( 'South' )
    

    #     # player = Player( f'{name}' , room['outside'].s_to )
    
    # elif ( direction == 'e' ):
    #     os.system( 'clear' )

    #     print( 'East' )

    # elif ( direction == 'w' ):
    #     os.system( 'clear' )

    #     print( 'West' )

os.system( 'clear' )
print( 'Game Over' )



    


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
