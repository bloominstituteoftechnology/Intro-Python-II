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
print(room['outside'])
# Make a new player object that is currently in the 'outside' room.
player_name = input("Enter your name  : ")
game_player = Player(player_name, "outside")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
while True:
    print('''\tCurrently you are in outside room .. 
             Hint to move : "{}"
             Keep moving around
             Press n : North direction
                   s : South direction
                   e : East direction
                   w : west direction
                   q : Quit'''.format(room['outside']))
    player_direction = input()
    a = ['n','s','e','w','q']
    if player_direction in a:
        if player_direction == 'q':
            print("Thanks for playing!\n")
            break
        elif player_direction == 'n':
            print('''\tYou are in Foyer room now 
                     Keep moving 
                     Next Hint to move :
                     "{}"'''.format(room['foyer']))
            print("Enter next direction : ")
            player_direction = input()
            
            if player_direction == 'e':
                print('''\tGoing in correct direction ...
                         Now you are in Narrow Passage
                         Hint to move forwoard : 
                         "{}"'''.format(room['narrow']))
                print("Enter next direction : ")
                player_direction = input()

                if player_direction == 'n':
                    print("WOW!! {}".format(room['treasure']))
                    break
                elif player_direction == 'w':
                    print("OOPS Follow the HINT : {}".format(room['narrow']))
                    print("Keep Trying : ")
                    player_direction = input()

                    if player_direction == 'n':
                        print("WOW!! {}".format(room['treasure']))
                        break
                    else:
                        print("BAD LUCk ... TRY AGAIN")
                        continue
    else:
        print("\tPlease enter ['n','s','e','w' OR 'q to Quit]")
        continue
    

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
