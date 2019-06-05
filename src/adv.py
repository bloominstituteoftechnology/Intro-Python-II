from room import Room

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
def main():

# Make a new player object that is currently in the 'outside' room.
    drip = Player("Drip", 'outside')
    print("Enjoy This Adventure")

# Write a loop that:
action_input = input("Enter a cardinal direction\n[N] for North, [E] for East, [S] for South, [W] for West, and [Q] to Quit")
while action_input.lower() != 'q':
        if action_input.lower() == 'n':
            print("Going North")
        elif action_input.lower() == 'e':
            print("Going East")
        elif action_input.lower() == 's':
            print("Going South")
        elif action_input.lower() == 'w':
            print("Going West")
        else:
            print("Action is not valid.")
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
