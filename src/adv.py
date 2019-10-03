import os
from room import Room
from player import Player
import sys,time,random
import time

os.system( 'clear' )

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons" , [ 'Backpack' ] ),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""" , [] ),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""" , [ 'Key' ]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""" , [] ),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""" , [ 'Treasure' ] ),
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

typing_speed = 200
def slowprint(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)

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

slowprint( 'What is your name?' )

name = input(' ');

os.system( 'clear' )

errorMessage = []

player = Player( f'{name}' , 'outside' , room['outside'], 3 , [] )

def map( location ):

    if location == 'outside':

        print( 'Map:' )
        print(' --------              --------')
        print('|        |            |        |')
        print('|        |            |        |')
        print('|        |            |        |')
        print('|        |____________|__      |')
        print('|   ●     ______   ______      |')
        print('|        |      | |   |        |')
        print('|        |      | |___|________|')
        print('|        |      |______        |')
        print('|        |             |   💎   |')
        print(' ---------              -------')
        print( 'You: ●' )
        print('')

        

    if location == 'foyer':

        print( 'Map:' )
        print(' --------              --------')
        print('|        |            |        |')
        print('|        |            |        |')
        print('|        |            |        |')
        print('|        |____________|__      |')
        print('|         ______ ● ______      |')
        print('|        |      | |   |        |')
        print('|        |      | |___|________|')
        print('|        |      |______        |')
        print('|        |             |   💎   |')
        print(' ---------              -------')
        print( 'You: ●' )
        print('')


    if location == 'overlook':

        print( 'Map:' )
        print(' --------              --------')
        print('|        |            |        |')
        print('|        |            |        |')
        print('|        |            |        |')
        print('|        |____________|__      |')
        print('|         ______   ______●     |')
        print('|        |      | |   |        |')
        print('|        |      | |___|________|')
        print('|        |      |______        |')
        print('|        |             |   💎   |')
        print(' ---------              -------')
        print( 'You: ●' )
        print('')


    if location == 'narrow':

        print( 'Map:' )
        print(' --------              --------')
        print('|        |            |        |')
        print('|        |            |        |')
        print('|        |            |        |')
        print('|        |____________|__      |')
        print('|         ______   ______      |')
        print('|        |      | |   |        |')
        print('|        |      | |___|________|')
        print('|        |      |●_____        |')
        print('|        |             |   💎   |')
        print(' ---------              -------')
        print( 'You: ●' )
        print('')


    if location == 'treasure':

        print( 'Map:' )
        print(' --------              --------')
        print('|        |            |        |')
        print('|        |            |        |')
        print('|        |            |        |')
        print('|        |____________|__      |')
        print('|         ______   ______      |')
        print('|        |      | |   |        |')
        print('|        |      | |___|________|')
        print('|        |      |______  ●     |')
        print('|        |             |   💎   |')
        print(' ---------              -------')
        print( 'You: ●' )
        print('')


def move( direction ):

    o = .1

    os.system( 'clear' )

    if len( errorMessage ) > 0:
        for i in errorMessage:
            errorMessage.pop()

    if player.currentroom == 'outside':

        if direction == 'l':

            if len( room['outside'].items ) > 0:

                os.system( 'clear' )
                availableitems = room['outside'].items
                slowprint( 'Items in room: ' )
                slowprint( *availableitems )
                answer = input( '\nPick it up? ( y / n )\n' ).lower()
                if answer == 'y':
                    player.items.append( availableitems[0] )
                    room['outside'].items.remove( availableitems[0] )
                    os.system( 'clear' )
                else:
                    print( 'did not pick it up' )
            else:
                errorMessage.append( 'No Items In This room' )

        elif direction == 'n':

            print(' \n' * 7 )

            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|   ●     ______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)
            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|    ●    ______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|     ●   ______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|      ●  ______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|       ● ______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|        ●______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ●_____   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         _●____   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         __●___   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ___●__   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ____●_   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         _____●   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______ ● ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            os.system( 'clear' )

            player.currentroom = 'foyer'
            player.roomdescription = room['foyer']

        else:

            errorMessage.append( 'you cant go that way' )

    elif player.currentroom == 'foyer':

        if direction == 'l':

            if len( room['outside'].items ) > 0:

                os.system( 'clear' )
                availableitems = room['foyer'].items
                slowprint( 'Items in room: ' )
                slowprint( *availableitems )
                answer = input( '\nPick it up? ( y / n )\n' ).lower()
                if answer == 'y':
                    player.items.append( availableitems[0] )
                    room['foyer'].items.remove( availableitems[0] )
                    os.system( 'clear' )
                else:
                    print( 'did not pick it up' )
            else:
                errorMessage.append( 'No Items In This room' )

        elif direction == 'n':

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______  ●______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)
            
            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ●_____      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)
            
            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   _●____      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   __●___      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ___●__      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ____●_      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   _____●      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            player.currentroom = 'overlook'
            player.roomdescription = room['overlook']

        if direction == 's':

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______ ● ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         _____●   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ____●_   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ___●__   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         __●___   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         _●____   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ●_____   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|        ●______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|       ● ______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|      ●  ______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|     ●   ______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|    ●    ______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|   ●     ______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            player.currentroom = 'outside'
            player.roomdescription = room['outside']

        if direction == 'e':

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ______      |')
            print('|        |      |●|   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      |●|___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            player.currentroom = 'narrow'
            player.roomdescription = room['narrow']

        if direction == 'w':

            errorMessage.append( 'you cant go that way' )

    elif player.currentroom == 'overlook':

        if direction == 'l':

            if len( room['overlook'].items ) > 0:

                os.system( 'clear' )
                availableitems = room['overlook'].items
                slowprint( 'Items in room: ' )
                slowprint( *availableitems )
                answer = input( '\nPick it up? ( y / n )\n' ).lower()
                if answer == 'y':
                    player.items.append( availableitems[0] )
                    room['overlook'].items.remove( availableitems[0] )
                    os.system( 'clear' )
                else:
                    errorMessage.append( 'Did not pick the item up' )
            else:
                errorMessage.append( 'No Items In This room' )

        elif direction == 's':

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   _____●      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ____●_      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ___●__      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   __●___      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   _●____      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ●_____      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______  ●______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            player.currentroom = 'foyer'
            player.roomdescription = room['foyer']

        else:

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ______ ●    |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ______  ●   |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ______  x   |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ______  x   |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            errorMessage.append( f'{name} fell off a cliff. You lose one life' )
            player.hearts = player.hearts - 1

    elif player.currentroom == 'narrow':

        if direction == 'l':

            if len( room['narrow'].items ) > 0:

                errorMessage.append( 'No Items In This room' )

        if direction == 'n':

            hasKey = []

            if len( player.items ) > 0:
                for i in player.items:
                    if ( i == 'Key' ):

                        print( 'HAS KEY' )
                        hasKey.append( 'boop' )
                        

                    else:

                        print( 'No NEY' )

            if len( hasKey ) > 0:

                time.sleep(10)

                os.system( 'clear' )

                print(' \n' * 7 )
                print( 'Map:' )
                print(' --------              --------')
                print('|        |            |        |')
                print('|        |            |        |')
                print('|        |            |        |')
                print('|        |____________|__      |')
                print('|         ______   ______      |')
                print('|        |      | |   |        |')
                print('|        |      | |___|________|')
                print('|        |      |_●____        |')
                print('|        |             |   💎   |')
                print(' ---------              -------')
                print( 'You: ●' )
                print('')

                time.sleep(o)

                os.system( 'clear' )

                print(' \n' * 7 )
                print( 'Map:' )
                print(' --------              --------')
                print('|        |            |        |')
                print('|        |            |        |')
                print('|        |            |        |')
                print('|        |____________|__      |')
                print('|         ______   ______      |')
                print('|        |      | |   |        |')
                print('|        |      | |___|________|')
                print('|        |      |__●___        |')
                print('|        |             |   💎   |')
                print(' ---------              -------')
                print( 'You: ●' )
                print('')

                time.sleep(o)

                os.system( 'clear' )

                print(' \n' * 7 )
                print( 'Map:' )
                print(' --------              --------')
                print('|        |            |        |')
                print('|        |            |        |')
                print('|        |            |        |')
                print('|        |____________|__      |')
                print('|         ______   ______      |')
                print('|        |      | |   |        |')
                print('|        |      | |___|________|')
                print('|        |      |___●__        |')
                print('|        |             |   💎   |')
                print(' ---------              -------')
                print( 'You: ●' )
                print('')

                time.sleep(o)

                os.system( 'clear' )

                print(' \n' * 7 )
                print( 'Map:' )
                print(' --------              --------')
                print('|        |            |        |')
                print('|        |            |        |')
                print('|        |            |        |')
                print('|        |____________|__      |')
                print('|         ______   ______      |')
                print('|        |      | |   |        |')
                print('|        |      | |___|________|')
                print('|        |      |____●_        |')
                print('|        |             |   💎   |')
                print(' ---------              -------')
                print( 'You: ●' )
                print('')

                time.sleep(o)

                os.system( 'clear' )

                print(' \n' * 7 )
                print( 'Map:' )
                print(' --------              --------')
                print('|        |            |        |')
                print('|        |            |        |')
                print('|        |            |        |')
                print('|        |____________|__      |')
                print('|         ______   ______      |')
                print('|        |      | |   |        |')
                print('|        |      | |___|________|')
                print('|        |      |_____●        |')
                print('|        |             |   💎   |')
                print(' ---------              -------')
                print( 'You: ●' )
                print('')

                time.sleep(o)

                os.system( 'clear' )

                print(' \n' * 7 )
                print( 'Map:' )
                print(' --------              --------')
                print('|        |            |        |')
                print('|        |            |        |')
                print('|        |            |        |')
                print('|        |____________|__      |')
                print('|         ______   ______      |')
                print('|        |      | |   |        |')
                print('|        |      | |___|________|')
                print('|        |      |______●       |')
                print('|        |             |   💎   |')
                print(' ---------              -------')
                print( 'You: ●' )
                print('')

                time.sleep(o)

                os.system( 'clear' )

                print(' \n' * 7 )
                print( 'Map:' )
                print(' --------              --------')
                print('|        |            |        |')
                print('|        |            |        |')
                print('|        |            |        |')
                print('|        |____________|__      |')
                print('|         ______   ______      |')
                print('|        |      | |   |        |')
                print('|        |      | |___|________|')
                print('|        |      |______ ●      |')
                print('|        |             |   💎   |')
                print(' ---------              -------')
                print( 'You: ●' )
                print('')

                time.sleep(o)

                os.system( 'clear' )

                player.currentroom = 'treasure'
                player.roomdescription = room['treasure']
            
            else:
                print( 'Key required to enter this rrom' )

        if direction == 's':

            errorMessage.append( 'you cant go that way' )

        if direction == 'e':

            errorMessage.append( 'you cant go that way' )

        if direction == 'w':

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      |●|___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ______      |')
            print('|        |      |●|   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            player.currentroom = 'foyer'
            player.roomdescription = room['foyer']


    elif player.currentroom == 'treasure':

        if direction == 's':

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______ ●      |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |______●       |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |_____●        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |____●_        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |___●__        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |__●___        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            print(' \n' * 7 )
            print( 'Map:' )
            print(' --------              --------')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |            |        |')
            print('|        |____________|__      |')
            print('|         ______   ______      |')
            print('|        |      | |   |        |')
            print('|        |      | |___|________|')
            print('|        |      |_●____        |')
            print('|        |             |   💎   |')
            print(' ---------              -------')
            print( 'You: ●' )
            print('')

            time.sleep(o)

            os.system( 'clear' )

            player.currentroom = 'narrow'
            player.roomdescription = room['narrow']

        else:

            errorMessage.append( 'You cant go that way' )
            

    else:
        os.system( 'clear' )
        errorMessage.append( 'try again' )




while ( playing == True ):

    if player.hearts == 0:
        break

    print('')
    print( 'Lives: ' + '❤️   '* player.hearts )
    print('')
    print( f'User: {player.name}' )
    print('')
    print( f'Current Room: {player.currentroom}' )
    print( f'Description: {player.roomdescription}' )
    print( ' ' )
    map( player.currentroom )
    if len( player.items ) > 0 :
        print( f'Inventory: {player.items}' )
    else:
        print( ' ' )
    if len( errorMessage ) > 0:
        print( 'Error Message:' , errorMessage[0] )
    else:
        print( ' ' )

    print( ' ' )



    direction = input( 'What direction do you want to go? ( n , s , e , w ) ' ).lower()

    if direction == 'q':
        break

    else:
        move( direction )

os.system( 'clear' )
slowprint( '      ____-----------____ \n')
slowprint( '   _- /#################\ -_ \n')
slowprint( ' / #####/-           -\##### \ \n')
slowprint( "|.`\ #                   # /'.|\n" )
slowprint( '| # |                     | # |\n' )
slowprint( '|  $########         ######%  |\n' )
slowprint( '|  `-_####_.         ._####_-`|\n' )
slowprint( '| ,---====--~      ,--====--, |\n' )
slowprint( '| ||Game Over|   ||Game Over ||\n' )
slowprint( "| `-=______=-' /\  `-=_____='|\n" )
slowprint( " \ `--====- # /  \ #  ====--'/ \n" )
slowprint( "  | *##  #   -=||=- #  ###* | \n" )
slowprint( "  |    __    `===='   ___   | \n" )
slowprint( '   \. \  |#|#|#|#|#|#|  / . / \n' )
slowprint( "   | * .``=_=_=_=_=_=''. * | \n" )
slowprint( '    \ # \|#|#|#|#|#|#|/ #  / \n' )
slowprint( "     \    ` ` `  '' '     / \n" )
slowprint( '      \ -=____    ____=- / \n' )
slowprint( '        "====-____-===="  \n\n' )


    


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
