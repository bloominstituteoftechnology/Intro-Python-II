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

# Declare all items

items = {
    'potion': Item('Apple Gel', 'Recovers 25 HP'),

    'elixer': Item('Orange Gel', 'Recovers 25 MP'),

    'shield': Item('Aegis', 'Legendary shield of Zeus'),

    'katana': Item('Masamune', 'A blade that can cut through anything'),

    'sword': Item('Sword of GouJian', 'Ancient sword from the East'),

    'spear': Item('Gae Bolg', 'A cursed spear once wielded by ChuCulain'),

    'tome': Item('Dire Thunder', 'A magic book that summons thunder against enemies')
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

player = Player(room['outside'])

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

#helper function to store new room into current room

def travel (player, room, attr):
    if hasattr(room, attr):
        new_room = getattr(room, attr)
        print("to " + new_room.name)
        player.relocate(new_room)
    else:
        print("You cannot travel in that direction")
   


while True:
    print(f"{player.at_room}\n")
    print("You can: \n")
    print("Enter in direction letter to move north(n), east(e), south(s), west(w)\n")
    print ("'items' to check your items in your inventory\n")
    print("'search' to seach room or area\n")
    print("'take' to take item\n")
    print("'drop' to drop item\n") 
    print("'q' to quit game\n")  

    cmd = input("Pick an action:")

# If the user enters "q", quit the game.
    if cmd == "q":
        break
# If the user enters a cardinal direction, attempt to move to the room there.
    elif cmd == "n":
        print('Moved North')
        attr = cmd + '_to'
        travel(player, player.at_room, attr)
        pass
    elif cmd == "e":
        print('Moved East')
        attr = cmd + '_to'
        travel(player, player.at_room, attr)
        pass
    elif cmd == "s":
        print('Moved South')
        attr = cmd + '_to'
        travel(player, player.at_room, attr)
        pass
    elif cmd == "w":
        print('Moved West')
        attr = cmd + '_to'
        travel(player, player.at_room, attr)
        pass
