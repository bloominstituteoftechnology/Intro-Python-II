from room import Room
from player import Player
from items import Item

# Declare all the rooms
item = {
  'lamp': Item("Lamp","You'll be able to see thru the darkness and explore"),
  'MP5': Item("MP5", "A Submachine gun that might be able to keep your wasted life alive. Dont get to happy because it is still missing the magazine"),
  'spinach': Item("Spinach", "Will keep you fed. So you won't starve to death."),
  'clock': Item("Clock", "This will be handy to check the time."),
  'backpack': Item("Backpack", "Will add more slots to your inventory"),
  'map': Item("Map", "Its a second pair of eyes. This map will help you set your bearings straight."),
  'golden-key': Item("Golden-key", "You found this golden key on the middle of the floor."),
  'treasure-chest': Item("Treasure-chest", "Empty...."),
  'magazine': Item("Magazine", "A double-column straight box magazine, with a capacity of 30 rounds. "),
  }

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['lamp'], item['MP5'], item['map']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item['clock'], item['backpack']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item['spinach'], item['golden-key']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item['magazine']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item['treasure-chest']]),
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
player = Player('outside')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
done = False
while not done:
  print(f'\n \033[37m Current Room Name => \033[32m {room[player.location].name} \n')
  print(f'\n \033[37m Location description => \033[32m {room[player.location].description} \n')
  print(f'\n \033[37m Room Items => \033[32m {room[player.location].items} \n')

  user_input = input('\n \033[37m <Command ').strip().lower()
  if user_input == 'q':
    print('\033[37m')
    done = not done
  elif user_input in ['w', 'n', 's', 'e']:
    if hasattr(room[player.location], f'{user_input}_to'):
      key = f'{user_input}_to'
      my_key = getattr(room[player.location], key)
      lst = ['outside', 'foyer','overlook','narrow', 'treasure']
      player.moveTo(lst, my_key)
  else:
    # print(f'unknown command {user_input}')
    print('\033[31m' + f'unknown command {user_input}')
    print('\033[37m')

# If the user enters "q", quit the game.
