from player import Player
from room import Room
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
room['foyer'].items = [Item('sword', 'sharp'), Item('invisibility', 'makes user invisible') ]
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# for key, value in room.items():
#     print(value.name)
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
zach = Player("Zach", room['outside'])
# player_input = ""
def get_input():
    player_input = input("\nEnter a direction to move.\nEnter get / take 'item name' to pick up item.\nEnter i to see inventory. 'q' for quit \n")
    return player_input

def print_info():
    zach.change_player_room(zach.room)
    print(f'Room: {zach.room.name}\nDescription: {zach.room.description}\n  Items')
    if len(zach.room.items) > 0:
        for i in zach.room.items:
            print(f'    Name: {i.name}\n    Description: {i.description}')
    else:
        print('    No items in this Room')

def current_room(name, item):
    for key, val in room.items():
        if val.name == name:
            the_room = room.get(key)
            the_room.delete_item(item)

def drop_current_room(name, item):
    for key, val in room.items():
        if val.name == name:
            the_room = room.get(key)
            the_room.add_off_drop_item(item)

def drop_off(word):
    error_msg = []
    if len(zach.items) > 0:
        for i in zach.items:
            if word == i.name:
                zach.drop_off_item(i)
                drop_current_room(zach.room.name, i)
            else:
                error_msg.append(f'The selected item {word} does not exist\n')
        if len(error_msg) == len(zach.room.items):
            print(error_msg[0])
    else:
        print("No Items present in inventory")




def check_room_items(word):
    error_msg = []
    if len(zach.room.items) > 0:
        for i in zach.room.items:
            if word == i.name:
                zach.pick_up_item(i)
                current_room(zach.room.name, i)
            else:
                error_msg.append(f'The selected item {word} does not exist\n')
        if len(error_msg) == len(zach.room.items):
            print(error_msg[0])
    else:
        print("No Items present in this room")

def print_inventory():
    print('  \nInventory')
    if len(zach.items) > 0:
        for i in zach.items:
            print(f'    Name: {i.name}\n    Description: {i.description}\n')
    else:
        print('    No items in Inventory\n')




def switch(input, room):
    the_switch = {
        'n': room.n_to,
        's': room.s_to,
        'e': room.e_to,
        'w': room.w_to,
    }
    two_words = input.split(" ")
    r_value = the_switch.get(input)
    if r_value:
        zach.change_player_room(r_value)
    elif input == 'add':
        room.ask_for_items()
    elif two_words[0] == 'get' or two_words[0] == 'take' and len(two_words) > 1:
        check_room_items(two_words[1])
    elif two_words[0] == "drop" and len(two_words) > 1:
        drop_off(two_words[1])
    elif input == 'i':
        print_inventory()
    else:
        print("That Direction is not available")



# Write a loop that:
while True:
    print_info()
    local_input = get_input()
    if local_input == 'q':
        break
    else:
        action = switch(local_input, zach.room)
# while player_input.lower() != "exit":
#     player_input = ""
#     for key, value in room.items():
#         if key == zach.room:
#             current_room = {"name": value.name, "desc": value.description }
# * Prints the current room name
#             print(f'Current Room: {current_room["name"]}\n  Description: {current_room["desc"]}')
#     player_input = input("Please Select a Direction, 'N,S,E,W': ")
#     if player_input.lower() == "n" and room[zach.room].n_to:
#         for key, value in room.items():
#             if current_room['name'] == room[zach.room].name:
#                 if value.name == room[zach.room].n_to.name:
#                     zach.room = key
#     elif player_input.lower() == "s" and room[zach.room].s_to:
#         for key, value in room.items():
#             if current_room['name'] == room[zach.room].name:
#                 if value.name == room[zach.room].s_to.name:
#                     zach.room = key
#     elif player_input.lower() == "e" and room[zach.room].e_to:
#         for key, value in room.items():
#             if current_room['name'] == room[zach.room].name:
#                 if value.name == room[zach.room].e_to.name:
#                     zach.room = key
#     elif player_input.lower() == "w" and room[zach.room].w_to:
#         for key, value in room.items():
#             if current_room['name'] == room[zach.room].name:
#                 if value.name == room[zach.room].w_to.name:
#                     zach.room = key
#     else:
#         print("The selected direction doesn't exist for this room")


# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
