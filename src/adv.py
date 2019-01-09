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

items = {
    'key': Item('Key', 'It\'s a key to something'),
    'sword': Item('Sword', 'It\'s a weapon'),
    'mouse': Item('Mouse', 'It could be a pet'),
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
player = Player('outside')
room_name = room[player.current_room].name
room_desc = room[player.current_room].description
room['foyer'].item_list = [items['key'].name, items['sword'].name]
room_items = room[player.current_room].item_list if len(
    room[player.current_room].item_list) else 'There is nothing in here.'
# Write a loop that:
while True:
    room_key = player.current_room
    # * Prints the current room name
    print(room_name)
    # * Prints the current description (the textwrap module might be useful here).
    print(room_desc)
    print(room_items)
    # * Waits for user input and decides what to do.
    move = input('Where are you going? n, s, e, or w? ')
    # If the user enters a cardinal direction, attempt to move to the room there.
    if room_key == 'outside' and move == 'n':
        print(room[room_key].n_to)
        room_name = room[room_key].n_to.name
        room_desc = room[room_key].n_to.description
        room_items = room[room_key].n_to.item_list
        player.current_room = [key for key in room.keys() if key == 'foyer'][0]
    elif room_key == 'foyer' and move == 's':
        room_name = room[room_key].s_to.name
        room_desc = room[room_key].s_to.description
        player.current_room = [
            key for key in room.keys() if key == 'outside'][0]
    elif room_key == 'foyer' and move == 'n':
        room_name = room[room_key].n_to.name
        room_desc = room[room_key].n_to.description
        player.current_room = [
            key for key in room.keys() if key == 'overlook'][0]
    elif room_key == 'foyer' and move == 'e':
        room_name = room[room_key].e_to.name
        room_desc = room[room_key].e_to.description
        player.current_room = [
            key for key in room.keys() if key == 'narrow'][0]
    elif room_key == 'overlook' and move == 's':
        room_name = room[room_key].s_to.name
        room_desc = room[room_key].s_to.description
        player.current_room = [key for key in room.keys() if key == 'foyer'][0]
    elif room_key == 'narrow' and move == 'w':
        room_name = room[room_key].w_to.name
        room_desc = room[room_key].w_to.description
        player.current_room = [key for key in room.keys() if key == 'foyer'][0]
    elif room_key == 'narrow' and move == 'n':
        room_name = room[room_key].n_to.name
        room_desc = room[room_key].n_to.description
        player.current_room = [
            key for key in room.keys() if key == 'treasure'][0]
    elif room_key == 'treasure' and move == 's':
        room_name = room[room_key].s_to.name
        room_desc = room[room_key].s_to.description
        player.current_room = [
            key for key in room.keys() if key == 'narrow'][0]
    elif move == 'q':
        # If the user enters "q", quit the game.
        print('Game over! Byeee')
        break
    else:
        # Print an error message if the movement isn't allowed.
        print('There is nothing over there. Try another direction: ')
