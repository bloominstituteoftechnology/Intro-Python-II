from room import Room
from player import Player
from item import Item
import getpass
import time

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons",
                    Item("Cracked Axe", 
                         "While better days have been seen, this blood-soaked axe is better than nothing",
                         10,
                         4,
                         3)),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", Item("Coat","It's getting cold in here. No one should notice one missing coat", 0, 6, 3)),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", Item("Magic Sandwich", "You need to summon your spiritual strength for victory", "0","1","10")),

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
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
playerName = getpass.getuser().title()

print("\nAncient prophecies have fortold your arrival...\n\nWelcome {}!".format(playerName))
player = Player(playerName, room["outside"])

# Write a loop that:
#e
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

intro = """
The Forsaken Dungeon is full of terrors and treasure.

Beware the creatures and dark magic lurking around every corner."""

instructions = """
Search each room for the untold bounties of this realm 
using the four cardinal directions (n, s, w, e). 

To inspect a room for items, use (b) to browse and (l) to loot.

If you wish to return to safety, simply quit the game (q).
Your treasure will be lost as everything is temporary...even your inevitable suffering.
"""

print(intro)
time.sleep(4)
print(instructions)
time.sleep(4)
print("\nStarting location: " + player.location.name)

user_prompt = "\nMove, browse, loot, or quit, the choice is yours... "

directions = ["n", "s", "e", "w"]

# Next part of game
response = ""
while response not in directions:
    
    response = input(user_prompt)

    if response == "n":
        player.move(response)
        print("Current location: " + player.location.name, "\nPrevious direction input: ", response)
        time.sleep(2)
        response = ""

    elif response == "s":
        player.move(response)
        print("Location: " + player.location.name, "\nPrevious direction input: ", response)
        time.sleep(2)
        response = ""

    elif response == "w":
        player.move(response)
        print("Location: " + player.location.name, "\nPrevious direction input: ", response)
        time.sleep(2)
        response = ""

    elif response == "e":
        player.move(response)
        print("Location: " + player.location.name, "\nPrevious direction input: ", response)
        time.sleep(2)
        response = ""

    elif response == "b":

        if player.browse_room_contents != []:
            time.sleep(2)
            print("\nName:", player.browse_room_contents.name, 
                "\nDescription:", player.browse_room_contents.description,
                "\nDamage:", player.browse_room_contents.damage,
                "\nDurability:", player.browse_room_contents.durability,
                "\nMana:", player.browse_room_contents.mana)
        else:
            time.sleep(2)
            print("\nNothing left to loot")

    elif response == "l":
        if player.location.loot != []:
            player.loot()
            print("\nYou're quite the wicked scoundrel. Here's your updated inventory:\n")
            time.sleep(2)
            print([item.name for item in player.items])
        else:
            time.sleep(2)
            print("Nothing left to loot. I'm serious.")

    elif response == "i":
        time.sleep(2)
        print("Player Inventory:\n\n" + player.items)

    elif response == "q":
        print("\n\nThanks for playing")
        time.sleep(2)
        quit()

    else:
        time.sleep(2)
        print("I didn't understand that.\n")
