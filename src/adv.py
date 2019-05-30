from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons."),

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
    "rock": Item("Superrock", "hard, cold, heavy stone"),
    "mirror": Item("Magicmirror", "magical looking glass"),
    "parachute": Item("Partychute", "jump to safety"),
    "flashlight": Item("Lightbeam", "light the way"),
    "gold": Item("Scrooges", "stacks on stacks on stacks"),
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

# Add items to rooms

room['outside'].add_item(item["rock"])
room['foyer'].add_item(item["mirror"])
room['overlook'].add_item(item["parachute"])
room['narrow'].add_item(item["flashlight"])
room['treasure'].add_item(item["gold"])

# room['outside'].items = item["rock"]


# room['outside'].add_item(Item("rock", "hard, cold, heavy stone") )
# room['foyer'].add_item(Item("Magicmirror", "magical looking glass"))
# room['overlook'].add_item(Item("parachute", "safety first, then teamwork"))
# room['narrow'].add_item(Item("flashlight", "light the way") )
# room['treasure'].add_item(Item("gold", "stacks on stacks on stacks"), )



#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Rory", room['outside'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

cmds = ["n", "s", "e", "w"]


while True:
    room = player.current_room

    # * Prints the current room name
    print(f"------------\nYou are in {room.name}\n")

    # * Prints out the player's inventory
    if len(player.inventory) < 1:
        print("You have no inventory")
    
    else:
        print(f'This is your inventory: {player.inventory}')

    print('')

    # * Prints the current description (the textwrap module might be useful here).    
    print(f"{room.description}\n")
    #

    # * Prints the items in the room
    print(f"There is a {room.items} in this room\n")


    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    cmd = input("Enter \"n\" to travel North, \"s\" to go South, \"e\" to go East, \"w\" to go West\n\nEnter \"take\" to pick up an item. \n \nEnter \"drop\" to leave item in room.\n \nEnter \"q\" to quit\n\n")
    
    # splitting the inputs
    cmd = cmd.split()

    if len(cmd) ==1:
        action = cmd[0]

    elif len(cmd) == 2:
        action = cmd[0]
        item = cmd[1]

    # if user enters q, game over    
    if cmd[0] == "q":
        exit()

    # if user enters direction, move to new room
    elif action != "q" and cmd[0] in cmds:
        player.move_player(cmd[0])

    elif action == "take":
        player.get_item(item)

        for i in room.items:
            if i.name == item:
                room.remove_item(i)

    elif action == "drop":
        room.add_item(item)
        
        for i in player.inventory:
            if i == item:
                player.drop_item(i)

        

    else:
        print("That command is not valid. Please try again.")



