from room import Room
from player import Player

import textwrap

## My room declarations

room = {
    'hallway' : Room("Super Lame Hallway", 
    "This hallway is nothing but concrete and drywall, but it does lead you to the Outside World. Head North to Exit into the Outside World."),
    'garden' : Room("The Gated Garden", 
    "The outside world beckons! Head North on the Forest Path. Head East to visit the Pond. Head South back into the Super Lame Hallway(don't do it!)."),
    'pond' : Room("Pretty Lil Pond",
    "A great place to unwind. Watch the swans and feel the breeze. The path back to The Gated Garden is the only exit."),
    'path' : Room("Forest Path",
    "This path looks enticing! You may head West and discover what beauties it may hold, or return South to the Gated Garden and all that you've ever known."),
    'cave': Room("Adventure Cave", 
    "This cave looks a little scary. Should you choose to be adventerous and bold and enter, or turn back?")
}



## My room links

room['hallway'].N_to = room['garden']
room['garden'].S_to = room['hallway']
room['garden'].E_to = room['pond']
room['pond'].W_to = room['garden']
room['garden'].N_to = room['path']
room['path'].S_to = room['garden']
room['path'].W_to = room['cave']
room['cave'].E_to = room['path']

#
# Main
#
# cave = room['cave'].e_to
# print(cave)
name = input('\nPlease enter your character name: ').capitalize()
# Make a new player object that is currently in the 'outside' room.
player = Player(name, room["hallway"])
print(f"\n\nWelcome {player.name}. You begin your journey begins in the {player.current_room}.")
print(f"\n\nNavigate through the world with keys W, D, S, A \nas directions N, E, S, W respectively. \nPress Q to exit the game.")    

# Write a loop that:
def direction_func():
    choice = input("\n\nPlease enter your direction/command choice : ").upper()
    if(choice in ['W', 'S', 'D', 'A', 'Q']):
        print(f"line 49, {choice}")
        return choice
    else :
        print('\n\nYou have made an invalid choice. Please choose a valid command.')
        direction_func()

choice = ""
while(choice != "Q"):
    print(f"\n\n{player.name}, you are in {player.current_room}")
    choice = direction_func()
    print(f"line 59 {choice}")
    if(choice in ['W', 'D', 'S', 'A']):
        print("A choice")
    else:
        print(f"Farewell Brave Traveler {player.name}.")


    




#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.






#Old/ example code below
# Declare all the rooms

# room = {
#     'outside':  Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons"),

#     'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east."""),

#     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm."""),

#     'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air."""),

#     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south."""),
# }

# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']








