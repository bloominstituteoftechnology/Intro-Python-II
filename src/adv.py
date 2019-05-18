# from room import Room
import re
from room import Room
from player import Player
from subprocess import call
from os import system, name 
from time import sleep


def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 


# Declare all the rooms

room = {
    'eastport': Room("East Portico", """This is where we greet our guests.""",[]),

    'enterancehall': Room("Enterance Hall", """Please come in.""",[]),

    'parlor': Room("Parlor", """Gossip and tea served daily.""", ['CARDS', 'CUP', 'NOTE']),

    'westport': Room("West Portico", """Take in a view of the gardens.""", ['ROSE', 'FIGURINE', 'SKETCHBOOK']),

    'library': Room("Library", """All manners of Manor's business are conducted in the library.""", ['LEDGER', 'BOOK', 'GLOBE']),

    'dininghall': Room("Dining Hall", """Join us for a feast or just a bite to eat.""", ['FORK', 'CANDLE', 'NAPKIN']),

    'guestroom': Room("Guest Room", """Stay awhile.""", ['PITCHER', 'PILLOW', 'FRAME']),

    'northterrace': Room("North Terrace", """Lovely views of the nearby village.""", ['LILY', 'BINOCULARS', 'CRICKET BAT']),

    'drawingroom': Room("Drawing Room", """Looking for a quiet spot to read or embroider? You've found the spot.""", ['NOVEL', 'PAINTBRUSH', 'NEEDLE']),

    'masterbedroom': Room("Master Bedroom", """Where the Lord and Lady of The Manor take their rest.""", ['MIRROR', 'GLOVE', 'KEYS']),

    'greenhouse': Room("Greenhouse", """The finest tomatoes in the parish.""", ['TOMATO', 'SHEARS', 'PEAR']),

    'southterrace': Room("South Portico", """Vistas overlooking the pond.""", ['LILAC', 'TOYBOAT', 'NECKLACE']),
}


# Link rooms together

room['eastport'].n_to = room['enterancehall']
room['enterancehall'].s_to = room['eastport']
room['enterancehall'].n_to = room['parlor']
room['enterancehall'].w_to = room['drawingroom']
room['enterancehall'].e_to = room['library']
room['parlor'].n_to = room['westport']
room['parlor'].s_to = room['enterancehall']
room['parlor'].e_to = room['dininghall']
room['parlor'].w_to = room['masterbedroom']
room['westport'].s_to = room['parlor']
room['library'].n_to = room['dininghall']
room['library'].w_to = room['enterancehall']
room['dininghall'].s_to = room['library']
room['dininghall'].e_to = room['guestroom']
room['dininghall'].w_to = room['parlor']
room['guestroom'].e_to = room['northterrace']
room['guestroom'].w_to = room['dininghall']
room['northterrace'].w_to = room['guestroom']
room['drawingroom'].n_to = room['masterbedroom']
room['drawingroom'].e_to = room['enterancehall']
room['masterbedroom'].s_to = room['drawingroom']
room['masterbedroom'].e_to = room['parlor']
room['masterbedroom'].w_to = room['greenhouse']
room['greenhouse'].e_to = room['masterbedroom']
room['greenhouse'].w_to = room['southterrace']
room['southterrace'].e_to = room['greenhouse']

#
# Main
#

lady = Player("Lady Abigayle", room['eastport'], ['HAT', 'PARASOL', 'BODICE'])
clear()
title = "\n    ______)          __     __)              \n   (, /  /)         (, /|  /|                \n     /  (/    _       / | / |  _  __   _____ \n  ) /   / )__(/_   ) /  |/  |_(_(_/ (_(_)/ (_\n (_/              (_/   '                    \n\n"

print(title)


print("\nWelcome to The Manor, " + lady.name + "! \n We are so looking forward to hosting you this Season. \n\n")

print("You are currently in the " + lady.curr_room.name + ".\n" + lady.curr_room.description + "\n\n")

def contents():
    output = ''
    for i in lady.curr_room.contents:
        output += (" " + i.capitalize() + "\n--<>--<>--<>--\n")
    return output

def collection():
    collect = input("If you would like to take an item, type 'Take' and the item. \n Or you may type 'No': ")
    if len(collect) != 0:
        if collect.split()[0].upper() == 'TAKE' or collect.split()[0].upper() == 'NO':
            if collect.split()[0].upper() == 'TAKE':
                lady.inventory.append(collect.split()[1].upper())
                lady.curr_room.contents.remove(collect.split()[1].upper())
                clear()
                print(title)
                lady.curr_room = lady.curr_room
                print('Welcome to the ' + lady.curr_room.name + '\n' + lady.curr_room.description + "\n\n")
                if len(lady.curr_room.contents) != 0:
                    print ('Before you, you see the following items:\n')
                    print(contents())
                    print("\n")
                else:
                    print("There is nothing in this room to add to your reticule.\n\n")
            else:
                if collect.split()[0].upper() == 'NO':
                    clear()
                    print(title)
                    lady.curr_room = lady.curr_room
                    print('Welcome to the ' + lady.curr_room.name + '\n' + lady.curr_room.description + "\n\n")
                    if len(lady.curr_room.contents) != 0:
                        print ('Before you, you see the following items:\n')
                        print(contents())
                        print("\n")
                else:
                    print("There is nothing in this room to add to your reticule.\n\n")
        else:
            print("\nYou must specify 'Take' or 'No'\n")

