from room import Room
from item import Item
import sys
import random



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
from item import Item
from player import Player
player = Player("You", room['outside'])

# Declare an item or two
item = {
'flashlight' : Item('Flashlight', 'helps with lighting the way worth 50pts')
}

# Place items in rooms randomly
for _ in range(0, 4):
    rand_room = random.choice(list(room.keys()))
    rand_item = random.choice(list(item.keys()))
    room[rand_room].add_item(rand_item)
#validator for the item:


def take(obj):
    if obj in player.currentRoom.items:
        player.currentRoom.remove_item(obj)
        player.pick_item(obj)
        item[obj].on_pick()
    else:
        print(f'There is no {obj} in this room')


def drop(obj):
    if obj in player.inventory:
        player.drop_item(obj)
        item[obj].on_drop()
    else:
        print(f'There is no {obj} in this room')



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


play = True

justOnce = True

# declaring actions for moving 

# 0 represents the word typed in and 1 represents the item name 

def getInput():
    action = input("What would you like to do? Action: ")
    
    if action[0] == "q":
        global play 
        global justOnce
        play = False
        foundItems = False
        
    elif action[0] == "n":
        if player.currentRoom.playerMove("n") == True:
            player.currentRoom = player.currentRoom.n_to
        if len(player.currentRoom.items) > 0:
            print("\nThis is your inventory:")
            print(player.inventory)
            for item in player.currentRoom.items:
                print(f'\nNew: {rand_item}')
        else:
            print("\nThis is your inventory:")
            
    elif action[0] == "e":
        if player.currentRoom.playerMove("e") == True:
            player.currentRoom = player.currentRoom.e_to
        if len(player.currentRoom.items) > 0:
            print("\nThis is your inventory:")
            print(player.inventory)
            for item in player.currentRoom.items:
                print(f'\nNew: {rand_item}')
        else:
            print("\nThis is your inventory:")
    elif action == "s":
        if player.currentRoom.playerMove("s") == True:
            player.currentRoom = player.currentRoom.s_to
        if len(player.currentRoom.items) >= 0:
            print("\nThis is your inventory:")
            print(player.inventory)
            for item in player.currentRoom.items:
               print(f'\nNew: {rand_item}')
        else:
            print("\nThis is your inventory:")
    elif action[0] == "w":
        if player.currentRoom.playerMove("w") == True:
            player.currentRoom = player.currentRoom.w_to
        if len(player.currentRoom.items) > 0:
            print("\nThis is your inventory:")
            print(player.inventory)
            for item in player.currentRoom.items:
                print(f'\nNew: {rand_item}')
        else:
            print("\nThis is your inventory:")
           # trying to pick up an item here
       

    # Get/Take command
    
    elif action.split(' ')[0] in ["take" , "get"]:
        if len(player.currentRoom.items) > 0:
                take(rand_item)
        else:
            print(f'nothing to pick up!')
            print(player.inventory)
    
    # drop
    elif action.split(' ')[0] in ["drop" , "d"]:
        if len(player.inventory) > 0:
                drop(rand_item)
        else:
            print(f'nothing to drop!')
            print(player.inventory)
    # inventory
    elif action.split(' ')[0] in ["inventory" , "i"]:
        if len(player.inventory) > 0:
            print(player.inventory)
        else:
            print("no items in inventory")
            

    else:
        print (f"\n'{action}' is not valid input")
        getInput()
        
        
while play:

    if justOnce:

        justOnce = False
        print("Use\n" +
        "'n' 'e' 's' 'w' to go north, east, south, or west.\n" +
        "'take' to pick up items'"
        "'q' to quit 'c' to show controls again")
    print("\n" + player.currentRoom.__str__())

    getInput()
