from room import Room
from player import Player

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
  print(f'\n Current Room Name => {room[player.location].name} \n')
  print(f' \n Location description => {room[player.location].description} \n')
  user_input = input('\n <Command ').strip().lower()
  if user_input == 'q':
    done = not done
  elif user_input in ['w', 'n', 's', 'e']:
    if hasattr(room[player.location], f'{user_input}_to'):
      key = f'{user_input}_to'
      print(key, player.location, room[player.location])
      mykey = getattr(room[player.location], key)
      print('\n MY KEEEYYYY', mykey.name.lower())
      lst = ['outside', 'foyer','overlook','narrow', 'treasure']
      print([extension for extension in lst if(extension in mykey.name.lower())])        
      new_location = [extension for extension in lst if(extension in mykey.name.lower())]
      print(new_location[0])
      player.location = new_location[0]
  else:
    print(f'unknown command {user_input}')
# If the user enters "q", quit the game.
