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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal action, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.



items = {'coin': Item('Coin', 'Gold coin worth 1.'),
'lantern': Item('Lantern', 'A lantern that can light up the room.')}
room['outside'].add_items(items['coin'])
room['foyer'].add_items(items['coin'])
room['overlook'].add_items(items['lantern'])

name = input('What is your name, Adventurer? ')
player = Player(name, room['outside'])




print(f'Welcome {name}. Begin your adventure from {player.current_room} \n')
print(room['outside'].show_items())

while True:
    action = input(f'Choose an action. (n for North, s for South, e for East, w for West, take to Pickup item, d to Drop, q to Quit) \n')

    if action == 'n' or action == 'N':
        next_move = player.current_room.n_to
        if next_move == None:
            print("Can't go that way. Try a different direction.")
        else:
            player = Player(name, next_move)
           
            print(player)
            print( player.current_room.show_items())
       
    elif action == 's' or action == 'S':
        next_move = player.current_room.s_to
        if next_move == None:
            print("Can't go that way. Try a different direction.")
        else:
            player = Player(name, next_move)
            print(player)
            print(player.current_room.show_items())
    
    elif action == 'e' or action == 'E':
        next_move = player.current_room.e_to
        if next_move == None:
            print("Can't go that way. Try a different direction.")
        else:
            player = Player(name, next_move)
            print(player)
            print(player.current_room.show_items())
    
    elif action == 'w' or action == 'W':
        next_move = player.current_room.w_to
        if next_move == None:
            print("Can't go that way. Try a different direction.")
        else:
            player = Player(name, next_move)
            print(player)
            print(player.current_room.show_items())


    elif action == 'take' or action == 'get':
        for item in player.current_room.items:
            print(player.pickup_item(item))

        print(player.inventory)

    elif action == 'drop' or action == 'discard':
        for i in player.inventory:
            if i.name == item:
                player.drop_item()
    
    
    elif action == 'i':
        print(player.show_inventory())

    elif action == 'q' or action == 'Q':
        print('Goodbye Adventurer!')
        break
        



