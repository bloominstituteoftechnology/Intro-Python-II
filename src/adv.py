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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# define items
rock = Item("Rock", "heavy rock for smashing toes.")
sword = Item("Sword", "stricketh thee with thy sword")
oracle = Item("oracle", "Life precious mysteries revealed")
wand = Item(
    "Wand", "Swaths of snakes approach to battle you")

# place items in rooms
# note, if you add items to the starting room, the player will spawn with them in inventory
room['foyer'].items.append(rock)
room['foyer'].items.append(oracle)
room['foyer'].items.append(wand)
room['narrow'].items.append(sword)

# welcome player - learn player's name
print('Welcome to your fated destiny player!')
player_input = input('What is your name?: ')
player = Player(player_input, room['outside'])
print(f'Well, {player.name} get ready for the adventure of a lifetime.')

# print players current room
current_room = player.current_room
print(current_room)

# define valid directions
valid_directions = ["n", "s", "e", "w"]

while True:
    # Wait for user input
    cmd = input(
        """Please enter a cardinal direction in the form of 'n', 's', 'e', or 'w'
or press 'i' to see your inventory 'get' 'drop' for items
press 'q' to quit -> """)
    # Parse user inputs (n, s, e, w, q)
    cmd = cmd.split()
    if cmd[0] in valid_directions:
        # If input is valid, move the player and loop
        player.travel(cmd[0])
        if len(current_room.items) > 0:
            player.items.extend(current_room.items)

    elif cmd[0] == "get":
        if len(cmd) <= 1:
            print("get what?")
            print(player.current_room.items[0].name)
        else:
            # player.addItem(player.current_room.items.index(cmd[1]).name)
            print(player.current_room.items)
            # remove the item from room

    elif cmd[0] == "drop":
        if len(cmd) <= 1:
            print("drop what?")

    elif cmd[0] == "i":
        if player.print_inventory() == "":
            print("Your inventory is empty\n")
        else:
            player.print_inventory()

    elif cmd[0] == "q":
        print("Goodbye!")
        exit()
    else:
        print("I did not recognize that command")
