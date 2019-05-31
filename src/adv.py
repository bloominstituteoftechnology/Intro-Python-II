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

# test = getattr(room['foyer'], "w_to")
# print(test)
# print(room['foyer'])
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

# my_player = Player("Abdiel", room["outside"])
possible_directions = ["n", "s", "e", "w"]

def get_direction():
    direction = input("Which way would you like to go? \n").lower()

    if direction == "q":
        return direction
    elif direction in possible_directions:
        direction = f"{direction}_to"
        return direction
    else :
        print(f"{direction} is not a valid input, please choose between 'n', 's', 'e', 'w', 'q'\n" )
        return None

def attempt_move(current_room, direction):
    if direction == "q":
        return False
    elif direction == None:
        return current_room
    else:
        if hasattr(current_room, direction):
            attribute_returned = getattr(current_room, direction)
            if attribute_returned == None:
                print("There is no room in that direction \n")
                return current_room
            else:
                return attribute_returned
        else:
            print("There is no room in that direction \n")
            return current_room


def begin_move():
    player_name =  input("Before we start, let's get your name: \n")
    my_player = Player(player_name, room['outside'])
    print(f"Great, {my_player.name}, let's begin.\n")
    print(f"We will start of at the {my_player.cur_room.name} where {my_player.cur_room.description}")
    ask_if_ready = input("\nReady to begin? (Y/N)\n").lower()
    if ask_if_ready == 'y':
        while(my_player.cur_room):
            direction = get_direction()
            my_player.cur_room = attempt_move(my_player.cur_room, direction)
            if my_player.cur_room == False:
                pass
            else:
                print(f"\nYou are in the {my_player.cur_room.name} where {my_player.cur_room.description}\n")

        print("\nThank you for playing! See ya soon")
    else:
        print("\nThank you for stopping by! See ya soon")

begin_move()
# def get_direction():
#     direction = input("Which way would you like to go?").lower()
#     if direction in possible_directions:
#         return direction
#     else:
#         print(f"{direction} is not a valid input, please choose between 'n', 's', 'e', 'w', 'q'")
#         return "error"

# def attempt_move(cur_room):
#     direction = get_direction()

#     if direction == "q":
#         return False
#     elif direction == "error":
#         attempt_move(cur_room)
#     else:
#         direction = f"{direction}_to"
    
#     print(f"it is trying to run {direction}")
#     room_returned = getattr(cur_room, direction)
#     print(f"room returned is {room_returned}")
#     if room_returned == None:
#         print("There is no room in that direction")
#         return cur_room
#     else:
#         return room_returned

# while(my_player.cur_room):
#     print(f"{my_player.name} is currently at {my_player.cur_room.name}")
#     my_player.cur_room = attempt_move(my_player.cur_room)