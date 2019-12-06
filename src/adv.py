from room import Room
from player import Player
from item import Item
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

item = {
    'coins': Item('Coins', 'You will unlock everything in this coins'),

    'key': Item('Key', 'get the key access to all the doors'),

    'pencil': Item('pencil', 'Just write your dream')
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

#  rooms link to items
room['overlook'].items.append(item['coins'])
room['narrow'].items.append(item['key'])
room['foyer'].items.append(item['pencil'])

#####################################
#                                   #
#          overlook  #   treasure   #
#           foyer       narrow      #
#          Outside                  #
#####################################


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


def initialize():
    player_name = input('What is your name?\n')

    current_player = Player(player_name, room['outside'])

    print(
        f'Welcome {current_player.get_name()}! Your current location is: {current_player.get_location().name}\n'
    )

    def print_current_location():
        print(f'You are now in the {current_player.get_location().name}\n')

    def is_valid_move(move):
        if move != None:
            return True
        else:
            return False

    def items_available(room):
        if (len(room.items)):
            return True
        else:
            return False

    nl = '\n'

    def print_items(room):
        print(
            f'It contains: {nl}{nl.join(str(x.name) for x in room.items)}{nl}'
        )

    while True:
        answer = input('Which direction do you want to go?')

        if(len(answer.split(', ')) == 1):
            if (answer == 'n' or answer == 's' or answer == 'w' or answer == 'e'):
                if answer == 'n':
                    if is_valid_move(current_player.get_location().n_to):
                        current_player.set_location(
                            current_player.get_location().n_to
                        )

                        print_current_location()

                        if items_available(current_player.get_location()):
                            print_items(current_player.get_location())

                    else:
                        print(
                            'Path does not exists. Try another direction.\n'
                        )
                if answer == "s":
                    if is_valid_move(current_player.get_location().s_to):
                        current_player.set_location(
                            current_player.get_location().s_to
                        )
                        print_current_location()

                    else:
                        print(
                            'Path does not exists. Try another direction.\n'
                        )
                if answer == "w":
                    if is_valid_move(current_player.get_location().w_to):
                        current_player.set_location(
                            current_player.get_location().w_to
                        )
                        print_current_location()

                    else:
                        print(
                            'Path does not exists. Try another direction.\n'
                        )
                if answer == "e":
                    if is_valid_move(current_player.get_location().e_to):
                        current_player.set_location(
                            current_player.get_location().e_to
                        )
                        print_current_location()

                    else:
                        print(
                            'Path does not exists. Try another direction.\n'
                        )
            elif (answer == 'q'):
                print(f'Thanks for playing!')
                break
            else:
                print(
                    f'Seems like you entered a wrong value. Either n,s,w,e or q for quit')
        else:
            split_input = answer.split()

            if split_input[0] == 'get' or split_input[0] == 'drop':
                if split_input[0] == 'get':
                    if items_available(current_player.get_location()):
                        current_player.items.append(item[split_input[1]])
                        current_player.current_room.items.remove(
                            item[split_input[1]]
                        )

                        print(f'You got: {current_player.items[0].name}!{nl}')
                else:
                    print('Item does not exist!')
            else:
                print(
                    'Invalid command: use either "take" or "drop" to interact with items'
                )


initialize()
