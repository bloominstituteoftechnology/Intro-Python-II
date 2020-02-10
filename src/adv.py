from item import Item
from room import Room
from player import Player
from shutil import get_terminal_size

# set screen size
cols, rows = get_terminal_size()

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     visible_items=['gumdrop']),

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

item = {
    'gumdrop' : Item('gumdrop', 'A plump, delicious-looking gumdrop candy.',
                     {'Eat the gumdrop.':
                        {'default':"You pop the gumdrop your mouth. It's not too bad, if a bit stale.",
                        'hungry':"You gobble down the gumdrop without even chewing. But it doesn't satisfy your hunger."}
                     }
                    )

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
Player = Player(input("Your name?"), room['outside'], status_effects=['hungry'])

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

def move(choice):
    """Attempt to move in a cardinal direction or return current room"""
    if choice == 'n':
        movement = Player.current_room.n_to
    elif choice == 's':
        movement = Player.current_room.s_to
    elif choice == 'e':
        movement = Player.current_room.e_to
    elif choice == 'w':
        movement = Player.current_room.w_to

    if movement == None:
        return Player.current_room
    else:
        return movement

while True:
    print("\n"*(rows-23), Player.current_room.name.upper())
    print("\n", Player.current_room.__directions__(), "\n")
    print(Player.current_room.description)
    if Player.current_room.visible_items:
        print("In the room you can see: ",
              ", ".join([item[x].name for x in Player.current_room.visible_items]))
    choice = input("Choose an action: ")
    if choice == "q":
        print("quit game!")
        break
    if any(x in choice for x in Player.current_room.visible_items):
        chosen = list(set(choice.split(" ")) & set(Player.current_room.visible_items))[0]
        print(f"Options:")
        options = {}
        for i, option in enumerate(item[chosen].options.keys()):
            options[str(i)] = option
            print(f"{i}. " + option)
        key = input("Choose an option: ")
        if key not in list(options.keys()):
            print(key)
            print(list(options.keys()))
            print("You think better of it.")
            continue
        action = options[key]
        if any(x in item[chosen].options[action].keys() for x in Player.status_effects):
            effect = list(set(Player.status_effects) & set(item[chosen].options[action].keys()))[0]
            print(item[chosen].options[action][effect])
            continue
        else:
            print(item[chosen].options[action]['default'])
            continue
    if choice not in ['n', 's', 'e', 'w']:
        print("You can't just sit here. Choose a direction!")
        continue
    else:
        movement = move(choice)
        if movement == Player.current_room:
            print("Can't go that way!")
            continue
        else:
            Player.current_room = movement
