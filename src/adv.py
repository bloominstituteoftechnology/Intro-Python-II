from room import Room
from player import Player
from item import Item
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

# Make a new player object that is currently in the 'outside' room.
new_player = Player('Link', room['outside'])
# print('NEW PLAYER', new_player)

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



def oops():
    print('You forgot to type haha')
    
def directions():
    print('*hint player can move go n, w, e, or s *')
    
# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# need a method to access dictionary data 
# want a loop that won't end

while True: 
    # print(f'\n {new_player.current_room.description}')
# #     #READ
# #     #create prompt that allows you to set; always a string
    cmd = input("-> ") 
    if len(cmd) <= 0:
        oops()
    if cmd == "directions":
        directions()
    elif cmd == "n":
        if new_player.current_room == room.get("outside", ['Room cannot be found']):
            new_player.current_room = new_player.current_room.n_to
            print(f'\n  You have entered the {new_player.current_room.description}\n') ##player in the foyer 
            
        elif new_player.current_room == room.get("foyer", ['Room cannot be found']):
            new_player.current_room = new_player.current_room.n_to
            print(f'\n  You have entered the {new_player.current_room.description}\n') ##player in the overlook
            
        else:
            new_player.current_room != ("foyer" or "outside")
            new_player.current_room = room.get("treasure")
            print(f'\n  You have entered the {new_player.current_room.description}\n') #player in treasure 
            
    elif cmd == "s":
        if new_player.current_room == room.get("foyer", ['Room cannot be found']):
            new_player.current_room = new_player.current_room.s_to #to overlook
            print(f'\n  You have entered the {new_player.current_room.description}\n') #outside 
            
        elif  new_player.current_room == room.get("overlook", ['Room cannot be found']):
            new_player.current_room = new_player.current_room.s_to #to foyer
            print(f'\n  You have entered the {new_player.current_room.description}\n') # player in foyer 
            
        else:
            new_player.current_room != ("foyer" or "overlook")
            new_player.current_room = room.get("narrow") #to treasure room to foyer
            print(f'\n  You have entered the {new_player.current_room.description}\n')  #to narrow 
            
    elif cmd == "e":
        if new_player.current_room == room.get("foyer", ['Room cannot be found']):
            new_player.current_room = new_player.current_room.e_to
            print(f'\n  You have entered the {new_player.current_room.description}\n') #player in narrow
            
    elif cmd == "w":
        if new_player.current_room == room.get("narrow", ['Room cannot be found']):
            new_player.current_room = new_player.current_room.w_to
            print(f'\n  You have entered the {new_player.current_room.description}\n') #player in foyer
    elif cmd == "q":
        print('Peace Out!')
        break