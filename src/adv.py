from room import Room
from player import Player
from item import Item
import textwrap
import sys


print("\n")
print("welcome, enter q to quit \n")
print("Directional commands: n, s, e, w")
print("Available actions: take <item>, drop <item>")
print("Available queries(displays currently held items): i, inventory \n")


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

# Declare all the items
item = {
    'shovel': Item("Shovel", "Tool for moving material"),

    'rope': Item("Rope", "Long and sturdy"),

    'ladder': Item("Ladder", "Tall and safe"),

    'club': Item("Club", "Solid oak club"),

    'bucket': Item("Bucket", "Old metal conatiner")
}





wrapper = textwrap.TextWrapper(width=50)

def get_word_list(current_room):
     word_list = wrapper.fill(text=room[current_room].description)
     print(word_list)

def get_room_key(room_name):
    for k, v in room.items():
        if room_name == v.name:
            return k

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Put items in their starting rooms
room['outside'].items.append(item['bucket'])
room['foyer'].items.append(item['ladder'])
room['overlook'].items.append(item['shovel'])
room['narrow'].items.append(item['rope'])
room['treasure'].items.append(item['club'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player_1 = Player('Player_1','outside')


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
    
    
    print("Current Room: ", player_1.current_room, "\n")
    print("Items in room: ", room[player_1.current_room].items, "\n")

    
    # prints room description
    get_word_list(player_1.current_room)
    print('\n')
    
    cmd = input('What do?:')

    if cmd == 'q':
        print("Goodbye")
        sys.exit()

    if cmd == 'n':
        try:
            player_1.current_room = get_room_key(room[player_1.current_room].n_to.name)
            print("Moved to: ", player_1.current_room, '\n')
        except:
            print('Nothing in that direction, try another path \n')
        continue
    if cmd == 's':
        try:
            player_1.current_room = get_room_key(room[player_1.current_room].s_to.name)
            print("Moved to: ", player_1.current_room, '\n')
        except:
            print('Nothing in that direction, try another path \n')
        continue
    if cmd == 'e':
        try:
            player_1.current_room = get_room_key(room[player_1.current_room].e_to.name)
            print("Moved to: ", player_1.current_room, '\n')
        except:
            print('Nothing in that direction, try another path \n')
        continue
    if cmd == 'w':
        try:
            player_1.current_room = get_room_key(room[player_1.current_room].w_to.name)
            print("Moved to: ", player_1.current_room, '\n')
        except:
            print('Nothing in that direction, try another path \n')
        continue

    if cmd.startswith('take'):
        t_item = cmd[5:]
        t_item = item[t_item.lower()]
        if t_item in room[player_1.current_room].items:
            room[player_1.current_room].items.remove(t_item)
            player_1.items.append(t_item)
            t_item.on_take()
        else:
            print("Invalid input")
        continue

    if cmd.startswith('drop'):
        d_item = cmd[5:]
        d_item = item[d_item.lower()]
        if d_item in player_1.items:
            player_1.items.remove(d_item)
            room[player_1.current_room].items.append(d_item)
            d_item.on_drop()
        else:
            print("Invalid input")
        continue

    if cmd == 'i' or cmd == 'inventory':
        print("Currently held item(s): ", player_1.items)
        continue

    else:
        print("Invalid command \n")