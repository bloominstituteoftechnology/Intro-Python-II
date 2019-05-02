from room import Room
from player import Player


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", "Storage: item13, Item14, Item15"),

    'foyer':    Room("Foyer", "Storage: item1, Item2, Item3", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", "Storage: item4, Item5, Item6", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", "Storage: item7, Item8, Item9", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", "Storage: item10, Item11, Item12", """You've found the long-lost treasure
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

while not cmd == "q":
    cmd = cmd.lower()
    print(player.currentRoom)

    bracket = '\n**********************************\n'
    print(bracket)
    print(player.currentRoom)
    location = room[player.currentRoom]
    print(location.description)
    print(bracket)
    if cmd == 'n':
        print(location.n_to)
        player.currentRoom = location.n_to
        print(player.currentRoom)
    elif cmd == 'q':
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



