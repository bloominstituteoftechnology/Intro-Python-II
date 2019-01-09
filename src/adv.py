from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('wand', 'Does not really work well, in really rough shape')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('sword', 'Looks as if it were just sharpened. Too bad its merely a training sword')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('potion', 'This can heal your health 25 points')]),

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


inits = 'Start of Game'
location = 'outside'

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Austin')
current_room = room['outside']

#============== FUNCTIONS ====================#


# moves player to user given direction
def move_area(p_inpt):
    global current_room
    if p_inpt == 'n':
        new_room = current_room.n_to
        current_room = new_room
        print(f"You are now at the {current_room.name}. {current_room.description}.")
        if len(current_room.items) > 0:
            print(f"You see a {current_room.items[0]}.")
    elif p_inpt == 's':
        new_room = current_room.s_to
        current_room = new_room
        print(f"You are now at the {current_room.name}. {current_room.description}")
    elif p_inpt == 'e':
        new_room = current_room.e_to
        current_room = new_room
        print(f"You are now at the {current_room.name}. {current_room.description}")
    elif p_inpt == 'w':
        new_room = current_room.w_to
        current_room = new_room
        print(f"You are now at the {current_room.name}. {current_room.description}")
    else:
        print('That is not a direction!')






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

print(f"\n Welcome to your first adventure, {player.name}! \n Use 'n' to go North \n Use 's' to go South \n Use 'w' to go West \n Use 'e' to go East \n Press 'q' to quit game" )

while not inits[0] == 'q':
    if current_room == room['outside']:
        print(f'You are currently {current_room}')
    else:
        print('\n<=========================================> \n')
    

    inits = input('Enter a direction: \n')
    move_area(inits)

    if len(current_room.items) > 0:
        inits = input('Would you like to pick up an Item?: \n').split(' ')
        if inits[0] == 'get':
            for i in current_room.items:
                if inits[1] == i.name:
                    player.items.append(i)
                    print(f"You have picked up the {i.name}")