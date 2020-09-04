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
}

items = {
   'hundred': Item("One Hundred Dollars", "Ca$h usable when you complete your adventure"),
   'lightsaber': Item("Light Saber", "Weird, I didn't know there were Jedi in this game"),
   'rabbitFriend': Item("Rabbit", "A rabbit who likes to live in adventurers backpacks")
}

room['narrow'].items = items['rabbitFriend']
room['overlook'].items = items['hundred']
room['foyer'].items = items['lightsaber']

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


directions = ['n', 'e', 's', 'w']
actions = ['t', 'd', 'take', 'drop']

#
# Main
#
playername = input('Sorcerer: What be thy name? ')
player = Player(playername,room['outside'])
print(f"Sorceror: May you find your adventure worthy, {player.name}")
helpstring = print("You can use the following commands: \n N: Move North \n E: Move East \n S: Move South \n W: Move West \n T or Take + Item: Take item \n D or Drop + Item: Drop Item \n I: examine Inventory \n H: Help (prints the commands) \n Q: Quit if this be thy wish")

# Make a new player object that is currently in the 'outside' room.


# Write a loop that:
#
while True:
    if player.room.items != []:
        print(player.room.items)
    else:
        print('No items in this room.')
    print(
        "Your current room:",
        "\n",
        player.room.name,
         "\n", 
         player.room.description
         )
    direction = (input("Input a command: ")).lower()
    if len(direction) == 1:
        if direction == "q": 
            break
        elif direction == "n":
            if hasattr(player.room, "n_to"):
                player.room = player.room.n_to
            else: 
                print("You don't find a room to the north of you")
        elif direction == "e":
            if hasattr(player.room, "e_to"):
                player.room = player.room.e_to
            else:
                print("You don't find a room to the east of you")
        elif direction == "s":
            if hasattr(player.room, "s_to"):
                player.room = player.room.s_to
            else:
                print("You don't find a room to the south of you")
        elif direction == "w":
            if hasattr(player.room, "w_to"):
                player.room = player.room.w_to
            else:
                print("You don't find a room to the west of you")
        elif direction == "i":
            if player.inventory != []:
                print(player.inventory)
            else:
                print(f"Your satchel is empty, {player.name}")
        elif direction == "h":
            print("You can use the following commands: \n N: Move North \n E: Move East \n S: Move South \n W: Move West \n T or Take + Item: Take item \n D or Drop + Item: Drop Item \n I: examine Inventory \n H: Help (prints the commands) \n Q: Quit if this be thy wish")
    elif len(direction) == 2:
        if direction[0] == "t" or direction[0] == "take":
            player.take(player.room.items[0])
        elif direction[0] == "d" or direction[0] == "drop":
            player.drop(player.room.items[0])
    # print(direction)


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# 
# If the user enters a cardinal direction, attempt to move to the room   there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
