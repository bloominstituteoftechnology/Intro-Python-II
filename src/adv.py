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

player_items = [Item("pencil", "A wooden instrument for drawing."),
                Item("glasses", "They help with sight.")]

room_items = [Item("ink well", "Some ink to write with."),
              Item("shoe", "A shoe.")]

# Link rooms together

room['outside'].items = room_items

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

player = Player(room['outside'], items = player_items)

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

def swap_item(name, cont1, cont2):
  """ Given two containers, try finding an item by name, and
      swap the item from cont1 to cont2.
  """
  found = False
  index = 0
  while not found and index < len(cont1.items):
    if cont1.items[index].name == name:
      found = True
    else:
      index += 1

  if not found:
    return False 

  item = cont1.items.pop(index)
  cont2.items.append(item)

  return True

endQ = False

while not endQ:
  print(player.room.name)
  print(player.room.description)
  inp = input("What do you want to do?: ").split(" ")

  if inp[0] == "q":
    endQ = True

  elif inp[0] in ["n", "N"]:
    dest = player.room.n_to
    if dest:
      player.room = dest
    else:
      print("There is no way to go north from here.")

  elif inp[0] in ["s", "S"]:
    dest = player.room.s_to
    if dest:
      player.room = dest
    else:
      print("There is no way to go south from here.")

  elif inp[0] in ["e", "E"]:
    dest = player.room.e_to
    if dest:
      player.room = dest
    else:
      print("There is no way to go east from here.")

  elif inp[0] in ["w", "W"]:
    dest = player.room.w_to
    if dest:
      player.room = dest
    else:
      print("There is no way to go west from here.")

  elif inp[0] in ["i", "inventory", "Inventory"]:
    inv = [ print(i.name + ":\n  ", i.description) for i in player.items ]
    if len(inv) == 0:
      print("You are holding no items.")

  elif inp[0] in ["l", "look", "Look"]:
    inv = [ print(i.name + ":\n  ", i.description) for i in player.room.items ]
    if len(inv) == 0:
      print("There are no items in this room.")

  elif inp[0] in ["d", "drop", "Drop"]:
    if len(inp) < 2:
      print("What to drop?")
    else:
      name = " ".join(inp[1:])
      if swap_item(name, player, player.room):
        print(f"Dropped the \"{name}\".")
      else:
        print(f"You don't have \"{name}\".")

  elif inp[0] in ["g", "get", "Get"]:
    if len(inp) < 2:
      print("What to get?")
    else:
      name = " ".join(inp[1:])
      if swap_item(name, player.room, player):
        print(f"Got the \"{name}\".")
      else:
        print(f"There aren't any \"{name}\" in this room")

  elif inp[0] in ["debug"]:
    print(player)
  print("\n")

