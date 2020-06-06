from room import Room
from player import Player
from item import Item
import textwrap

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

# [X] Make a new player object that is currently in the 'outside' room.
# print(player1)

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


backpack = Item('Backpack', 'To store your gold')
flashlight = Item('Flashlight', "maybe it's dark inside")
sword = Item('Sword', 'You need this to protect yourself')
rope = Item('Rope', 'You can do anything with it')
fire = Item('Fire', 'You can burn anything')


room['foyer'].items = [sword]
room['overlook'].items = [rope]
room['treasure'].items = [backpack]
room['narrow'].items = [fire]
room['outside'].items = [flashlight]



print("\n\n\nWelcome to the game!\n".upper())    
print("Enter 'h' to get help.\n")   
player = Player("Ann", room['outside'])
choices = ['n', 's', 'w', 'e']
while True: #Loop
    print("\n")
    player_input = input("Enter command -> ").lower().strip()
    print(f'\nYou are at: {player.current_room.name}'.upper())
    print(f'\n{player.current_room.description}\n')

    if player_input in choices:

        if player_input == 'n' and player.current_room.n_to != None:
            player.current_room = player.current_room.n_to
        elif player_input == 's'and player.current_room.s_to != None:
            player.current_room = player.current_room.s_to
        elif player_input == 'w' and player.current_room.w_to != None:
            player.current_room = player.current_room.w_to
        elif player_input == 'e'and player.current_room.e_to != None:
            player.current_room = player.current_room.e_to
        else:
            player_input = input("You can't go that way! type  N, S, E, W -> ").lower().strip()
    elif player_input == 'h':
        print('\nHow to play')
        print("'n' = go North")
        print("'s' = go South")
        print("'w' = go West")
        print("'e' = go East")
        print("'c' = to check room's item")
        print("'t' = to take the item")
        print("'d' = to drop your item")
        print("'i' = to check your inventory")
        # print("'r' = to see your current room")
        print("'q' = to quit")
    elif player_input == 'c':
        print(f'\n\n\n\n{player.current_room.name}')
        for item in player.current_room.items:
            print(f'This room has "{item.name}" \nDiscription: {item.discription}\n\n\nEnter "t" to take "{item.name}"')
    elif player_input == 't':
        for i in player.current_room.items:
            if player_input == 't':
                player.items.append(i)
            else:
                pass
        for i in player.items:
            print(f'\n\n\n\nYou got "{i.name}"\n\n\n\n') 
    elif player_input == 'i':
        print(f"\n\nYour items")
        for i in player.items:
            print(f'Item: {i.name}, {i.discription}')   
    elif player_input == 'd':
        for i in player.items:
            if player.items is not []:
                player.items.remove(i)   
    # elif player_input == 'r':
    #     print(f'\n\n\nYou are at {player.current_room.name}')   
    elif player_input == 'q':
        print('Bye')
        break
    else: 
        print("Invalid command")