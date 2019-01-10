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


pc = Player("Default", room["outside"], [], 50)
location = pc.location

print("You wake up, you only remember your name")
pc.name = input("What is your name: ")
print(f"Welcome, {pc.name}, your adventure begins.")
print("""---------------------------------------------------
  
  
  """)
print(location.desc)
print("""---------------------------------------------------
  
  
  """)
# make this a function
entry = input("""What will you do?
Move: n, e, s, w
Check Location: c
Investigate Room: i
: """)
# try newLocation variable, and have the location change be assigned to newLocation before the True check, so that player location doesnt get lost
# then assign location to new location of True check succeed
if entry == "n":
    if location.desc:
        location = pc.location.n_to
        print("You go North")
elif entry == "e":
    if location.desc:
        location = pc.location.e_to
        print("You go East")
elif entry == 's':
    if location.desc:
        location = pc.location.s_to
        print("You go South")
elif entry == "w":
    if location.desc:
        location = pc.location.w_tp
        print("You go West")
print("""---------------------------------------------------

  
  
  """)
if location.desc:
    print(location.desc)
else:
    print("You see no way forward in that direction")


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
