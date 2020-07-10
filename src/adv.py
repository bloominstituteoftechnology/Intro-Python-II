from room import Room
from player import Player
from itemDictionary import item

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

# Make a new player object that is currently in the 'outside' room
name = input('\nHello adventurer. What is your name?\n')
player = Player(name, room['outside'])
player.inventory = item

while True:
  currentLocation = player.location
  print(currentLocation)
  print(player.inventory)
  print(currentLocation.items)
  choice = input('What would ' + name + ' like to do next? \n m(Move location) || c(Check Something): ') 

  if choice[0].lower() == 'm':
    player.move()

  if choice[0].lower() == 'c':
    check = input('What would ' + name + ' like to check? \n i(inventory) || r(Room): ')
    if check[0].lower() == 'i':
      player.checkInventory()
    if check[0].lower() == 'r':
      player.checkRoom()

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
