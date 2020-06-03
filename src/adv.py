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
# Make a new player object that is currently in the 'outside' room.
player_name = input('what is your name? ')
player1 = Player(player_name, room['outside'])
print(f'welcome {player1.name}!')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
quiting = False

while not quiting:

    
    print(f'You are standing inside the {player1.current_room.name}. You look around and see {player1.current_room.description}\n')
    print(f'near by you also see {player1.current_room.items}')
    
    # what are the accepted commands for movement of quitting? If the user doesnt enter then we will
    # prompt for an accepted command. 

    accepted_commands = ['q', 'n', 'e', 's', 'w']
    
    # get the user command for the direction that they want to move, or if they want to quit. 
    command = input('What do you want to do? You can move n, s, e, or w. or you can quit, q? ')
    command = command.strip() # add the strip() in case the user accidently puts a space after their choice.
     
    if command in accepted_commands:
        if command == 'n':
            if player1.current_room.n_to == None:
                print("That way is blocked! Pick another direction!\n")
                # player1.current_room
            else:
                player1.current_room = player1.current_room.n_to
        if command == 's':
            if player1.current_room.s_to == None:
                print("That way is blocked! Pick another direction!\n")
                # player1.current_room
            else:
                player1.current_room = player1.current_room.s_to
        if command == 'e':
            if player1.current_room.e_to == None:
                print("That way is blocked! Pick another direction!\n")
                # player1.current_room
            else:
                player1.current_room = player1.current_room.e_to
        if command == 'w':
            if player1.current_room.w_to == None:
                print("That way is blocked! Pick another direction!\n")
                # player1.current_room
            else:
                player1.current_room = player1.current_room.w_to
        if command == 'q':
            quiting = True
            print('Thanks for playing!')
    else:
        command = input('That isnt a valid command! You can move n, s, e, or w. or you can quit, q? ')

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
