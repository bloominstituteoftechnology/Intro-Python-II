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

    'den': Room("Strange Den", """You stumble into the den of a tall lanky eldritch creature.
It quickly grabs hold of you with it's fingers, each one matching the length of your arms.
As it draws you closer, everything fades to black."""),
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
# Declare Player:
player = Player(
    current_room=room["outside"],
    name="David davis"
)
# Declare items
item = {
    'lighter': Item("lighter", "Half empty lighter", 1),
    'survival_knife': Item("survival knife", "Fishing knife", 2),
    'bloody dress': Item("bloody dress", "Bloody dress on the floor",  3),
    'torn note': Item("torn note", "A half of a note", 4),
    'old shoe': Item("old shoe", "Old dress shoe", 5),
}

# Add Items to Rooms:
room['outside'].addItem(item['survival_knife'])
room['foyer'].addItem(item['lighter'])
room['foyer'].addItem(item['bloody dress'])
room['overlook'].addItem(item['torn note'])
room['narrow'].addItem(item['old shoe'])
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
# Start The Game:
game_running = True

# Intro Text:
print(f"\nYour name is {player.name}...\n")
print("The sky thunders as it begins to pour.\nYou see an eerie cave entrance straight ahead of you.\nTo view your controls, enter 'C'.\n")

# Create Input Variable:
player_input = ""

while game_running == True:

    # Quit Function:
    if player_input.lower() == "q":
        print("\nThank you for playing!")
        quit()

   # Take Item Function:
    if player.current_room.items != []:
        for i in player.current_room.items:
            if player_input.lower() == f"take {i.name}":
                player.takeItem(i)
                player.current_room.removeItem(i)
    else:
        if "take" in player_input.lower():
            print("There is nothing to take.")

    # Drop Item Function:
    if player.items != []:
        for i in player.items:
            if player_input.lower() == f"drop {i.name}":
                player.dropItem(i)
                player.current_room.addItem(i)
    else:
        if "drop" in player_input:
            print("You don't have any items...")

    # Drop Item Function:
        if player.items != []:
            for i in player.items:
                if player_input.lower() == f"drop {i.name}":
                    player.dropItem(i)
                    player.current_room.addItem(i)
        else:
            if "drop" in player_input:
                print("You don't have any items...")

                # Repeating Message:
        player_input = str(input("What will you do?: "))
