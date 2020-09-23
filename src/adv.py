from instantiate import room
from player import Player
from room import Room
from item import Item
from functions import print_slow
import sys

#
# Main
#


# Make a new player object that is currently in the 'entrance' room.
player = Player()
player.current_room = room['entrance']

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

# Intro and instructions
print_slow('You wake up at the entrance of a mansion\nYou notice a piece of paper in your hand, it reads\n\"Find the Cybertruck.\"\n')
print_slow('You see a hallway to your north, a door to your east and west, and no exit behind you.\n')
print_slow('Enter \'n\', \'e\', \'s\', or \'w\' to move around.\n')
print_slow('Type \'search\' in any room to look for items in that room\n')
print_slow('To see what items you have, type \'items\'.\n\n')
print_slow('To quit type \'q\'\n')
print_slow('PRO TIP: Keep track of where you are so you don\'t get lost!\n\n')

while player.foundTruck == False:
    action = input('Move or search? (n, e, s, w, or search): ').upper()
    print('\n')
    if action == 'SEARCH':
        player.search()
    elif action == 'ITEMS':
        player.checkInventory()
    elif action[0] in ['N', 'E', 'S', 'W']:
        player.move(action)
    elif action == 'Q':
        sys.exit()
    else:
        print_slow('Incorrect input')

    if player.current_room.name == room['cybertruck'].name:
        player.foundTruck = True

take_job = input('Do you take the job? (Y/N): ').upper()
if take_job == 'Y':
    print_slow('\nCongratulations! You managed to find the Cybertruck and get a job! Well done!\n')
elif take_job == 'N':
    print_slow('\nSad Elon is sad, but you still managed to find the Cybertruck!\n')

input('Press \'Enter\' to exit!')