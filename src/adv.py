from room import Room
from player import Player
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
old_room = room['outside']

new_room = room['outside']
new_Player = Player(new_room , "name")
#print(room["outside"])
#print([(k, room[k]) for k in room])
#print(room['outside'].n_to)

print(old_room)
direction = (input("[E] East  [N] North   [W] West    [S] South     [Q] Quit\n")).upper()
# Make a new player object that is currently in the 'outside' room.

# Write a loop that:

while not direction == "Q":
    
    if direction == "N":
        if new_room.n_to == None:
            print("Can't go there")
        else:
            new_room = new_room.n_to
            print(new_room)
                
    elif direction == "S":
        if new_room.s_to == None:
            print("Can't go there")
        else:
            new_room = new_room.s_to
            print(new_room)
            
    elif direction == "E":
        if new_room.e_to == None:
            print("Can't go there")
        else:
            new_room = new_room.e_to
            print(new_room)
            
    
    elif direction == "W":
        if new_room.w_to == None:
            print("Can't go there")
        else:
            new_room = new_room.w_to
            print(new_room)
            
        
        
        
        
    

#    print("newplayer",new_Player)
    direction = (input("[E] East  [N] North   [W] West    [S] South     [Q] Quit\n")).upper()
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
