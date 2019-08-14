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
player = Player('User', room['outside'])
# Write a loop that:
# class Adventure:
#     def __init__(self, room_name, room_description):
#         # self._room_name = room_name
#         self.room_name = room_name
#         self.room_description = room_description

#     # def set_room(self, room_entered):
#     #     self._room_name = room_entered

#     def __str__(self):
#         game_output = "Welcome to J's Room Search Adventure! (Version 1)"
#         print('Press key to begin?')
#         for room in self.room_name:
#             game_output += str(i) + " " + room.room_name + "\n"
#             i += 1
#         game_output + str(i=="q") + "press 'q' to quit the self"

#         return game_output

# # game = Adventure([Room("outside", )], [Room("foyer")], [Room("overlook")], [Room("narrow")], [Room("treasure")])
# # print(game)

#       
# * Prints the current room name
while True: 
    print("Welcome to J's Room Search Adventure! (Version 1)")
    selection = input("Select a room to enter! ")
    try: 

        if selection == "q":
            print("Thanks for playing!")
            break
        elif selection == "n" or selection == "s" or selection == "w" or selection == "e":
            print('help')
            print()
        else: 
            print ("You can only select 'n', 's','w', 'e'. Press 'q' to quit ")

    except ValueError:
        print("You can only enter a string!")
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the self.
