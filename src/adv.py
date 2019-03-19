from room import Room
from player import Player
import os

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
# 
# New game:
os.system("clear")
name = input("Welcome, what is your name new player: ")
player = Player(name, "fighter", "elf", {"agi": 5, "str": 5, "int": 5, "vit": 5, "dex": 5, "pie": 5},[{1: {"name": "rusty sword"}}])
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

help = False
while True:
  os.system("clear")
  if help == False:
    print('(enter "h" for help)')
  else:
    print('Help:\nn: move north\ne: move east\ns: move south\nw: move west\nq: quit\nh: toggle help')
  print(player.currentRoom())
  cmd = input("Type your command: ")
  print(cmd)
  if cmd == "q":
    print("Goodbye!")
    break
  if cmd == "h":
    help = not help
  if cmd == "n":
    if room[player.rname].n_to is None:
      print("<can't move north>")
    else:
    #if 'n_to' in room[player.rname].keys():
      player.rdescription = room[player.rname].n_to.rdescription
      player.rname = room[player.rname].n_to.rname
  else:
    print("<not a command>")
