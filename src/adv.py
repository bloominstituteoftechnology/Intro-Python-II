from room import Room
from player import Player
from item import Item

#
# Main
#
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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
rock = Item("rock", "this is a rock")
water = Item("water", "this is a water")
onion = Item("onion", "this is a onion")
unicycle = Item("unicycle", "this is a unicycle")
player = Player("Michael", room['outside'])
room['outside'].items.append(rock)
room['foyer'].items.append(rock)
room['overlook'].items.append(rock)
room['narrow'].items.append(rock)
room['treasure'].items.append(rock)

room['outside'].items.append(water)
room['foyer'].items.append(water)
room['overlook'].items.append(water)
room['narrow'].items.append(water)
room['treasure'].items.append(water)

room['outside'].items.append(onion)
room['foyer'].items.append(onion)
room['overlook'].items.append(onion)
room['narrow'].items.append(onion)
room['treasure'].items.append(onion)

room['outside'].items.append(unicycle)
room['foyer'].items.append(unicycle)
room['overlook'].items.append(unicycle)
room['narrow'].items.append(unicycle)
room['treasure'].items.append(unicycle)
# for item in player.currentRoom.items:
#     print(item.name)
# Make a new player object that is currently in the 'outside' room.

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

while True:
    cmd = input("-> ").split()
    if cmd[0] in ["n", "s", "e", "w"]:
        player.travel(cmd[0])
    elif cmd[0] == "q":
        break
    elif len(cmd) == 2 and (cmd[0] == "get" or cmd[0] == "take"):
        item = cmd[1]
        player.add_item(item)
        print("You currently possess", player.all_items())
    else:
        print("I did not understand that command\n")
