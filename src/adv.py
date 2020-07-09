from room import Room
from player import Player
from item import Item
import time
import tkinter as tk

# function to return key for any value 
def get_key(val): 
    for key, value in room.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

# Instantiate all the items
item1 = Item('sword', 'The blade is sharp. I best be careful with this. Hopefully I won\'t need to use it.')
item2 = Item('shield', 'An old wooden shield with some wierd symbols engraved on it.')
item3 = Item('bow', 'This is useless unless I can find some arrows...')
item4 = Item('arrows', 'Sharp! Now if only I had a bow...')
item5 = Item('hookshot', 'Maybe I can cross that chasm with this...')

# Instantiate all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),
    'glory':  Room("You win!!!",
                     "You have achieved eternal glory! You collected all the items and crossed the great chasm!!!", []),

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
room['overlook'].n_to = room['glory']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# GUI experimenting
# from tkinter import *
# from tkinter.ttk import *
# master = tk.Tk()
# pane = Frame(master)
# greeting = tk.Label(text="What is your adventurer\'s name?")
# greeting.pack()
# entry = tk.Entry(fg="yellow", bg="blue", width=50)
# entry.pack()
# name = entry.get()
# pane.pack_forget()
# mainloop()

# Main
name = input('--------------------------------------------\nWhat is your adventurer\'s name?\n--------------------------------------------\n')
player = Player(name, 'outside', [])
user_input = ["p"]

while user_input[0] != "q":
    # Prompt based on room and items
    print("--------------------------------------------\nLOCATION:\nThe", room[player.current_room].name)
    print(room[player.current_room].description)
    if len(room[player.current_room].items) > 0:
        print('\nNEARBY ITEMS:')
        for item in room[player.current_room].items:
            print(item.name, '-', item.description)

    user_input = input("\n\n        [n] North\n[w] West         [e] East\n        [s] South\n\n\n[i] Inventory\n[get [ITEM_NAME]] Grab an item\n[drop [ITEM_NAME]] Drop an item\n[q] Quit\n\n")

    # Split input
    user_input = user_input.split()
    if len(user_input) == 2:
        if user_input[0] == 'get' or user_input[0] == 'take':
            for item in room[player.current_room].items:
                if item.name == user_input[1]:
                    player.items.append(item)
                    room[player.current_room].items.remove(item)
                    item.on_take()
                    time.sleep(1.5)
                else:
                    print('That item doesn\'t seem to be in this room!')
                    time.sleep(1.5)
        if user_input[0] == 'drop':
            if len(player.items) == 0: 
                print('You\'re inventory is empty!')
                time.sleep(1.5)  
            for item in player.items:
                if item.name == user_input[1]:
                    room[player.current_room].items.append(item)
                    player.items.remove(item)
                    item.on_drop()
                    time.sleep(1.5)
                else:
                    print('That item isn\'t in your inventory!')
                    time.sleep(1.5)   
                   
    

    # Action based on input
    if user_input[0] == 'n':
        if room[player.current_room].n_to != None and player.current_room != 'overlook':
            #if len(player.items) == 5
            player.current_room = get_key(room[player.current_room].n_to)
        elif len(player.items) == 5 and player.current_room == 'overlook':
            player.current_room = get_key(room[player.current_room].n_to)
        elif len(player.items) < 5 and player.current_room == 'overlook':
            print('Maybe if I collect all the items I\'ll be able to cross this chasm...')
            time.sleep(1.5)
        else:
            room[player.current_room].invalid_room()
    if user_input[0] == 'e':
        if room[player.current_room].e_to != None:
            player.current_room = get_key(room[player.current_room].e_to)
        else:
            room[player.current_room].invalid_room()
    if user_input[0] == 's':
        if room[player.current_room].s_to != None:
            player.current_room = get_key(room[player.current_room].s_to)
        else:
            room[player.current_room].invalid_room()
    if user_input[0] == 'w':
        if room[player.current_room].w_to != None:
            player.current_room = get_key(room[player.current_room].w_to)
        else:
            room[player.current_room].invalid_room()
    if user_input[0] == 'i':
        for item in player.items:    
            print(item.name, ' ', item.description)
        time.sleep(1.5)
