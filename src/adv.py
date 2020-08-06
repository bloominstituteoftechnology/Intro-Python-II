from room import Room
from player import Player
from item import Item


# Declare all the items
item = {
    'brain': Item('Brain', 'The Scarecrow\'s found a Brain!'),
    'heart': Item('Heart', 'Thanks for finding a Heart for the Tin Man'),
    'courage': Item('Courage', 'Kindly give the Lion some Courage'),
    'water bucket': Item('Water Bucket', 'May come in useful to melt some witches ;)!'), 
    'home': Item('Home', 'Where did the tornado send Home to??')
}

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
"North of you, the cave mount beckons", item['brain']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", item['heart']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", item['courage']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", item['water bucket']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", item['home']),
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

# 1. Make a new player object that is currently in the 'outside' room.

player_name = input("Choose your player name: ")
player_room = room['outside']

player = Player(player_name, player_room, [])

# Write a loop that:
while True:

    # 2. Prints the current room name
    # 3. Prints the current description (the textwrap module might be useful here).
    location = player.current_room
    print(f"""\n    Welcome {player.name}! The goal of this game is to find the treasure! 
    You are currently located at the {player_room.name}. {player_room.description}. 
    Please input 'n', 's', 'e', or 'w' to move to a different location. 
    Note that not all directions may be allowed at any given time. 
    You may also input 'q' at any time to quit!\n""")

    # 4. Waits for user input and decides what to do.
    command = input("> ").split(',')

    # 5. If the user enters "q", quit the game.
    if command[0] == 'q':
        print(f"Thanks for playing!")
        break

    # 6. If the user enters a cardinal direction, attempt to move to the room there.
    # 7. Print an error message if the movement isn't allowed.
    elif command[0].lower() == 'n' or command[0].lower() == 'north':
        pass
    elif command[0].lower() == 's' or command[0].lower() == 'south':
        pass
    elif command[0].lower() == 'e' or command[0].lower() == 'east':
        pass
    elif command[0].lower() == 'w' or command[0].lower() == 'west':
        pass