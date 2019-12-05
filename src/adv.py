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
choices = ['n', 's', 'w', 'e']
# print('NEW PLAYER', new_player)
items = {
    'scroll': Item("Scroll", 'A worn piece of parchment that contains faded directions to get out'),
    'sword': Item("Sword", 'A dull blunt sword lays against the wall in a dark corner'),
    'torch': Item("Torch", 'The torch looks as though it can be seperated from the wall and carried')
}

print(items['scroll'].description)
print(room['outside'].items) #empty array 
room['treasure'].items = items['scroll'] #adds item to room 
print(room['treasure'])
# Link rooms together
# don't forgot to use append to add item; or overwriting everything 

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
    print(f'\n  You have entered the {new_player.current_room.description}\n') 
    cmd = input("-> ").lower().strip() #if you have space won't affect code 
# #     #READ
# #     #create prompt that allows you to set; always a string
    # make this dynamic, instead of the hard code use if none
   
    if cmd in choices:
        if cmd == 'n' and new_player.current_room.n_to != None:
            new_player.current_room = new_player.current_room.n_to
              
        elif cmd == 's'and new_player.current_room.s_to != None:
            new_player.current_room = new_player.current_room.s_to

        elif cmd == 'w' and new_player.current_room.w_to != None:
            new_player.current_room = new_player.current_room.w_to
   
        elif cmd == 'e'and new_player.current_room.e_to != None:
            new_player.current_room = new_player.current_room.e_to
           
        else:
            cmd = input("That's wrong direction! type  N, S, E, W -> ").lower().strip()
    elif cmd == 'q':
        print('Bye')
        break
    else: 
        print("Invalid command")







    # # print(f'\n  You have entered the {new_player.current_room.description}\n') 
    # #bug when you hit the third n room about about none attr
    
    # if len(cmd) <= 0:
    #     oops()
    # if cmd == "directions":
    #     directions()
    # elif cmd == "n":  #check if equal to none
    #     new_player.current_room != None
    #     new_player.current_room = new_player.current_room.n_to
    #     print(f'\n  You have entered the {new_player.current_room.description}\n') 
            
    #     else:
    #         print('This wrong is invalid Sir!')
    # elif cmd == "s":
    #     new_player.current_room != None
    #     new_player.current_room = new_player.current_room.s_to
    #     print(f'\n  You have entered the {new_player.current_room.description}\n')
    #     else:
    #         print('This wrong is invalid Sir!')
    # elif cmd == "e":
    #     new_player.current_room != None
    #     new_player.current_room = new_player.current_room.e_to
    #     print(f'\n  You have entered the {new_player.current_room.description}\n') 
            
    #     else:
    #         print('This wrong is invalid Sir!')
    # elif cmd == "w":
    #     new_player.current_room != None
    #     new_player.current_room = new_player.current_room.w_to
    #     print(f'\n  You have entered the {new_player.current_room.description}\n') 
        
    # else:
    #     print('This wrong is invalid Sir!')
    # elif cmd == "q":
    #     print('Peace Out!')
    #     break 
    
