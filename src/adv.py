from room import Room
from player import Player
from item import Item, Gold, Weapon, Rock, Dagger
from string import capwords

# Declare all the rooms

north = 'Move North'
south = 'Move South'
east = 'Move East'
west = 'Move West'

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons",
                    [north]),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
    passages run north and east.""",
                  [south, north, east],
                  {'empty lantern': Item('empty lantern',
                                         'An simple oil-fueled lantern, '
                                         'currently devoid of fuel.', 5)}),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, 
    falling into the darkness. Ahead to the north, a light flickers in 
    the distance, but there is no way across the chasm.""",
                     [south]),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from 
    west to north. The smell of gold permeates the air.""",
                   [west, north],
                   {'gold': Gold(3), 'rock': Rock()}),

    'treasure': Room("Treasure Chamber",
                     """You've found the long-lost treasure
                     chamber! Sadly, it has already been completely emptied by
                     earlier adventurers. The only exit is to the south.""",
                     [south],
                     {'gold': Gold(1), 'dagger': Dagger()}),
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


def action_loop(player):
    print('Choose an action:\n')
    available_actions = player.current_room.actions + [
        f'Get {capwords(x)}'
        for x in player.current_room.inventory
        if player.current_room.inventory is not None
    ] + ['', 'View Inventory', 'Drop Item', '']

    for action in available_actions:
        print(action)

    action_input = input('Action:\n')

    if capwords(action_input) in available_actions:
        action_input = action_input.lower()
        if action_input.split()[0] == 'move':
            if action_input == 'move north':
                player.current_room = player.current_room.n_to
            elif action_input == 'move east':
                player.current_room = player.current_room.e_to
            elif action_input == 'move south':
                player.current_room = player.current_room.s_to
            elif action_input == 'move west':
                player.current_room = player.current_room.w_to
            return player.current_room
        elif action_input.split()[0] == 'get':
            item = action_input[4:]
            if item in player.current_room.inventory.keys():
                player.get_item(player.current_room.inventory[item])
                player.inventory[item].on_take()
                player.view_inventory()
                action_loop(player)
            else:
                print('No such item!')
                action_loop(player)
        elif action_input.split()[0] == 'drop':
            if action_input == 'drop item':
                print('Which item would you like to drop?')
                for x in player.inventory:
                    print(x)
                drop = input('Item:\n')
                if drop in player.inventory:
                    player.drop_item(player.inventory[drop])
                    player.current_room.inventory[drop].on_drop()
                    action_loop(player)
                else:
                    print('No such item!')
                    action_loop(player)
        elif action_input == 'view inventory':
            player.view_inventory()
            action_loop(player)
        return player.current_room
    elif 'drop' in action_input:
        item = action_input[5:]
        if item in player.inventory.keys():
            player.drop_item(player.inventory[item])
            print(f'You have dropped {item}.')
            action_loop(player)
        else:
            print('No such item!')
            action_loop(player)
        return player.current_room
    else:
        print('That\'s impossible!')
        action_loop(player)
    return player.current_room


def play_loop(player):
    print(f'Location: {player.current_room.name}')
    print(f'{player.current_room.description}\n')
    if player.current_room.inventory:
        print('You see something laying in the shadows...')
        print(f'This room contains '
              f'{[x for x in player.current_room.inventory]}')
    while player.current_room.name != 'Treasure Chamber':
        player.current_room = action_loop(player)
        play_loop(player)
    else:
        player.victory = True


def main():
    player_name = input('What is your name, adventurer?\n')
    player = Player(player_name, room['outside'])
    while not player.victory:
        play_loop(player)
    else:
        print(f'You have discovered what remains '
              f'of the treasure, {player.name}!\n'
              f'Congratulations!')


if __name__ == '__main__':
    main()
