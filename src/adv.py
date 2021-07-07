from room import Room
from player import Player
from item import Item
import sys
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



#Instantiate a few items
sword = Item('sword', "this is a magical sword")
phone = Item('phone', 'this is the best phone')
coins = Item('coins', 'these coins can buy you more items')

# Make a new player object that is currently in the 'outside' room.
player = Player('Alejandro', room['outside'])
player.currentRoom.items = [sword, phone, coins]
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.

while True:
    print('\n-----------\n')
    print(f'Current room: {player.currentRoom.name}')
    print(f'Room description: {player.currentRoom.description}')
    print(f'Number of items in room: {len(player.currentRoom.items)}')
    user_action = input('What do you want to do? \n Look around the room to find objects (use: list)\n Go to another room (use: north/south/east/west)\n  >')
    actions = user_action.split(' ')
    print(actions)

    if len(actions) == 1:
        if user_action == 'list' or user_action == 'ls':
            if len(player.currentRoom.items) == 0:
                print(f'No items found in room: {player.currentRoom.name}. Go to another room')
            for item in player.currentRoom.items:
                print(f'{item.name}: {item.description}')
        elif user_action == 'inventory' or user_action == 'i':
            if len(player.items) == 0:
                print(f'{player.name} has no items. Take an item from a room')
            for item in player.items:
                print(f'{item.name}: {item.description}')
        elif user_action == 'north' or user_action == 'n' or user_action == "North":
            if player.currentRoom == room['overlook'] or player.currentRoom == room['treasure']:
                print('\nYou cannot go north. Please go back\n')
            else:
                player.currentRoom = player.currentRoom.n_to
        elif user_action == 'south' or user_action ==  's' or  user_action == "South":
            if player.currentRoom == room['outside'] or player.currentRoom == room['narrow']:
                print('\nYou cannot go south. Please go back\n')
            else:
                player.currentRoom = player.currentRoom.s_to
        elif user_action == 'east' or user_action == 'e' or user_action == 'East':
            if player.currentRoom == room['outside'] or player.currentRoom == room['overlook'] or player.currentRoom == room['treasure'] or player.currentRoom == room['narrow']:
                print('\nYou cannot go east. Please go back\n')
            else:
                player.currentRoom = player.currentRoom.e_to
        elif user_action == 'west' or user_action == 'w' or user_action == 'West':
            if player.currentRoom == room['outside'] or player.currentRoom == room['overlook'] or player.currentRoom == room['foyer'] or player.currentRoom == room['treasure']:
                print('\nYou cannot go east. Please go back\n')
            else:
                player.currentRoom = player.currentRoom.w_to

    elif len(actions) == 2:
        verb = actions[0]
        item = actions[1]
        if verb == 'get' or verb == 'take':
            #check to see if items exist in room
           for i in player.currentRoom.items:
                if item == i.name:
                    #remove from Room
                    player.currentRoom.items.remove(i)
                   #add to Player list
                    player.items.append(i)
                    print(f'{i.name} was added to {player.name}\'s items' )
        if verb == 'drop' or verb == 'leave':
            for i in player.items:
                print(i.name)
                if item == i.name:
                    #remove from player list
                    player.items.remove(i)
                    print(f'{i.name} was removed from {player.name}\'s items and added to {player.currentRoom.name}' )
                    
                   #add to room
                    player.currentRoom.items.append(i)
                   
                    
                    

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
