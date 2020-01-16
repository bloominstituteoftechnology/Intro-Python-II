from room import Room
from player import Player
from item import Item
import os
from gold import Gold


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

'Room1': Room("Room 1", """You've found the long-lost room 1! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

'Room2': Room("Room 2", """You've found the long-lost room 2! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),


}

#Items

health_pot = Item("Health Potion", "Take a lickin and keep on kickin")
shield = Item("Shield", "Protects you from the bad ouchy things")
sword = Item("sword", "The pointy bit faces away from you")
poison_apple = Item("Browning apple", "It doesn't look like the kind of apple you would want to eat")

#put the stuff in the places

room['treasure'].items = [shield, sword]
room['foyer'].items = [health_pot]
room['narrow'].items = [poison_apple]
room['outside'].items = [health_pot]


#random bits of gold



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].e_to = room['Room1']
room['Room1'].w_to = room ['treasure']
room['Room1'].e_to = room ['Room2']
room['Room2'].w_to = room ['Room1']

#
# Main
#



# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'])



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


def direction(d, currentRoom):

    attrib = d + '_to'

    if hasattr(currentRoom, attrib):
        return getattr(currentRoom, attrib)
    else:
        print("There is nothing there, you cannot go forward")

    return currentRoom

done = False

while not done:
    print('\nWelcome! Press N,S,W,E to move around!')
    print(f'\n{player.currentRoom}\n')
    print(f'\n{player.currentRoom.description}\n')
  

 

    user_input = input("\nType direction to go: ").strip().lower().split()

    if len(user_input) != 1:
        print('That is a weird command my dude Type n,s,w, or e')
        continue

    if  user_input[0] == 'q':
        done = True

    if user_input[0] in ["get item"]:
        player.add_item
        print(player.inventory)
    

    elif user_input[0] in ["n", "north", "s", "south", "w", "west", "e", "east"]:
        player.currentRoom = direction(user_input[0], player.currentRoom)

    
    else:
        unknown_input = user_input[0]
        print('I do not know what you are saying ', unknown_input)