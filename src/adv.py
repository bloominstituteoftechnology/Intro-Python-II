from room import Room
from player import Player
from item import Item
import os

# Declare all the items
#for now itemId will be it's index in this list
items = [
  Item(0, "a rusty sword", "better than a stick..."),
  Item(1, "a damaged buckler", "not sure how many hits this can take..."),
  Item(2, "a bronze key", "what door does this go to?"),
  Item(3, "a blue ribbon", "it looks fancy..."),
  Item(4, "a radian diamond", "you could probably sell this for a lot..."),
  Item(5, "a curious doll", "it looks spooky...")
]

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [items[5]]),

    'foyer':    Room("Foyer", 
                      """Dim light filters in from the south. Dusty
passages run north and east.""",
                      []),

    'overlook': Room("Grand Overlook", 
                      """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                      [items[4]]),

    'narrow':   Room("Narrow Passage", 
                      """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                      [items[3]]),

    'treasure': Room("Treasure Chamber", 
                      """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                      []),
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
stats = {"agi": 5, "str": 5, "int": 5, "vit": 5, "dex": 5, "pie": 5}
inventory = [items[0], items[1]]
player = Player(name, "fighter", "elf", stats, inventory, room['outside'])
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

def convertCmdtoDir(cmd):
  if cmd == 'n':
    return 'north'
  if cmd == 's':
    return 'south'
  if cmd == 'e':
    return 'east'
  if cmd == 'w':
    return 'west'

helpFlag = False
inventoryFlag = False
currentRoomShortName = 'outside'
while True:
  os.system("clear")

  if helpFlag == False:
    print('(enter "h" for help)')
  else:
    print('Help:\nn: move north\ne: move east\ns: move south\nw: move west\ni: toggle player inventory\nq: quit\nh: toggle help')
  
  print(player.currentRoom())
  if len(player.Room.inventory) > 0:
    print('Nearby you see:')
    for item in player.Room.inventory:
      print(item)
    print('\n')

  if inventoryFlag == True:
    print('Player Inventory: (toggle "i")')
    for item in player.inventory:
      print(item)
    print('\n')

  print('------------------------------------------')
  cmd = input("Type your command: ")

  if cmd == "q":
    print("Goodbye!")
    break

  if cmd == "h":
    helpFlag = not helpFlag

  if cmd == "i":
    inventoryFlag = not inventoryFlag

  if cmd == "n" or cmd == "s" or cmd == "e" or cmd == "w":
    direction = convertCmdtoDir(cmd)
    if getattr(player.Room, cmd+'_to') is None:
      print("*can't move" + direction + "*")
      input("press enter to continue")
    else:
      player.Room = getattr(player.Room, cmd+'_to')

  if 'take' in cmd.lower() or 'get' in cmd.lower():
    print(cmd[len(cmd)-1])
    itemId = int(cmd[len(cmd)-1])
    if player.Room.removeItem(items[itemId]) is True:
      player.addItem(items[itemId])

  if 'drop' in cmd.lower():
    print(cmd[len(cmd)-1])
    itemId = int(cmd[len(cmd)-1])
    if player.removeItem(items[itemId]) is True:
      player.Room.addItem(items[itemId])

  else:
    print("*not a command*")
