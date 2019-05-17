# from room import Room
import re
import Room from room.py

selection = input("Select N for North, S for South, E for East, or W for West: ")

if len(re.findall("[nNsSeEwW]", selection)) != 1:
    print("Please select a valid direction.")
else:
    print("The user has selected " + selection.upper())

# Declare all the rooms

room = {
    'eastport': Room("East Portico", """Welcome to The Manor."""),

    'enterancehall' = Room("Enterance Hall", """Please come in."""),

    'parlor' = Room("Parlor", """Gossip and tea served daily."""),

    'westport' = Room("West Portico", """Take in a view of the gardens."""),

    'library' = Room("Library", """All manners of Manor's business are conducted in the library."""),

    'dininghall' = Room("Dining Hall", """Join us for a feast or just a bite to eat.""",

    'guestroom' = Room("Guest Room", """Stay awhile."""),

    'northterrace' = Room("North Terrace", """Lovely views of the nearby village."""),

    'drawingroom' = Room("Drawing Room", """Looking for a quiet spot to read or embroider? You've found the spot."""),

    'masterbedroom' = Room("Master Bedroom", """Where the Lord and Lady of The Manor take their rest."""),

    'greenhouse' = Room("Greenhouse", """The finest tomatoes in the parish."""),

    'southterrace '= Room("South Portico", """Vistas overlooking the pond."""),
}


# Link rooms together

room['eastport'].n_to = room['enterancehall']
room['enterancehall'].s_to = room['eastport']
room['enterancehall'].n_to = room['parlor']
romm['enterancehall'].w_to = room['drawingroom']
romm['enterancehall'].e_to = room['library']
romm['parlor'].n_to = room['westport']
romm['parlor'].s_to = room['enterancehall']
romm['parlor'].e_to = room['dininghall']
romm['parlor'].w_to = room['masterbedroom']
romm['westport']s._to = room['parlor']
romm['library'].n_to = room['dininghall']
romm['library']w._to = room['enterancehall']
romm['dininghall'].s_to = room['library']
romm['dininghall'].e_to = room['guestroom']
romm['dininghall'].w_to = room['parlor']
romm['guestroom'].e_to = room['northterrace']
romm['guestroom'].w_to = room['dininghall']
romm['northterrace'].w_to = room['guestroom']
romm['drawingroom'].n_to = room['masterbedroom']
romm['drawingroom'].e_to = room['enterancehall']
romm['masterbedroom'].s_to = room['drawingroom']
romm['masterbedroom'].e_to = room['parlor']
romm['masterbedroom'].w_to = room['greenhouse']
romm['greenhouse'].e_to = room['masterbedroom']
romm['greenhouse'].w_to = room['southterrace']
romm['southterrace']e._to = room['greenhouse']

# #
# # Main
# #

# # Make a new player object that is currently in the 'outside' room.

# # Write a loop that:
# #
# # * Prints the current room name
# # * Prints the current description (the textwrap module might be useful here).
# # * Waits for user input and decides what to do.
# #
# # If the user enters a cardinal direction, attempt to move to the room there.
# # Print an error message if the movement isn't allowed.
# #
# # If the user enters "q", quit the game.
