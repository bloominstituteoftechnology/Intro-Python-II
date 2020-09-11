from room import Room
from player import Player
from item import Item
from secret import Secret
from writing import Writing

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

    'hollow': Room("Secret Hollow", """A few dozen feet down the cliff you come upon
    a hollow space in the face of the cliff. As the wind howls you see sitting on
    an ancient altar is a solid gold monkey idol with diamond eyes""")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['overlook'].c_to = room['hollow']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['hollow'].c_to = room['overlook']

# Create items
sword = Secret('Sword', 3, 12)
diamond = Item('Diamond', 30)
wand = Secret('Wand', 30, 45)
shield = Item('Shield', 4)
note = Writing('Note', 0, '"Check out the Cliff to \ndiscover a secret treasure"')
idol = Item('Solid gold idol', 500)


# Add items to rooms
room['foyer'].secrets.append(sword)
room['narrow'].secrets.append(wand)
room['narrow'].items.append(shield)
room['overlook'].items.append(diamond)
room['treasure'].items.append(note)

# Add secrets to rooms


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player(room['outside'])

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

playing = None
menu = input(f'Welcome to Darkest Dungeons! To play press p to quit press q\n')
if menu == 'q':
    print('Thanks For Playing!')
    playing = False
elif menu == 'p':
    print('\nEnter n, s, e, w to go in any of the cardinal directions available in each room!\nTo investigate a room enter i')
    playing = True
while playing:
    action = input(f'\n{player1.currentRoom}choose a direction or investigate!\n')

    if action == 'n' and player1.currentRoom.n_to != None:
        player1.currentRoom = player1.currentRoom.n_to
    
    elif action == 's' and player1.currentRoom.s_to != None:
        player1.currentRoom = player1.currentRoom.s_to
    
    elif action == 'e' and player1.currentRoom.e_to != None:
        player1.currentRoom = player1.currentRoom.e_to
    
    elif action == 'w' and player1.currentRoom.w_to != None:
        player1.currentRoom = player1.currentRoom.w_to

    elif action == 'c' and player1.currentRoom.c_to != None:
        player1.currentRoom = player1.currentRoom.c_to
    
    elif action == 'i':
        player1.investigate()

    elif action == 'p':
        item = input('Enter item\'s name ')
        for thing in player1.currentRoom.items:
            if item == thing.name and thing.hidden == False:
                player1.get(item)
            else:
                print(f'There is no {item} to pick up')

    elif action == 'q':
        print('\nThanks For Playing')
        playing = False
    
    else:
        print('\nPlease choose a valid direction!')