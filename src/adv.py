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


sword = Item("Sword", "cutting through flesh")
axe = Item("Axe", "battle axe")
torch = Item("Torch", "torch")
dagger = Item("Dagger", "hunting")
gold = Item("Gold", "Yea Buddy")

room['outside'].items = []
room['foyer'].items = [torch]
room['overlook'].items = [dagger]
room['narrow'].items = [axe, sword]
room['treasure'].items = [gold]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newPlayer =Player('Dave', room['outside'])
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

while True:
    action = input('Enter an action: ')
    if action == 'start':
        if newPlayer.current_room:
            print(f'{newPlayer.current_room}')
        else:
            print('no path in that direction')
    if action == 'n':
        if newPlayer.current_room.n_to:    
            newPlayer.current_room=newPlayer.current_room.n_to
            print(f'{newPlayer.current_room}')
        else: 
            print('you cannot go north')
    if action == 's':
        if newPlayer.current_room.s_to:
            newPlayer.current_room=newPlayer.current_room.s_to
            print(f'{newPlayer.current_room}')
        else:
            print('no path in that direction')
    if action == 'e':
        if newPlayer.current_room.e_to:
            newPlayer.current_room=newPlayer.current_room.e_to
            print(f'{newPlayer.current_room}')
        else:
            print('no path in that direction')
    if action == 'w':
        if newPlayer.current_room.w_to:
            newPlayer.current_room=newPlayer.current_room.w_to
            print(f'{newPlayer.current_room}')
        else:
            print('no path in that direction')
    if action == 'q':
       exit()

    if action == 'look':
        if newPlayer.current_room.items:
            for obj in newPlayer.current_room.items:    
                print(obj.name)
        else:
            print('no items in your room')
