from room import Room
from player import Player
from bandersnatch import Bandersnatch
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.",
                     False),

    'foyer':    Room("Foyer", 
                     """Dim light filters in from the south. Dusty passages run north and east.""",
                     True),

    'overlook': Room("Grand Overlook",
                     """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
                     True),

    'narrow':   Room("Narrow Passage", 
                     """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
                     False),

    'treasure': Room("Treasure Chamber", 
                     """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",
                     True),
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

# defining items
item = {
    'blade': Item("blade", "a vorpal blade."),
    'torch': Item("torch", "a burning torch."),
    'stick': Item("stick", "A pointed stick!"),
    'treasure': Item("treasure", "a gold dubloon.")
}

# put them in rooms
room['foyer'].items.append(item['stick'])
room['overlook'].items.append(item['blade'])
room['outside'].items.append(item['torch'])
room['treasure'].items.append(item['treasure'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

playername = input("\nenter your name.\n")


player_inst = Player(playername, room['outside'])
a_bandersnatch = Bandersnatch(current_room=room['treasure'])

playerinput = None
while playerinput != 'q':

    control_mapping = {
            "n":player_inst.current_room.n_to,
            "e":player_inst.current_room.e_to,
            "s":player_inst.current_room.s_to,
            "w":player_inst.current_room.w_to,
        }

    valid_directions = [x for x in ['n','e','s','w'] if control_mapping[x] is not None]


    print(f"\n{player_inst.name}'s location: {player_inst.current_room.name}")

    if player_inst.current_room.is_lit:
        print(player_inst.current_room.description)
        print(f'valid directions: {valid_directions}')
        print(f'available items: {player_inst.current_room.items}.')

    if player_inst.current_room.name == a_bandersnatch.current_room.name:
        print("The Perfidious Bandersnatch is in the room with you!")

    playerinput = input("\nenter a command - n, e, s, w, i, take [item], drop [item], q.\n")
    if playerinput[0] not in ['n','e','s','w', 'i', 't', 'g', 'd', 'q']:
        print("invalid command.")

    elif playerinput in ['n','e','s','w']:
        player_inst.move(playerinput)
        a_bandersnatch.move()

    elif playerinput == 'i':
        print("your inventory contains:")
        [print(item) for item in player_inst.inventory]

    elif len(playerinput.split()) == 2:
        if playerinput.split()[0] == ('take' or 'get'):
            player_inst.take_item(playerinput.split()[1])
        elif playerinput.split()[0] == 'drop':
            player_inst.drop_item(playerinput.split()[1])

    else:
        pass



quit()
    
