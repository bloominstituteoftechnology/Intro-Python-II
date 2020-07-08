import textwrap
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


def adventure_awaits():

    new_name = input("\nEnter Your NAME! Adventure Awaits...\n-->  ")
    current_player = Player(new_name, "outside")
    playing = True
    print(f"\nHello {current_player.name}!\nExplore rooms and obtain treasure! \nAdventure Awaits!\n")
   
    while (playing):
        wrapper = textwrap.TextWrapper(width=70)
        room_description = wrapper.wrap(
            text=room[current_player.room].description)

        # show heros current room and room description
        print(f"\nCurrent Room: \n{current_player.room}\n")
        print("Room Description: ")
        for every_line in room_description:
            print(every_line)

        # waits for user input to decide what to do next
        action = input("\n\nWhat shall the hero do next??? \ntype 'help' for a hint! \n-->  ")
        if (action == help):
            return "Enter a direction i.e. north, south, east, west to attempt to move to another location. \ntype 'q' to quit \n"
        elif (action == "north"):
            if (current_player.room == "outside"):
                current_player.room = "foyer"
            elif (current_player.room == "foyer"):
                current_player.room = "overlook"
            elif (current_player.room == "overlook"):
                print("You fell off the cliff!")
                leaving_game = True
                while (leaving_game):
                    try_again = input("Try Again? y/n? \n-->   ")
                    if (try_again == "y"):
                        current_player.room = "outside"
                        leaving_game = False
                    elif (try_again == "n"):
                        leaving_game = False
                        playing = False
                    else:
                        print("type 'y' to keep trying, 'n' to stop playing:  ")
            elif (current_player.room == "narrow"):
                current_player.room = "treasure"
            elif (current_player.room == "treasure"):
                print("You ran into a cave wall!") 
        elif (action == "south"):
            if (current_player.room == "outside"):
                print("You left the game!")
                leaving_game = True
                while (leaving_game):
                    try_again = input("Try Again? y/n? \n-->   ")
                    if (try_again == "y"):
                        current_player.room = "outside"
                        leaving_game = False
                    elif (try_again == "n"):
                        leaving_game = False
                        playing = False
                    else:
                        print("type 'y' to keep trying, 'n' to stop playing: \n-->  ")
            elif (current_player.room == "foyer"):
                current_player.room = "outside"
            elif (current_player.room == "overlook"):
                current_player.room = "foyer"
            elif (current_player.room == "narrow"):
                print("You fell off a ledge into spikes!")
                leaving_game = True
                while (leaving_game):
                    try_again = input("Try Again? y/n? \n-->   ")
                    if (try_again == "y"):
                        current_player.room = "outside"
                        leaving_game = False
                    elif (try_again == "n"):
                        leaving_game = False
                        playing = False
                    else:
                        print("type 'y' to keep trying, 'n' to stop playing: \n-->  ")
            elif (current_player.room == "treasure"):
                current_player.room = "narrow"
        elif (action == "east"):
            if (current_player.room == "outside"):
                print("You left the game!")
                leaving_game = True
                while (leaving_game):
                    try_again = input("Try Again? y/n? \n-->   ")
                    if (try_again == "y"):
                        current_player.room = "outside"
                        leaving_game = False
                    elif (try_again == "n"):
                        leaving_game = False
                        playing = False
                    else:
                        print("type 'y' to keep trying, 'n' to stop playing: \n-->  ")
            elif (current_player.room == "foyer"):
                current_player.room = "narrow"
            elif (current_player.room == "overlook"):
                print("You fell off the cliff!")
                leaving_game = True
                while (leaving_game):
                    try_again = input("Try Again? y/n? \n-->   ")
                    if (try_again == "y"):
                        current_player.room = "outside"
                        leaving_game = False
                    elif (try_again == "n"):
                        leaving_game = False
                        playing = False
                    else:
                        print("type 'y' to keep trying, 'n' to stop playing:  ")
            elif (current_player.room == "narrow"):
                print("You fell off the narrow ledge into spikes!")
                leaving_game = True
                while (leaving_game):
                    try_again = input("Try Again? y/n? \n-->   ")
                    if (try_again == "y"):
                        current_player.room = "outside"
                        leaving_game = False
                    elif (try_again == "n"):
                        leaving_game = False
                        playing = False
                    else:
                        print("type 'y' to keep trying, 'n' to stop playing:  ")
            elif (current_player.room == "treasure"):
                print("A cave bear ate you!")
                leaving_game = True
                while (leaving_game):
                    try_again = input("Try Again? y/n? \n-->   ")
                    if (try_again == "y"):
                        current_player.room = "outside"
                        leaving_game = False
                    elif (try_again == "n"):
                        leaving_game = False
                        playing = False
                    else:
                        print("type 'y' to keep trying, 'n' to stop playing:  ")
        elif (action == "west"):
            if (current_player.room == "outside"):
                print("You left the game!")
                leaving_game = True
                while (leaving_game):
                    try_again = input("Try Again? y/n? \n-->   ")
                    if (try_again == "y"):
                        current_player.room = "outside"
                        leaving_game = False
                    elif (try_again == "n"):
                        leaving_game = False
                        playing = False
                    else:
                        print("type 'y' to keep trying, 'n' to stop playing: \n-->  ")
            elif (current_player.room == "foyer"):
                print("A vampire spotted you and sucked your blood!")
                leaving_game = True
                while (leaving_game):
                    try_again = input("Try Again? y/n? \n-->   ")
                    if (try_again == "y"):
                        current_player.room = "outside"
                        leaving_game = False
                    elif (try_again == "n"):
                        leaving_game = False
                        playing = False
                    else:
                        print("type 'y' to keep trying, 'n' to stop playing:  ")
            elif (current_player.room == "overlook"):
                print("You fell off the cliff!")
                leaving_game = True
                while (leaving_game):
                    try_again = input("Try Again? y/n? \n-->   ")
                    if (try_again == "y"):
                        current_player.room = "outside"
                        leaving_game = False
                    elif (try_again == "n"):
                        leaving_game = False
                        playing = False
                    else:
                        print("type 'y' to keep trying, 'n' to stop playing:  ")
            elif (current_player.room == "narrow"):
                current_player.room = "foyer"
            elif (current_player.room == "treasure"):
                print("You stepped on a poisonous fungi and the spores killed you!")
                leaving_game = True
                while (leaving_game):
                    try_again = input("Try Again? y/n? \n-->   ")
                    if (try_again == "y"):
                        current_player.room = "outside"
                        leaving_game = False
                    elif (try_again == "n"):
                        leaving_game = False
                        playing = False
                    else:
                        print("type 'y' to keep trying, 'n' to stop playing:  ")
        elif (action == "q"):
            playing = False
        else:
            print("Please enter a direction: south, west, east, north. etc.")

adventure_awaits()
