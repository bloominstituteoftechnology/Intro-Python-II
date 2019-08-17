from room import Room
from player import Player
from player import PlayerInventory

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items = {'candle': 'Looks new', 'Notepad': "There is writing on it, but it is not legible"}),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", items = {'Stick': 'Just a stick', 'Rock': "Just a rock. Shape is a bit interesting though."}),

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

# Player inventory

player_inventory = PlayerInventory(items=None)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print("Welcome to THE MOST AWSOME ADVENTURE EVER!!\n\nThis adventure starts when you find yourself wondering in the great woods. You are a young adventurer keen on making a name for yourself as a great treasure hunter.\nCan you find your first treasure?\n")
player = Player(input("Please enter your character name: "), room['outside'], player_inventory)

print(f'\n{player.current_room}\n')

action = input("Where would you like to move? Move North(n), South(s), East(e), or West(w) \nView Inventory(i) \nPick Up Item(p) \nQuit Game(q)\n\n")

player.action_input(action)

# Write a loop that:
while True:
    if action == 'q':
        break
    elif player.current_room is not None:
        player.display_room()
        action = input("Where would you like to move next? Move North(n), South(s), East(e), or West(w) \nView(i) \nPick Up Item(p) \nQuit Game(q)\n\n")
        player.action_input(action)
        continue
    else:
        print("This room does not exist. Please try again.")  # Else is not being used

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