def rid():
    collect = input("If you would like to take an item, type 'Leave' and the item. \n Or you may type 'No': ")
    if len(collect) != 0:
        if collect.split()[0].upper() == 'LEAVE' or collect.split()[0].upper() == 'NO':
            if collect.split()[0].upper() == 'LEAVE':
                lady.curr_room.contents.append(collect.split()[1].upper())
                lady.inventory.remove(collect.split()[1].upper())
                clear()
                print(title)
                lady.curr_room = lady.curr_room
                print('Welcome to the ' + lady.curr_room.name + '\n' + lady.curr_room.description + "\n\n")
                if len(lady.curr_room.contents) != 0:
                    print ('Before you, you see the following items:\n')
                    print(contents())
                    print("\n")
                collection()
            else:
                if collect.split()[0].upper() == 'NO':
                    clear()
                    print(title)
                    lady.curr_room = lady.curr_room
                    print('Welcome to the ' + lady.curr_room.name + '\n' + lady.curr_room.description + "\n\n")
                    if len(lady.curr_room.contents) != 0:
                        print ('Before you, you see the following items:\n')
                        print(contents())
                        print("\n")
                        collection()
                    else:
                        print("There is nothing in this room to add to your reticule.\n\n")
        else:
            print("\nYou must specify 'Take' or 'No'\n")

selection = ""

while selection != 'Q':
    selection = input("Would you like to travel N-North, S-South, E-East, or W-West about The Manor \n or you may R-Check your possesions in your reticule or Q-Quit: ")
    selection = selection.upper()
    if len(re.findall("[NSEWRQ]", selection)) == 1:
        if selection == 'N':
            if hasattr(lady.curr_room, 'n_to'):
                clear()
                print(title)
                lady.curr_room = lady.curr_room.n_to
                print('Welcome to the ' + lady.curr_room.name + '\n' + lady.curr_room.description + "\n\n")
                if len(lady.curr_room.contents) != 0:
                    print ('Before you, you see the following items:\n')
                    print(contents())
                    print("\n")
                    collection()
                else:
                    print("There is nothing in this room to add to your reticule.\n\n")
            else:
                clear()
                print(title)
                print("Sorry, there is nothing in that direction.\n\n")
        elif selection == 'S':
            if hasattr(lady.curr_room, 's_to'):
                clear()
                print(title)
                lady.curr_room = lady.curr_room.s_to
                print('Welcome to the ' + lady.curr_room.name + '\n' + lady.curr_room.description + "\n\n")
                if len(lady.curr_room.contents) != 0:
                    print ('Before you, you see the following items:\n')
                    print(contents())
                    print("\n\n")  
                else:
                    print("There is nothing in this room to add to your reticule.\n\n")
            else:
                clear()
                print(title)
                print("Sorry, there is nothing in that direction.\n\n")
        elif selection == 'E':
            if hasattr(lady.curr_room, 'e_to'):
                clear()
                print(title)
                lady.curr_room = lady.curr_room.e_to
                print('Welcome to the ' + lady.curr_room.name + '\n' + lady.curr_room.description + "\n\n")
                if len(lady.curr_room.contents) != 0:
                    print ('Before you, you see the following items:\n')
                    print(contents())
                    print("\n\n")  
                else:
                    print("There is nothing in this room to add to your reticule.\n\n")
            else:
                clear()
                print(title)
                print("Sorry, there is nothing in that direction.\n\n")
        elif selection == 'W':
            if hasattr(lady.curr_room, 'w_to'):
                clear()
                print(title)
                lady.curr_room = lady.curr_room.w_to
                print('Welcome to the ' + lady.curr_room.name + '\n' + lady.curr_room.description + "\n\n")
                if len(lady.curr_room.contents) != 0:
                    print ('Before you, you see the following items:\n')
                    print(contents())
                    print("\n\n")  
                else:
                    print("There is nothing in this room to add to your reticule.\n\n")
            else:
                clear()
                print(title)
                print("Sorry, there is nothing in that direction.\n\n")
        elif selection == 'R':
            clear()
            print(title)
            print("Reticule Contents:\n")
            for i in lady.inventory:
                print("  " + i.title())
                print("--<>--<>--<>--")
            print('\n\n')
            rid()
        elif selection !='Q':
            clear()
            print(title)
            print("Please select a valid command.\n\n")

if selection == 'Q' :
    clear()
    print(title)
    print("It has been a pleasure, please visit again soon.")
    sleep(2)
    clear()
    quit()
