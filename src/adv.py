from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", """
    North of you, the cave mount beckons."""),

    'foyer':    Room("Foyer", """
    Dim light filters in from the south. 
    Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """
    A steep cliff appears before you, falling into the darkness.
    Ahead to the north, a light flickers in the distance, 
    but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """
    The narrow passage bends here from west to north.
    The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """
    You've found the long-lost treasure chamber! 
    Sadly, it has already been completely emptied by earlier adventurers. 
    The only exit is to the south."""),
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
player_name = input("    Please enter player name: ")
print()
player = Player(player_name, room['outside'])

# Another approach to try/except (will keep code DRY):
# def try_direction(dir, current_room):
#     attribute = dir + '_to'
    
#     #See if the inputted direction is one we can move to
#     if hasattr(current_room, attribute)
#         # fetch the new room
#         return getattr(current_room, attribute)
#     else: 
#         print('You cannot go that way')
#         return current_room

# Write a loop that:
while True:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
    print(f'    {player}')
    print()
# * Waits for user input and decides what to do.
    print(f'''    Your options:
        n to go North
        s to go South
        e to go East
        w to go West
        q  to   Quit
    ''')
    decision = input('    Where would you like to go? ').lower()
    print()
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    if (len(decision) == 1):
        # Continue hasattr/getattr approach:
        # else:
        # player.current_room = try_direction(decision, player.current_room )
        if (not (decision in ['n','s','e','w', 'q'])):
            print(f'    {decision} is not an option, try again...')
        elif (decision == 'n'):
            if (player.current_room.n_to):
                print(player.current_room.n_to)
        elif (decision == 's'):
            try:
                player.current_room = player.current_room.s_to
            except AttributeError:
                print(f'    {player.name} cannot move south, try again...')
        elif (decision == 'e'):
            try:
                player.current_room = player.current_room.e_to
            except AttributeError:
                print(f'    {player.name} cannot move east, try again...')
        elif (decision == 'w'):
            try:
                player.current_room = player.current_room.w_to
            except AttributeError:
                print(f'    {player.name} cannot move west, try again...')
    # If the user enters "q", quit the game.
        elif (decision == 'q'):
            print('    GAME OVER')
            print()
            break
    # elif (len(decision) == 4):
        

