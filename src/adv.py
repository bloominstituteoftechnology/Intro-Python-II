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
alejandrok = Player('Alejandro', room['outside'])
alejandrok.currentRoom.items = [sword, phone, coins]
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.

while True:
    print('\n-----------\n')
    print(f'Current room: {alejandrok.currentRoom.name}')
    print(f'Room description: {alejandrok.currentRoom.description}')
    user_action = input('What do you want to do? \n Look around the room to find objects (use: list)\n Go to another room (use: north/south/east/west)\n  >')
    actions = user_action.split(' ')
    print(actions)

    if len(actions) == 1:
        if user_action == 'list' or user_action == 'ls':

            if len(alejandrok.currentRoom.items) == 0:
                print(f'No items found in room: {alejandrok.currentRoom.name}. Go to another room')
            for item in alejandrok.currentRoom.items:
                print(f'{item.name}: {item.description}')
        elif user_action == 'north' or user_action == 'n' or user_action == "North":
            if alejandrok.currentRoom == room['overlook'] or alejandrok.currentRoom == room['treasure']:
                print('\nYou cannot go north. Please go back\n')
                break
            else:
                alejandrok.currentRoom = alejandrok.currentRoom.n_to
        elif user_action == 'south' or user_action ==  's' or  user_action == "South":
            if alejandrok.currentRoom == room['outside'] or alejandrok.currentRoom == room['narrow']:
                print('\nYou cannot go south. Please go back\n')
                break
            else:
                alejandrok.currentRoom = alejandrok.currentRoom.s_to
        elif user_action == 'east' or user_action == 'e' or user_action == 'East':
            if alejandrok.currentRoom == room['outside'] or alejandrok.currentRoom == room['overlook'] or alejandrok.currentRoom == room['treasure']:
                print('\nYou cannot go east. Please go back\n')
                break
            alejandrok.currentRoom = alejandrok.currentRoom.e_to
        elif user_action == 'west' or user_action == 'w' or user_action == 'West':
            if alejandrok.currentRoom == room['outside'] or alejandrok.currentRoom == room['overlook'] or alejandrok.currentRoom == room['foyer'] or alejandrok.currentRoom == room['treasure']:
                print('\nYou cannot go east. Please go back\n')
                break
            alejandrok.currentRoom = alejandrok.currentRoom.w_to

    elif len(actions) == 2:
        verb = actions[0]
        item = actions[1]
        if verb == 'get' or verb == 'take':
            #check to see if items exist in room
           for i in alejandrok.currentRoom.items:
                if item == i.name:
                    #remove from Room
                    alejandrok.currentRoom.items.remove(i)
                   #add to Player list
                    alejandrok.items.append(i)
                    print(f'{i.name} was added to {alejandrok.name}\'s items' )
        if verb == 'drop' or verb == 'leave':
            for i in alejandrok.items:
                print(i.name)
                if item == i.name:
                    #remove from player list
                    alejandrok.items.remove(i)
                    print(f'{i.name} was removed from {alejandrok.name}\'s items' )
                   #add to room
                    alejandrok.currentRoom.items.append(i)
                    

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
