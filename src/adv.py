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
player = Player(
    input('Greetings Adventurer! What is your name?\n'), room['outside'])

print(player)
# Write a loop that:
while True:
    # * Prints the current room name
    print(player.current_room.name)
# * Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)
# * Waits for user input and decides what to do.
    user_input = input('Choose a direction that calls you...\n\n')
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

    def update_player_room(direction_to):
        global player
        print(player.current_room.__getattribute__(
            direction_to))
        print('\n\nPlayerINFO: ', player)
        player.current_room = player.current_room.__getattribute__(
            direction_to)

    movement_error_message = 'That direction does not lead to anything.'

    print('user_input: ', user_input)

    if player.current_room.name == "Outside Cave Entrance":
        if user_input == 'n':
            update_player_room('n_to')
        else:
            print(movement_error_message)
    elif player.current_room.name == "Foyer":
        if user_input == 'w':
            print(movement_error_message)
        elif user_input == 'n':
            update_player_room('n_to')
        elif user_input == 's':
            update_player_room('s_to')
        elif user_input == 'e':
            update_player_room('e_to')
    elif player.current_room.name == "Grand Overlook":
        if user_input == 'n' or 'e' or 'w':
            print(movement_error_message)
        elif user_input == 's':
            update_player_room('s_to')
    elif player.current_room.name == "Narrow Passage":
        if user_input == 's' or 'e':
            print(movement_error_message)
        elif user_input == 'w':
            update_player_room('w_to')
        elif user_input == 'n':
            update_player_room('n_to')
    elif player.current_room.name == "Treasure Chamber":
        if user_input == 'n' or 'e' or 'w':
            print(movement_error_message)
        elif user_input == 's':
            update_player_room('s_to')

# If the user enters "q", quit the game.
    if user_input == 'q':
        print('\n\nThanks for playing! Goodbye.\n\n')
        exit(0)
