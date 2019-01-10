from room import Room
from player import Player
from item import Item

# Declare all the rooms

# item = {

# }

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

# name of the room to the instance of each room 
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
# . notation accessing attribute on a class 
# bracket notation for dictionary

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
# print(player)

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

def try_direction(direction, current_room):
  attribute = direction + '_to'
  
  if hasattr(current_room, attribute):
    return getattr(current_room, attribute)
  else: 
    print("You can't go that way")
    return current_room

done = False

while not done:
  # currentRoom = player.current_room
  s = input().lower().split()
  print(s)
  s = s[0] #b/c of split it returns a list
  print(s, " this is s")
  # split to get rid of white space
  print(f'This is the current room {player.current_room.name}')
  print((player.current_room.description))

  if s in ['n', 's', 'e', 'w']:
    player.current_room = try_direction(s, player.current_room)
  elif s == 'q':
    done = not done
  else: print(f'unknown command "{s}"')
  

