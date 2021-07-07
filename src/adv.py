from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms
room = {
    'outside':Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons", 
                    [Item("coin"), 
                    Item("gun")]),
    'foyer':Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", 
                    [Item("pizza")]),

    'overlook':Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", 
                    [Item("sword")]),

    'narrow':Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", 
                    [Item("burger"), 
                    Item("tank")]),

    'treasure':Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", 
                    [Item("pizza")]),
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
player_1 = Player("1", room['outside'])
wrappedDesc = textwrap.wrap(player_1.current_room.desc)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

print(f"Player's current room: {player_1.current_room.name}")
print(f"Current room desc: {wrappedDesc}")
user_input = input("Select one of the following direction to move the player. \nN (north), S (south), E (east), W (west):\n ---> ").lower().split(" ")

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def prompt_next_move():
    return input("What's the next move. Please select a direction:\n ---> ").lower().split(" ")

def prompt_invalid_room_warning(room):
    return input(f"You can't move to {room}. Please make another choice:\n ---> ").lower().split(" ")

while user_input is not None:
    length = len(user_input)

    if length == 1:
        if user_input[0] == "n":
            north_room = player_1.current_room.n_to
            if north_room is not None:
                player_1.current_room = north_room
                user_input = prompt_next_move()
            else:
                user_input = prompt_invalid_room_warning("north")
        elif user_input[0] == "s":
            south_room = player_1.current_room.s_to
            if south_room is not None:
                player_1.current_room = south_room
                user_input = prompt_next_move()
            else:
                user_input = prompt_invalid_room_warning("south")
        elif user_input[0] == "e":
            east_room = player_1.current_room.e_to
            if east_room is not None:
                player_1.current_room = east_room
                user_input = prompt_next_move()
            else:
                user_input = prompt_invalid_room_warning("east")
        elif user_input[0] == "w":
            west_room = player_1.current_room.w_to
            if west_room is not None:
                player_1.current_room = west_room
                user_input = prompt_next_move()
            else:
                user_input = prompt_invalid_room_warning("west")
        elif user_input[0] == "q":
            print(f'You exited the game. Sorry to see you go. Bye!')
            break
        else:
            if length == 0:
                user_input = input("Please enter a value from N, S, E, W. Make a selection:\n ---> ")
            elif length > 1:
                user_input = input("You can only select a value from N, S, E, W. Make a selection:\n ---> ")
            else:
                user_input = input("This movement is not allowed. You can only select a value from N, S, E, W:\n ---> ").lower()
    elif length == 2:
        if user_input[0] == "get" or user_input[0] == "take":
            item = Item(user_input[1])
            if item in player_1.current_room.items:
                player_1.current_room.removeItem(user_input[1])
                player_1.items.append(user_input[1])
            else:
                print(f"This room doesn't have item: {user_input[1]}")
                user_input = input("Please make another choice:\n ---> ")

