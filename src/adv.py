from room import Room
from player import Player
from item import Item
# Declare all the rooms

item = {
    "wallet": Item("Wallet", "A simple leather wallet, unfortunately it's completely empty, was this yours?"),
    "dirt": Item("Dirt", "It's dirt")
}
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item["wallet"], item["dirt"]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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
# ========================================================================================> Variables ----<
pc = Player("Default", room["outside"], [], 50)
location = pc.location
newLocation = ""
# ========================================================================================> Functions ----<


# Item function handles player obtaining items
def itemHandler():

    if location.items:
        print("     You search the room and find some items of interest:")
        count = 0
        for item in location.items:
            count += 1
            print("     " + item.name + ": " + str(count))
        print("     Take an item?  y/n")
        entry = input(": ")
        if entry == "y":
            print("     Choose an item to take")
            entry = input(": ")
            entry = int(entry) - 1
            pc.inv.append(location.items.pop(entry))

    else:
        print("     There is nothing very interesting here")

# mainActions function handles the primary actions of the game loop


def mainActions():
    global location
    global newLocation
    print(f'''
    {location.desc}
    ''')
    entry = input("""   What will you do?
    Move: n, e, s, w
    Check Location: c
    Check Inventory: b
    Investigate Room: i
    Quit: q
    : """)

    try:
        if entry == 'n':
            newLocation = location.n_to
        elif entry == 'e':
            newLocation = location.e_to
        elif entry == 's':
            newLocation = location.s_to
        elif entry == 'w':
            newLocation = location.w_to
        elif entry == 'c':
            print(f"""
    You are in the {location.name}
            """)
        elif entry == 'q':
            print('''
    Thank you for playing, goodbye
    ''')
            quit()
        elif entry == 'i':
            print('''
    You look around the room...
            ''')
            itemHandler()
        elif entry == 'b':
            print("""
    You look into your bag...
    """)
            for item in pc.inv:
                print(item.name)
        else:
            print("""
    That didnt work, try a different action
    """)
    except AttributeError:
        print('''
    You do not see a way forward in that direction
            ''')
        mainActions()

    if newLocation:
        location = newLocation

    mainActions()
    print(f'''
    {location.desc}
    ''')
    mainActions()


#
# Main
#

# Make a new player object that is currently in the 'outside' room.


print("You wake up, you only remember your name")
pc.name = input("   What is your name: ")
print(f"    Welcome, {pc.name}, your adventure begins.")


mainActions()

# make this a function

# try newLocation variable, and have the location change be assigned to newLocation before the True check, so that player location doesnt get lost
# then assign location to new location of True check succeed


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
