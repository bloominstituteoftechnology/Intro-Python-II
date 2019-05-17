# from room import Room
import re
from room import Room
from player import Player

# selection = input("Select N for North, S for South, E for East, or W for West: ")

# if len(re.findall("[nNsSeEwW]", selection)) != 1:
#     print("Please select a valid direction.")
# else:
#     print("The user has selected " + selection.upper())

# Declare all the rooms

room = {
    'eastport': Room("East Portico", """This is where we greet our guests."""),

    'enterancehall': Room("Enterance Hall", """Please come in."""),

    'parlor': Room("Parlor", """Gossip and tea served daily."""),

    'westport': Room("West Portico", """Take in a view of the gardens."""),

    'library': Room("Library", """All manners of Manor's business are conducted in the library."""),

    'dininghall': Room("Dining Hall", """Join us for a feast or just a bite to eat."""),

    'guestroom': Room("Guest Room", """Stay awhile."""),

    'northterrace': Room("North Terrace", """Lovely views of the nearby village."""),

    'drawingroom': Room("Drawing Room", """Looking for a quiet spot to read or embroider? You've found the spot."""),

    'masterbedroom': Room("Master Bedroom", """Where the Lord and Lady of The Manor take their rest."""),

    'greenhouse': Room("Greenhouse", """The finest tomatoes in the parish."""),

    'southterrace': Room("South Portico", """Vistas overlooking the pond."""),
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

lady = Player("Lady Abigayle", room['eastport'])

print("\n")
print("    ______)          __     __)              ")
print("   (, /  /)         (, /|  /|                ")
print("     /  (/    _       / | / |  _  __   _____ ")
print("  ) /   / )__(/_   ) /  |/  |_(_(_/ (_(_)/ (_")
print(" (_/              (_/   '                    ")
print("\n")

print("\nWelcome to The Manor, " + lady.name + "! \n We are so looking forward to hosting you this Season. \n")
# Write a loop that:

print("You are currently in the " + lady.curr_room.name + ".")
print(lady.curr_room.description + "\n")



selection = input("Would you like to travel N-North, S-South, E-East, or W-West about The Manor \n or you may R-Check your possesions in your reticule or Q-Quit: ")
selection = selection.upper()

if len(re.findall("[NSEWRQ]", selection)) == 1:
    while selection != 'Q':
        if selection == 'N':
            if hasattr(lady.curr_room, 'n_to'):
                lady.curr_room = lady.curr_room.n_to
                print('Welcome to  the ' + str(lady.curr_room.name))
                break
            else:
                print("Sorry, there is nothing in that direction.")
        elif selection == 'S':
            if hasattr(lady.curr_room, 's_to'):
                lady.curr_room = lady.curr_room.s_to
                print('Welcome to the ' + lady.curr_room.name)
                break
            else:
                print("Sorry, there is nothing in that direction.")
        elif selection == 'E':
            if hasattr(lady.curr_room, 'e_to'):
                lady.curr_room = lady.curr_room.e_to
                print('Welcome to the ' + lady.curr_room.name)
                break
            else:
                print("Sorry, there is nothing in that direction.")
        elif selection == 'W':
            if hasattr(lady.curr_room, 'w_to'):
                lady.curr_room = lady.curr_room.w_to
                print('Welcome to the ' + lady.curr_room.name)
                break
            else:
                print("Sorry, there is nothing in that direction.")
        elif selection == 'R':
            print("Collection")
        else:
            print("Please select a valid command.")
