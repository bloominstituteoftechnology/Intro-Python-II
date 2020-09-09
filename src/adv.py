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

new_player = Player("Ashley", room['outside'])

def game_input(command, player):
    end_game = False
    if command == 'n':
        if player.current_room.n_to != None:
            player.current_room = player.current_room.n_to
            display_room_description(player.current_room)
        else:
            print("Sorry, can't go this way!")
    elif command == 's':
        if player.current_room.s_to != None:
            player.current_room = player.current_room.s_to
            display_room_description(player.current_room)
        else:
            print("Nope, try again!")
    elif command == 'e':
        if player.current_room.e_to != None:
            player.current_room = player.current_room.e_to
            display_room_description(player.current_room)
        else:
            print("Are you lost? This isn't the way")
    elif command == 'w':
        if player.current_room.w_to != None:
            player.current_room = player.current_room.w_to
            display_room_description(player.current_room)
        else:
            print("Made a wrong turn, try again!")
    elif command == 'q':
        end_game = True
    else:
        print('Please enter a valid direction')
    return end_game


def display_room_description(room):
    print(f'You are in {room.name}')
    print(room.description)
end_game = False

display_room_description(new_player.current_room)

while end_game == False:
    end_game = game_input(str(input()), new_player)

print('Thanks for playing!')
