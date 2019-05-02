from room import Room
from player import *

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
def main():
    # Make a new player object that is currently in the 'outside' room.
    

    # Write a loop that:
    #
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
    print()
    print("******** WELCOME TO THE *********")
    print("**** ULTIMATE ADVENTURE GAME ****")
    mario = Player("Mario", room['outside'])
    currentRoom = mario.currentRoom
    print("\nCurrent Room: " + currentRoom.name)
    print(f"Room Description: {currentRoom.description}")

    action_input = input("\nEnter in a cardinal direction\n[N] for North, [E] for East, [S] for South, [W] for West and [Q] to Quit\n ")
    #print(mario)

    while action_input.lower() != 'q':
        
        if action_input.lower() == 'n':
            try:
                mario.currentRoom = currentRoom.n_to
                print("Going North")
            except:
                print("Nope. Can't go that way.")
        elif action_input.lower() == 'e':
            try:
                mario.currentRoom = currentRoom.e_to
                print("Going East")
            except:
                print("Uh-oh edge of the Earth. Choose another direction.")
        elif action_input.lower() == 's':
            try:
                mario.currentRoom = currentRoom.s_to
                print("Going South")
            except:
                print("An immovable wall blocks you pass.")
        elif action_input.lower() == 'w':
            try:
                mario.currentRoom = currentRoom.w_to
                print("Going West")
            except:
                print("Nah brah.")        
        else:
            print("Action is not valid.")
        currentRoom = mario.currentRoom
        #print(f"Current room: {currentRoom.name}")
        print("\nCurrent Room: " + currentRoom.name)
        print(f"Room Description: {currentRoom.description}")
        action_input = input("\nEnter in a cardinal direction\n[N] for North, [E] for East, [S] for South, [W] for West and [Q] to Quit\n ")
    print("Thanks for playing. Have a nice life...")

main()