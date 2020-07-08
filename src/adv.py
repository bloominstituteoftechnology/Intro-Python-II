from room import Room
from player import Player
from item import Item
import time

# function to return key for any value 
def get_key(val): 
    for key, value in room.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

# Declare all the items
item1 = Item('sword', 'The blade is sharp. I best be careful with this. Hopefully I won\'t need to use it.')
item2 = Item('shield', 'An old wooden shield with some wierd symbols engraved on it.')
item3 = Item('bow', 'This is useless unless I can find some arrows...')
item4 = Item('arrows', 'Sharp! Now if only I had a bow...')
item5 = Item('hookshot', 'Maybe I can cross that chasm with this...')

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item2]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item1]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item3]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item4, item5]),
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

# Main
name = input('--------------------------------------------\nWhat is your adventurer\'s name?\n--------------------------------------------\n')
player = Player(name, 'outside', [])
user_input = "p"

while user_input != "q":
    print("--------------------------------------------\nLOCATION:\nThe", room[player.current_room].name)
    print(room[player.current_room].description)
    if len(room[player.current_room].items) > 0:
        print('\nNEARBY ITEMS:')
        for item in room[player.current_room].items:
            print('A', item.name, '-', item.description)
    print('\nPick an action for', player.name)

    user_input = input("\n\n        [n] North\n[w] West         [e] East\n        [s] South\n\n\n[i] Inventory\n[g] Grab an item\n[q] Quit\n\n")

    if user_input == 'n':
        try:
            player.current_room = get_key(room[player.current_room].n_to)
        except:
            print('There is nothing to be gained by going in this direction...')
            time.sleep(1.5)
    if user_input == 'e':
        try:
            player.current_room = get_key(room[player.current_room].e_to)
        except:
            print('There is nothing to be gained by going in this direction...')
            time.sleep(1.5)
    if user_input == 's':
        try:
            player.current_room = get_key(room[player.current_room].s_to)
        except:
            print('There is nothing to be gained by going in this direction...')
            time.sleep(1.5)
    if user_input == 'w':
        try:
            player.current_room = get_key(room[player.current_room].w_to)
        except:
            print('There is nothing to be gained by going in this direction...')
            time.sleep(1.5)
    if user_input == 'i':
        for item in player.items:    
            print(item.name, ' ', item.description)
        time.sleep(1.5)
    if user_input == 'g':
        for item in room[player.current_room].items:
            player.items.append(item)
            room[player.current_room].items.remove(item)
