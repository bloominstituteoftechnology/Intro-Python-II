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

jack = Player('Jack Stone', 'outside')

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

print(room[jack.current_room])
player_input = input("Please enter a command:")

def move():
    global player_input
    move_dir = f"{player_input}_to"
    if getattr(room[jack.current_room], move_dir) != None:
        jack.current_room = getattr(room[jack.current_room], move_dir)
        print(room[jack.current_room])
        room[jack.current_room].print_items()
        player_input = input("Please enter a command:")
    else:
        print('There is no room in that direction')
        player_input = input("Please enter a command:")


while player_input != 'q':
    input_arr = player_input.split(" ")
    if len(input_arr) < 2:
        if player_input == 'n' or player_input == 's' or player_input == 'e' or player_input == 'w':
            move()
        elif player_input == 'i':
            jack.print_inventory()
            player_input = input("Please enter a command:")
        else:
            print('Please enter a cardinal direction (ex. n, s, e, w)')
            player_input = input("Please enter a command:")
    else:
        if input_arr[0] == 'get':
            if room[jack.current_room].got_item(input_arr[1]):
                jack.get_item(items[input_arr[1]])
                print(f"You picked up the {input_arr[1]}")
                player_input = input("Please enter a command:")
            else: 
                print(f"There is no {input_arr[1]} in this room ya goober")
                player_input = input("Please enter a command:")
        elif input_arr[0] == 'drop':
            if jack.dropped_item(input_arr[1]):
                room[jack.current_room].receive_item(items[input_arr[1]])
                print(f"You dropped the {input_arr[1]}")
                player_input = input("Please enter a command:")
            else: 
                print(f"You don't have a {input_arr[1]} to drop!")
                player_input = input("Please enter a command:")
        else:
            print('Please enter a valid two word command (ex. get torch, drop drawers)')
            player_input = input("Please enter a command:")
