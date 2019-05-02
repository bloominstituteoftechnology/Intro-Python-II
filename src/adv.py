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

    'narrow':   Room("Narrow Passage",  """The narrow passage bends here from west
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
player = Player('Sergey', 'outside')
print(player)
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

cmd = input("Hi! type your name to start the game:")
# player = Player(cmd, "outside")

print(player.currentRoom)



while  cmd.lower() != 'q':
    
    bracket = '\n**********************************\n'
    print(bracket)
    print(player.currentRoom)
    location = room[player.currentRoom]
    print(location.description)
    print(bracket)
    
    if cmd.lower() == 'n':
        try:
            print(location.n_to)
            player.currentRoom = location.n_to
        except:
            print(player.currentRoom)
    elif cmd.lower() == 's':
        print(location.s_to)
        player.currentRoom = location.s_to
        print(player.currentRoom)
    elif cmd.lower() == 'e':
        print(location.e_to)
        player.currentRoom = location.e_to
        print(player.currentRoom)
    elif cmd.lower() == 'w':
        print(location.w_to)
        player.currentRoom = location.w_to
        print(player.currentRoom)
    elif cmd.lower() == 'q':
        print('Exit the game')
        break

def find_item(name, current_room):
    for i in current_room.inventory:
        if i.name == name:
            return i
    return None



def move_to(direction, current_room):
    attribute = direction + '_to'

    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)
    
    else:
        print("Not a valid room")
        return current_room



