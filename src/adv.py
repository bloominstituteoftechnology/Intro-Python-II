from room import Room
from player import Player
from item import Item
import os
import time


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


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
sword = Item('sword', 'this is an awesome sword')
ring = Item('ring', 'this is the ring in history')
coffee = Item('coffee', 'this is not Starbuck,Im lying')
coins = Item('coins', 'coins is what I love')
arrow = Item('arrow', 'this is an arrow I need to catch some bird')


def add_initial_items_to_rooms():
    room['outside'].add_item(sword)
    room['outside'].add_item(coffee)
    room['foyer'].add_item(ring)
    room['overlook'].add_item(arrow)
    room['overlook'].add_item(coffee)
    room['treasure'].add_item(coins)
    room['narrow'].add_item(coffee)


def print_out_items_in_current_room(room):
    if not room.items:
        print(style.MAGENTA + "This room have nothing left")
    else:
        print(style.MAGENTA + 'This room have ' + ','.join(f"{item.name}" for item in room.items))


def get_room_detail():
    print(style.YELLOW + "Current room:", player.current_room.name)
    print(style.YELLOW + "Description:", player.current_room.description)


player = Player("Nick", room['outside'])
wrong_alert = (style.RED + "Wrong direction,follow the hint in description!!!")


def show_wrong_direction_alert():
    print(wrong_alert)


print(style.BLUE + "Welcome to the Adventure Game!")
print(style.BLUE + "Please choose a direction to move.")

add_initial_items_to_rooms()
game_running = True


def cardinal_direction():
    if instruction == "n":
        if player.current_room.n_to == None:
            show_wrong_direction_alert()

        else:
            player.current_room = player.current_room.n_to
    elif instruction == "s":
        if player.current_room.s_to == None:
            show_wrong_direction_alert()

        else:
            player.current_room = player.current_room.s_to
    elif instruction == "e":
        if player.current_room.e_to == None:
            show_wrong_direction_alert()

        else:
            player.current_room = player.current_room.e_to
    elif instruction == "w":
        if player.current_room.w_to == None:
            show_wrong_direction_alert()

        else:
            player.current_room = player.current_room.w_to
    # If the user enters "q", quit the game
    elif instruction == "q":
        print("Game Over!")
        quit()


while game_running:

    get_room_detail()

    print_out_items_in_current_room(player.current_room)

    if not player.inventory:

        instruction = input(style.CYAN +
                            '\n'.join(
                                f"[take {item.name}] take {item.name} and run" for item in player.current_room.items) +
                            "\n[n] north [s] south [e] east [w] west [q] quit\n")
        cardinal_direction()

        for item in player.current_room.items:
            if instruction == f"take {item.name}":

                player.pick_up_item_to_inventory(item)
                item.on_take()
                print(style.RED + "USER INVENTORY: " +
                      ",".join(f"{item.name}" for item in player.inventory))
                player.current_room.remove_item(item)
            elif instruction != "n" and instruction != "s" and instruction != "e" and instruction != "w" and instruction != "q":
                print(style.RED + "This item you are looking for not in this room")
                break


    else:
        instruction = input(
            '\n'.join(f"[take {item.name}] take {item.name} and run\n" for item in player.current_room.items) +
            '\n'.join(f"[drop {item.name}]" for item in player.inventory) + "\n" +
            "\n[n] north [s] south [e] east [w] west [q] quit\n")

        cardinal_direction()

        for item in player.current_room.items:
            if instruction == f"take {item.name}":

                player.pick_up_item_to_inventory(item)
                item.on_take()
                print(style.RED + "USER INVENTORY: " +
                      ",".join(f"{item.name}" for item in player.inventory))
                player.current_room.remove_item(item)
            else:
                print(style.RED + "This item you are looking for not in this room")
                break

        for item in player.inventory:
            if instruction == f"drop {item.name}":
                player.drop_item(item)
                item.on_drop()
                player.current_room.add_item(item)
            else:
                print(style.RED + "You don't have this item to drop")
                break

#
