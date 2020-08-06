from room import Room
from player import Player
#from item import Item

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
room['outside'].n_to = room['foyer']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

def game():
    # player_name = input(f"\n What is your name? \n Enter Your Name : ")
    player = Player(current_room = room["outside"])

    print(" ")
    print("Welcome to the ADVENTURE Game!")
    answer = input("Are you ready for an adventure? Y/N ").lower().strip()
    print(" ")

    if answer == "y":
        playing = True
        player.describe_room()

        while playing == True:

            answer = input("\nWhat's your next move? \nGo North [n] South [s] East [e] West [w] \nQuit [q]").lower().strip()
            if answer in ["n", "s", "e", "w"]:
                if player.move_player(answer) == True:
                    player.describe_room()
                else:
                    print("\n   There is no way to go that direction.  \n")
            elif answer == "q":
                playing = False
            else:
                print("\n  That action isn't available.  \n")
    else:
        print("\n  Oh well, see you later!")
        return


game()


# if answer == "y":
#     # Let's pick a name for the character
#     # print("Let's choose a name!")
#     # player_name = input("Name: ")
#     player = Player()

#     # At the beginnig of the game, the current room is 'outside'
#     player.current_room = room['outside']
#     current_room = player.current_room
#     # Print the name and the description of the room
#     print("\n")
#     print(current_room.name)
#     print(current_room.description)

#     answer = input("\nWhat's your next move? \nGo North [n] South [s] East [e] West [w] ").lower().strip()
    
#     if answer == "n":
#         # Now the current room is 'foyer'
#         current_room = current_room.n_to
#         # Print the name and the description of the room
#         print("\n")
#         print(current_room.name)
#         print(current_room.description)

#         answer = input("\nWhat's your next move? \nGo North [n] South [s] East [e] West [w] ").lower().strip()
#         if answer == "s":
#             # Now the current room is 'outside'
#             current_room = current_room.s_to
#             # Print the name and the description of the room
#             print(current_room.name)
#             print(current_room.description)

#             answer = input("\nWhat's your next move? \n Go North [n] South [s] East [e] West [w] ").lower().strip()
#             if answer == "n":
#                 # Now the current room is 'foyer'
#                 current_room = current_room.n_to
#                 # Print the name and the description of the room
#                 print(current_room.name)
#                 print(current_room.description)

#             else:
#                 # There is nothing in this direction
#                 print("There is no way to go that direction.")
                    

#         elif answer == "n":
#             # Now the current room is 'overlook'
#             current_room = current_room.n_to
#             # Print the name and the description of the room
#             print(current_room.name)
#             print(current_room.description)

#             answer = input("\nWhat's your next move? \n Go North [n] South [s] East [e] West [w] ").lower().strip()
#             if answer == "s":
#                 # Now the current room is 'foyer'
#                 current_room = current_room.s_to
#                 # Print the name and the description of the room
#                 print(current_room.name)
#                 print(current_room.description)

#             else:
#                 # There is nothing in this direction
#                 print("There is no way to go that direction.")
#                 pass

#         elif answer == "e":
#             # Now the current room is 'narrow'
#             current_room = current_room.e_to
#             # Print the name and the description of the room
#             print(current_room.name)
#             print(current_room.description)

#             answer = input("\nWhat's your next move? \n Go North [n] South [s] East [e] West [w] ").lower().strip()
#             if answer == "w":
#                 # Now the current room is 'foyer'
#                 current_room = current_room.w_to
#                 # Print the name and the description of the room
#                 print(current_room.name)
#                 print(current_room.description)

#             elif answer == "n":
#                 # Now the current room is 'treasure'
#                 current_room = current_room.n_to
#                 # Print the name and the description of the room
#                 print(current_room.name)
#                 print(current_room.description)

#                 answer = input("What's your next move? \n Go North [n] South [s] East [e] West [w] ").lower().strip()
#                 if answer == "s":
#                     # Now the current room is 'narrow'
#                     current_room = current_room.s_to
#                     # Print the name and the description of the room
#                     print(current_room.name)
#                     print(current_room.description)

#                 else:
#                     # There is nothing in this direction
#                     print("There is no way to go that direction.")
#                     pass

#         else:
#             # There is nothing in this direction
#             print("There is no way to go that direction.")

#     else:
#         # There is nothing in this direction
#         print("There is no way to go that direction.")

# else:
#     print("Well, see you next time!")
#     playing = False


# # Make a new player object that is currently in the 'outside' room.

# # Write a loop that:
# #
# # * Prints the current room name
# # * Prints the current description (the textwrap module might be useful here).
# # * Waits for user input and decides what to do.
# #
# # If the user enters a cardinal direction, attempt to move to the room there.
# # Print an error message if the movement isn't allowed.
# #
# # If the user enters "q", quit the game.
