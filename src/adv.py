from room import Room
from player import Player
from directions import room

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print('Welcome')
player_name = input("What is your name: ")
player = Player(name = player_name, current_room = room['outside'])

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

#Print current room name
print(f'Welcome {player.name}! You are currently in the room {player.current_room}')

while True:

    #Player has to choose direction
    #Selection has to be an input
    selection = input("""Choose a direction:
    North(n), South(s), East(e), West(w),
    or Quit(q) """)

    try:
        #Have to cast input as a string
        selection = str(selection.strip().lower())

        if selection == 'q':
            print(f"Thank you for playing {player.name}")
            break

        elif selection in ('n','s','e','w'):
            #Need to think through this part

            player.move(selection)
            print(f"{player.name} {player.current_room}")

        else:
            print("Please choose a valid direction.")

    except TypeError:
        print("Please choose n, s, e, w.")

