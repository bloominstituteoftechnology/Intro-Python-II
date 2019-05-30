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


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Adding items to room
room['foyer'].add_item(Item('torch', 'Helps you find the way in dark'))
room['foyer'].add_item(Item('mask', 'Saves you from dust'))
room['overlook'].add_item(Item('binocular', 'See far away objects'))
room['narrow'].add_item(Item('shoes', 'For better grip on narrow ledges'))
room['treasure'].add_item(Item('box', 'Empty gold box'))
room['treasure'].add_item(Item('map', 'Map to next gold hunt adventure'))

#
# Main
#


def move_in_dir(direction):
    current_room = player.get_current_room()

    # Check if player can move in direction given
    if direction == 'n' and current_room.n_to:
        player.set_current_room(current_room.n_to)
        return True
    elif direction == 's' and current_room.s_to:
        player.set_current_room(current_room.s_to)
        return True
    elif direction == 'e' and current_room.e_to:
        player.set_current_room(current_room.e_to)
        return True
    elif direction == 'w' and current_room.w_to:
        player.set_current_room(current_room.w_to)
        return True

    return False


def validate_cmd(cmd):
    valid_cmds = ['n', 's', 'e', 'w', 'q']

    split_cmd = cmd.split()
    cmd_len = len(split_cmd)

    # Input command should be 2 words at most
    if cmd_len != 1 and cmd_len != 2:
        return False

    if cmd_len == 1:
        if split_cmd[0] not in valid_cmds:
            return False

    if cmd_len == 2:
        # Input command should be take or drop
        if split_cmd[0] != 'take' and split_cmd[0] != 'drop':
            return False

    return True


def process_cmd(cmd, player):
    split_cmd = cmd.split()
    cmd_len = len(split_cmd)

    if cmd_len == 1:

        if split_cmd[0] == 'q':
            print('\nNice game. Visit again.')
            exit()
        else:
            if not move_in_dir(cmd.lower()):
                print('\nMoving in this direction is not allowed.')
    else:
        if split_cmd[0] == 'take':
            room = player.get_current_room()

            item_picked = False

            for index, item in enumerate(room.get_items()):
                if item.name == split_cmd[1]:
                    item_picked = True
                    player.add_item(item)
                    room.remove_item(index)
            if not item_picked:
                print('\nItem mentioned not available in room.')
        else:
            room = player.get_current_room()

            item_dropped = False

            for index, item in enumerate(player.get_items()):
                if item.name == split_cmd[1]:
                    item_dropped = True
                    room.add_item(item)
                    player.remove_item(index)

            if not item_dropped:
                print('\nItem mentioned not available with you.')


def print_error():
    print('Input invalid.\n')
    print('n - Move in North direction')
    print('s - Move in South direction')
    print('e - Move in East direction')
    print('w - Move in West direction')
    print('\nq - For exiting the game')
    print('\nTake item from a room')
    print('take <item_name>')
    print('\nDrop item in room')
    print('drop <item_name>')


# Make a new player object that is currently in the 'outside' room.
player = Player('Shreyas')
player.set_current_room(room['outside'])

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


while True:

    print(player.current_room)

    item_count_room = len(player.get_current_room().get_items())
    print(f'\n{item_count_room} available items in room.')
    for item in player.current_room.get_items():
        print(item)

    item_count_player = len(player.get_items())
    print(f'\n{item_count_player} available items with you.')
    for item in player.get_items():
        print(item)

    cmd = input("\nPlease provide your input: ")

    if not validate_cmd(cmd):
        print_error()
        continue

    process_cmd(cmd, player)
