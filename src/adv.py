from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Laboratory Entrance", """North of you, the door to the laboratory is slightly ajar"""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Hallways lit by red emergency lights run north and east."""),

    'storage': Room("Storage Room", """A room with stuff to be discussed later. A door in some direction is locked"""),

    'crawl':   Room("Crawl Space", """The East hallway ends in rubble, impassible, however a small panel is removed exposing a small tunnel heading further north."""),

    'control': Room("Control Room", """You enter what seemed to have been the control room for the laboratory. Unfortunately no power seems to be connected to the room, making it useless. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['storage']
room['foyer'].e_to = room['crawl']
room['storage'].s_to = room['foyer']
room['crawl'].s_to = room['foyer']
room['crawl'].n_to = room['control']
room['control'].s_to = room['crawl']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

p1 = Player(You, outside )

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

while True: 
    #print current room
    #print room description

    direction = input("What direction would you like to go? (n,e,s,w")

    if direction == "q":
        #function to finish game
        #finishGame()
    elif direction == "n":
        #currentRoom.n_to?