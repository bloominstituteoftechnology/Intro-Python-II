from room import Room
from player import Player
from item import Item

# Declare all the rooms
room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),
    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}
# declare all items
item = {
    'outside': Item('pistol', "burried slightly in some freshly disturbed dirt"),
    'foyer': Item('beef jerky', """wonder how long its been here"""),
    'overlook': Item('Nervana CD', """strange that this is here"""),
    'narrow': Item('Soda', 'Good thing its not a "pop"'),
    'treasure': Item('Monopoly Money', 'This is a terrible joke 😭')
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

# Link item to room??
room['outside'].add_item(item['outside'])
room['foyer'].add_item(item['foyer'])
room['overlook'].add_item(item['overlook'])
room['narrow'].add_item(item['narrow'])
room['treasure'].add_item(item['treasure'])


# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

'''
direction is the direction the user input
current is the current room the player is in

returns the new room that the player moves to if the
move was successful, or returns the current room if the move was
not successful
'''


def try_direction(direction, current):
    attribute = direction + '_to'

    # See if the inputted direction is one that we can move to
    if hasattr(current, attribute):
        # fetch the new room
        return getattr(current, attribute)
    else:
        print("There is nothing in that direction")
        return current

# checks if item is in the room


def display_item(item):
    room_items = player.curr_room.item_list
    return any(i.name == item for i in room_items)

# checks if item is in iventory, any func returns bool


def item_in_inv(item):
    player_item = player.item_list
    return any(i == item for i in player_item)

# decides what to do when player interacts with an item


def interact_item(action, item):
    room_items = player.curr_room.item_list
    player_items = player.curr_room

# if the player chooses to get the item, add it to their inventory
    if action == "get":
        player.grab_item(item)
# remove it from the rooms inventory
        for i in room_items:
            if i.name == item:
                player.curr_room.remove_item(i)


# Write a loop that:
#
while True:
    room_items = player.curr_room.display_item()
    # * Prints the current room name
    print(player.curr_room.name)
    # * Prints the current description (the textwrap module might be useful here).
    print(player.curr_room.desc)
    if len(room_items) > 0:
        print(f"There is a {room_items}\n")
    print(
        'commands: \nq=Quit\nn=North\ne=Eastn\nw=West\ns=South\ngrab [item-name]=pick_up_item\ndrop [item-name]=drop_item')
    # * Waits for user input and decides what to do.
    s = input("\n>").lower().split()

    # check to see if the user input a one or two word command
    if len(s) == 1:
        # the user passed us a direction

        # grab the first character of the first word
        s = s[0][0]
        if s == 'q':
            print('Thank you for playing')
            break

        player.curr_room = try_direction(s, player.curr_room)
    elif len(s) == 2:
        # the user passed us a two-word command
        first_word = s[0]  # verb
        second_word = s[1]  # noun
        print(first_word, second_word)
        if first_word in ['grab', 'drop']:
            for i in room_items:
                player.grab_item(i)
                print(f"you just grabbed {i}")
                continue
        else:
            print("There is no item in the room by that name")
            continue
    else:
        print("I don't understand that command")
        continue

    # none dynamic way
    # if s == 'n':
    #     player.curr_room = player.curr_room.n_to
    # elif s == 's':
    #     player.curr_room = player.curr_room.s_to
    # elif s == 'e':
    #     player.curr_room = player.curr_room.e_to
    # elif s == 'w':
    #     player.curr_room = player.curr_room.w_to
    # else:
    #     print("not a valid direction")

    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
