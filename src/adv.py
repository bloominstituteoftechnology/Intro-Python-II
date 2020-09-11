from room import Room
from player import Player
from item import Item
from enemy import Enemy
import os

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'throne':   Room("Throne Room", "!--- BATTLE ---!\nA giant Guardian stands ominously in the center of the Throne Room. The only way out of here is to fight him!"),

    'dungeon':  Room("Dungeon", "Down the stairs from the narrow you enter the dungeon. A place filled with a tormented history."),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! 
    Fill your pockets with all the gold they can carry and when you're ready, 
    exit to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['throne']
room['dungeon'].n_to = room['narrow']
room['narrow'].s_to = room['dungeon']
room['throne'].n_to = room['treasure']
room['throne'].s_to = room['narrow']
room['treasure'].s_to = room['throne']

#
# Main
#

# Add items to rooms
room['foyer'].add_item(Item("Sword", "An old rusty blade, but still dangerous in the right hands."))
room['dungeon'].add_item(Item("Armour", "Steel armour, it has seen its share of battle but will still provide much needed protection from any *Enemies close-by"))
room['treasure'].add_item(Item("Treasure", "It's the long lost Ogre King's treasure!"))

# Make a new player object that is currently in the 'outside' room.
print("WELCOME TO PYTHON ADVENTURE GAME!!!")
player_name = input("Please enter your name --> ")
player = Player(player_name, room["outside"], 200, 100)
print(f"\n---------- Welcome {player.name}! Get ready to start your adventure! ----------\n*press 'q' to quit\n")

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

# LOGIC FUNCTIONS
def check_items_in_room():
  items_in_room = ""
  if len(player.current_room.items) > 0:
    print("-------------------------------------------------------\n")
    print(f"Items in room:")
    for item in player.current_room.items:
      items_in_room += f"{item.name}\n"
    print(items_in_room)
    print("-------------------------------------------------------")

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

# DECLARE ENEMIES
guardian = Player("Guardian", room['throne'], 100, 50)

# PROPERTIES
playing = True
possible_directions = ["n", "s", "e", "w"]
fighting_actions = ["atk", "i", "take", "drop"]
item_action_done = False
fighting_enemy = False

# GAME LOOP
while playing == True:

    for item in player.items:
      if item.name == "Sword":
        player.atk = 300
      elif item.name == "Armour":
        player.hp = 300

    if player.current_room.name == "Throne Room":
      print("In the throne room")
      fighting_enemy = True

    while fighting_enemy == True:
      guardian.attack(player)
      
      if player.hp <= 0:
        print("YOU DIED!")
        playing = False
        break
      elif guardian.hp <= 0:
        print("YOU SLAYED THE GUARDIAN!!\nYou may now enter the Treasure Room!")
        fighting_enemy = False
        break

      
      fighting_cmd = input("""
    Choose an action:
      Fight          = [atk]
      Show Inventory = [i]
      Take Item      = [take *item]
      Drop Item      = [drop *item]
    --> """).lower()

      split_fight_cmd = fighting_cmd.split()

      atk_cmd = split_fight_cmd[0]
      print(atk_cmd)

      if atk_cmd in fighting_actions:
        if atk_cmd == "atk":
          print("attttackckcing")
          player.attack(guardian)
      else:
        print("\n--- Error: Please select a valid action ---\n")

    if playing == False:
      break

    print("-------------------------------------------------------")
    print(f"Location: \033[1m{player.current_room.name}\033[0m")
    print(player.current_room.description)

    check_items_in_room()

    selected_direction = input("""
  Choose an action:
    Move           = [n, s, e, w]
    Show Inventory = [i]
    Take Item      = [take *item]
    Drop Item      = [drop *item]
  --> """).lower()
  
    split_cmd = selected_direction.split()

    if len(split_cmd) == 1:

      if selected_direction == "q":
          print("\n--- Thank you for playing the game ---")
          playing = False
          break

      elif selected_direction == "i":
        cls()
        player.show_inventory()
      elif selected_direction in possible_directions:
          try:
              cls()
              player.move(selected_direction)
          except:
              print("-------------------------------------------------------")
              print("--- You bump into a wall ---")
      else:
          print("\n--- Error: Please select a valid action ---\n")
          cls()
    
    elif len(split_cmd) == 2:
      command = (split_cmd[0])
      item_cmd = (split_cmd[1]).title()

      #take/drop logic
      if command == "take":
        cls()
        for item in player.current_room.items:
          if item.name == item_cmd:
            player.take_item(item, player.current_room.name)
            player.current_room.remove_item(item)
          else:
            print(f"{item_cmd} not in here")
      elif command == "drop":
        cls()
        for item in player.items:
          if item.name == item_cmd:
            player.drop_item(item)
      else:
        cls()
        print("--- Did not understand command ---")

    else:
      cls()
      print("--- Did not understand command ---")

