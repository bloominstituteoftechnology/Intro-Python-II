#benefits of oop
#encapsulation every object needs some kind of extenral facing API in order to manipulate its internal state.
#inheritance allows us to leverage preexisting code that exists on a base class. explicitly forms object hierarchy.
#polymorphism

#in python only use dictionaries for storing key value pairs. 

from seanroom import Room
from seanplayer import Player

player = Player(room['outside'])

def try_direction(direction, current_room):
    #direction is the direction the user input
    #current_room is the current room player in
    #returns the new room that the player move to if
    #move was successful or return current room if the move
    # was not successful
    attribute = direction + '_to'
    #append to to the direction command
    #can see if inputted direction is valid
    if hasattr(current_room, attribute):
        #fetch the new room
        return getattr(current_room, attribute)
    #could also do try/except but this is more explicit than general
    else:
        print("You can't go that way!")
        return current_room

while True:
    print(player.current_room.name)
    print(player.current_room.description)

    s = input("\n>").lower()[0]
    """
    want to accept all these:
    so can just take first letter of these ie 0 element
    North, South, East, West, north, south, east, west
    N, S, E, W, n, s, e, w
    """
    player.current_room = try_direction(s, player.current_room)

    if s == 'q':
        break
        #ie break out of the loop


#for getting an item
while True:
    s = input("\n>").lower().split()
    #split for two word commands

    #check to see if user input one or two word command
    if len(s) == 1:
        #then user passed a direction

        #grab first char of first word
        s = s[0][0]

        player.current_room = try_direction(s, player.current_room)

    elif len(s) ==2: 
        #user passed a two-word command
        first_word = s[0]
        second_word = s[1]

        if first_word in ['get', 'drop']:

    else:
        print("i dont understand that")
        continue
    
