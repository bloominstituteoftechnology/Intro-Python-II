from room import Room
from player import Player
from item import Item
from enum import Enum


class Action(Enum):
    """
    An enumeration for specifying potential user actions
    """
    MOVE = 1
    TAKE_ALL_ITEMS = 2
    SHOW_INVENTORY = 3
    SHOW_ROOM_INFO = 4
    TAKE_SINGLE_ITEM = 5
    DROP_SINGLE_ITEM = 6
    EXIT = 7


class Direction(Enum):
    """
    An enumeration for specifying the available directions
    """
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4


# Setup rooms
def room_setup():
    """
    Declares all rooms and connects those rooms in a specified way
    """
    global room
    room = {
        'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

        'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

        'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling 
        into the darkness. Ahead to the north, a light flickers in
        the distance, but there is no way across the chasm."""),

        'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. 
        The smell of gold permeates the air."""),

        'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! 
        Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
    }
    room['outside'].n_to = room['foyer']
    room['foyer'].s_to = room['outside']
    room['foyer'].n_to = room['overlook']
    room['foyer'].e_to = room['narrow']
    room['overlook'].s_to = room['foyer']
    room['narrow'].w_to = room['foyer']
    room['narrow'].n_to = room['treasure']
    room['treasure'].s_to = room['narrow']


# Setup room items
def room_item_setup():
    """
    Adds items to each specified room
    """
    room['outside'].room_items.append(Item('Sword', 'A rusty old iron sword'))
    room['outside'].room_items.append(Item('Shield', 'A wooden shield'))
    room['foyer'].room_items.append(Item('Coins', 'Bronze coins'))
    room['overlook'].room_items.append(Item('Ruby', 'A large, cut, Ruby'))
    room['narrow'].room_items.append(Item('Key', 'A key, I wonder what this is for?'))
    room['treasure'].room_items.append(Item('Treasure Box', 'I hear something inside, how do I open it?'))


def display_current_room_info():
    """
    Will print the room info based on the players current room.
    """
    print('========== ROOM INFO ==========')
    print(f'You\'re character is currently located in the room named "{player.current_room}".')
    print(f'The room description says: "{player.current_room.room_description}"')
    print(f'The items available in this room are: {[item.name for item in player.current_room.room_items]}')
    print('========== END ROOM INFO ==========')


def move_user():
    """
    Moves user to a particular, specified room
    """
    north_room = player.current_room.n_to
    south_room = player.current_room.s_to
    west_room = player.current_room.w_to
    east_room = player.current_room.e_to

    while True:
        user_chosen_direction = input("Please enter a direction to move in by selecting a number \n "
                                      "(1) North \n "
                                      "(2) South \n "
                                      "(3) West \n "
                                      "(4) East \n "
                                      "Direction: ")
        try:
            direction = Direction(int(user_chosen_direction))
        except ValueError:
            print("Incorrect direction, please try again by selecting a number (1-4).")
            continue

        if direction == Direction(1) and north_room:
            player.current_room = north_room
        elif direction == Direction(2) and south_room:
            player.current_room = south_room
        elif direction == Direction(3) and west_room:
            player.current_room = west_room
        elif direction == Direction(4) and east_room:
            player.current_room = east_room
        else:
            print("There is no room in that direction, please try again!")
            continue

        display_current_room_info()
        break


def take_all_items():
    """
    Takes all items from the current room and puts them into the users inventory
    """
    for item in player.current_room.room_items:
        player.add_item_to_inventory(item)
    player.current_room.room_items = []
    print(f'================ Items have been added to your inventory: {player.inventory} ================')


def show_inventory():
    """
    Prints the items in a users inventory
    """
    print(f'================ Inventory: {[item for item in player.inventory]} ================')


def take_single_item():
    """
    Allows the user to take a single, user specified item from a room
    """
    available_items = [item.name.lower() for item in player.current_room.room_items]
    if len(player.current_room.room_items) == 0:
        print("There are no items in this room!")
    while True:
        item_to_take = input("Please type the name of the item to take: ").lower()
        if item_to_take not in available_items:
            print("Item does not exist, try again.")
            continue
        else:
            for item in player.current_room.room_items:
                if item_to_take == item.name.lower():
                    player.add_item_to_inventory(item)
                    item.on_take(player)
                    player.current_room.room_items.remove(item)
        break



def drop_single_item():
    """
    Drops a single, user specified item from their inventory
    """
    items_inventory = [item.name.lower() for item in player.inventory]
    if len(player.inventory) == 0:
        print("You have no items!")
    while True:
        item_to_remove = input("Please type the name of the item to remove: ").lower()
        if item_to_remove not in items_inventory:
            print("Item does not exist, try again.")
            continue
        else:
            for item in player.inventory:
                if item_to_remove == item.name.lower():
                    player.remove_item_from_inventory(item)
                    item.on_drop(player)
        break


def exit_game():
    """
    Exits the game by closing the script entirely
    """
    print('Exiting...Thanks for playing!')
    raise SystemExit(0)


def process_user_action(action):
    """
    Processes a user action based on the selection chosen in start_game()

    arguments:
    action -- the chosen user action, based on the Action enumeration
    """
    if action == Action.MOVE:
        move_user()
    elif action == Action.TAKE_ALL_ITEMS:
        take_all_items()
    elif action == Action.SHOW_INVENTORY:
        show_inventory()
    elif action == Action.SHOW_ROOM_INFO:
        display_current_room_info()
    elif action == Action.TAKE_SINGLE_ITEM:
        take_single_item()
    elif action == Action.DROP_SINGLE_ITEM:
        drop_single_item()
    elif action == Action.EXIT:
        exit_game()
    else:
        return "incorrect action"


def start_game():
    """
    Starts the game and sets up each room for the game. It adds a player and enters a game loop until conditions are met
    """
    room_setup()
    room_item_setup()
    global player
    player = Player("Conner", room['outside'])
    print(f'Welcome to the adventure game {player.name}!')
    display_current_room_info()
    while True:
        user_action = input("Please choose an action by selecting a number \n "
                            "(1) Move \n "
                            "(2) Take All Items \n "
                            "(3) Show Inventory \n "
                            "(4) Show Room Info \n "
                            "(5) Take a single item \n "
                            "(6) Drop a single item \n "
                            "(7) Exit \n Action: ")

        try:
            user_action = Action(int(user_action))
            process_user_action(user_action)
        except ValueError:
            print("Incorrect action, please try again by selecting a number (1-7).")
            continue


start_game()
