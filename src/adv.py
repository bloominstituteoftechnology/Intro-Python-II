import random
from player import Player
from room import Room
from item import Item

# Declare all the rooms

item = {
    'sword': Item('sword', 'a used sword, a worn down blade that has seen many battles'),

    'ruby': Item('ruby', 'a ruby that inspires greed and fortune, looks to be worth plenty of gold'),

    'dung': Item('dung', 'a pile of dung, not sure why you would want to pick this up yet your curiosity beckons'),

    'torch': Item('torch', 'a torch, looks to still have some life left in it')
}


def generate_item():
    return random.choice(list(item.values()))


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", generate_item()),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east""", generate_item()),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm""", generate_item()),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air""", generate_item()),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south""", generate_item()),
}

print(room['outside'])


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


print('welcome to gay adventureland 3.0!')

player_name = input("what is your name?: ")

location = room['outside']

inventory = []

player = Player(player_name, location, inventory)


print(f"you are {player_name}, the gay barbarian {location}")

print("what would you like to do next?")


def choose_action():
    return int(input("[1] go north  [2] go south   [3] go east  [4] go west [5] pick up item [6] open inventory    [9] Quit\n"))


action = choose_action()

inventory_action = 0


def open_inventory():
    print('inventory: ')
    player.open_inventory()
    global action
    action = int(
        input("[1] go north  [2] go south   [3] go east  [4] go west [7] drop item [9] Quit\n"))


def drop(item, current_room):
    for i in range(0, len(player.items)):
        if item == player.items[i].item_name:
            global room
            room[current_room].items = player.items[i]


def next_step():
    print(location)
    print('what would you like to do next?')
    global action
    action = choose_action()


def wrong_way():
    print('that direction is blocked, try again')
    global action
    action = choose_action()


while not action == 9:
    if location == room['outside']:
        if action == 1:
            location = room['outside'].n_to
            next_step()
        elif action == 5:
            print('you picked up a {x}'.format(
                x=room['outside'].items.item_name))

            player.pickup_item(room['outside'].items)
            room['outside'].items = 'nothing of interest'
            action = choose_action()
        elif action == 6:
            open_inventory()

        elif action == 7:
            discard = input('what item would you like to drop?')
            drop(discard, 'outside')
            player.drop_item(discard)
            print(f'you dropped a {discard} into the room')
            action = choose_action()

        else:
            wrong_way()

    elif location == room['foyer']:

        if action == 2:
            location = room['foyer'].s_to
            next_step()

        elif action == 3:
            location = room['foyer'].e_to
            next_step()

        elif action == 1:
            location = room['foyer'].n_to
            next_step()

        elif action == 5:
            print('you picked up a {x}'.format(
                x=room['foyer'].items.item_name))
            player.pickup_item(room['foyer'].items)
            room['foyer'].items = 'nothing of interest'
            action = choose_action()

        elif action == 6:
            open_inventory()

        elif action == 7:
            discard = input('what item would you like to drop?')
            player.drop_item(discard)
            action = choose_action()

        else:
            wrong_way()

    elif location == room['overlook']:
        if action == 2:
            location = room['overlook'].s_to
            next_step()

        elif action == 5:
            print('you picked up a {x}'.format(
                x=room['overlook'].items.item_name))
            player.pickup_item(room['overlook'].items)
            room['overlook'].items = 'nothing of interest'
            action = choose_action()

        elif action == 6:
            open_inventory()

        elif action == 7:
            discard = input('what item would you like to drop?')
            player.drop_item(discard)
            action = choose_action()

        else:
            wrong_way()

    elif location == room['narrow']:
        if action == 4:
            location = room['narrow'].w_to
            next_step()
        elif action == 1:
            location = room['narrow'].n_to
            next_step()

        elif action == 5:
            print('you picked up a {x}'.format(
                x=room['foyer'].items.item_name))
            player.pickup_item(room['narrow'].items)
            room['narrow'].items = 'nothing of interest'
            action = choose_action()

        elif action == 6:
            open_inventory()

        elif action == 7:
            discard = input('what item would you like to drop?')
            player.drop_item(discard)
            action = choose_action()

        else:
            wrong_way()

    elif location == room['treasure']:
        if action == 2:
            location = room['treasure'].s_to
            next_step()
        elif action == 7:
            discard = input('what item would you like to drop?')
            player.drop_item(discard)
            action = choose_action()
        elif action == 5:
            print('you picked up a {x}'.format(
                x=room['treasure'].items.item_name))
            player.pickup_item(room['treasure'].items)
            room['treasure'].items = 'nothing of interest'
            action = choose_action()

        elif action == 6:
            open_inventory()
        else:
            wrong_way()


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
