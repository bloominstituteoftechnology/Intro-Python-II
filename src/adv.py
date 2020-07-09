from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("outside", "Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     ["lantern", "fire", "grapple", "shovel"]),

    'foyer':    Room("foyer", "Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("overlook", "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("narrow", "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("treasure", "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["crown", "chest", "chalice"]),
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
player = input("Enter your name here to play: ")

player1 = Player(player, room['outside'], [])

# print("GETATTR", getattr(room['outside'], 'n_to'))
direction = input("""Please enter a direction you want to travel,
[n], [s], [e] or [w] If you would like to quit please enter [q]: """)

userIpt = direction.lower()

currentRoom = 'outside'

while not userIpt == 'q':
    if userIpt == 'n' or userIpt == 's' or userIpt == 'e' or userIpt == 'w':
        try:
            cardinal = (f"{userIpt}_to")

            print(getattr(room[currentRoom], cardinal))

            currentRoom = getattr(room[currentRoom], cardinal).roomID

        except AttributeError:
            print("Try again, you cannot move in that direction!")

    elif userIpt == 'look':
        grabbedItems = room[currentRoom].look()
        for item in grabbedItems:
            player1.item_list.append(item)

    direction = input("""Please enter a direction you want to travel,
[n], [s], [e] or [w] If you would like to quit please enter [q]: """)

    userIpt = direction.lower()


# if player1.current_room == 'outside':

# Make a new player object that is currently in the 'outside' room.

# print(player1)

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

# player1 = Player("matt", room['outside'])

# def player_input():
#     return input("[n] North [s] South [e] East [w] West [q] Quit\n")

# prompt = player_input()

# def move():
#     print(player1.current_room)
#     print("What is your next move???")
#     global prompt
#     prompt = player_input()

# def bad_move():
#     print("Sorry, you can't move in that direction. Please try again!")
#     global prompt
#     prompt = player_input()

# while not prompt == "q":
#     print(room[player1.current_room.name].n_to)
#     if player1.current_room == room['outside']:
#         if prompt == "n":
#             player1.current_room = room["outside"].n_to
#             move()
#         else:
#             bad_move()
#     elif player1.current_room == room['foyer']:
#         if prompt == "n":
#             n_to
#             move()
#         elif prompt == "s":
#             player1.current_room = room['foyer'].s_to
#             move()
#         elif prompt == "e":
#             player1.current_room = room['foyer'].e_to
#             move()
#         else:
#             bad_move()
#     elif player1.current_room == room['overlook']:
#         if prompt == "s":
#             player1.current_room = room['overlook'].s_to
#             move()
#         else:
#             bad_move()
#     elif player1.current_room == room['narrow']:
#         if prompt == "n":
#             player1.current_room = room['narrow'].n_to
#             move()
#         elif prompt == "w":
#             player1.current_room = room['narrow'].w_to
#             move()
#     # elif player1.current_room == room['treasure']:
