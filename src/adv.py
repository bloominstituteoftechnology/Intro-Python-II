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

# Make a new player object that is currently in the 'outside' room.

player_name = input("What's your name?: ")
player_room = room["outside"]
player = Player(player_name, player_room)
print(player)

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
# !!The hasattr() method returns TRUE if provided an attribute, FALSE if it doesn't.!!

while True:
    current_room = player.current_room
    print(f'You are located at {current_room.name}. {current_room.description}')
    print("What direction are you headed now?")
    answer = input('Enter n, s , e, w and q to quit the game: ')

    if answer == 'n':
        if hasattr(current_room, 'n_to'):
            print("Head North. Don't forget, the North Remembers...")
            player.current_room = current_room.n_to
        else:
            print(f'{player_name}, {player_name}... enter another location, this area is off limits ')
    elif answer == 's':
        if hasattr(current_room, 's_to'):
            print(f'{player_name}, Grab the sunscreen, Youre headed South!')
            player.current_room = current_room.s_to
        else:
            print(f'{player_name}, {player_name}... enter another location, this area is off limits')
    elif answer == 'e':
        if hasattr(current_room, 'e_to'):
            print(f'{player_name}, Youre moving on up, Headed to the East(side)')
            player.current_room = current_room.e_to
        else:
            print(f'{player_name}, {player_name}... enter another location, this area is off limits')
    elif answer == 'w':
        if hasattr(current_room, 'w_to'):
            print(f'{player_name}, Getting Wild? Head West')
            player.current_room = current_room.w_to
        else:
            print(f'{player_name}, {player_name}... enter another location, this area is off limits')
    elif answer == 'q':
            print(f"Its been fun, {player_name}. Youll be back soon!")
            exit()
