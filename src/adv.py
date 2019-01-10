from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Club", "well worn wooden club"), Item("Sword", "damaged and rusted iron sword")]),
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

def game():  
# Make a new player object that is currently in the 'outside' room.
    player = Player(room['outside'], [])
    print(player)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    print('Game Options:')
    userInput = input("""[N] North [S] South [E] East [W] WEST [Q] Quit\n
    [(take) + (name of object)] Takes item [(drop) + (name of object)] Drops Item\n""").upper().split()
    print('#######################################################################################')

    while not userInput[0][0] == 'Q':
        
        if len(userInput) == 1:
            if (userInput[0][0] == 'N') and (hasattr(player.room, 'n_to') == True):
                player.room = player.room.n_to
            elif userInput[0][0] == 'S' and (hasattr(player.room, 's_to') == True):
                player.room = player.room.s_to
            elif userInput[0][0] == 'E' and (hasattr(player.room, 'e_to') == True):
                player.room = player.room.e_to
            elif userInput[0][0] == 'W' and (hasattr(player.room, 'w_to') == True):
                player.room = player.room.w_to
            elif userInput[0] == 'I' or userInput[0] == 'INVENTORY':
                print('\nMy Inventory:')
                for item in player.inventory:
                    print(item.name)
            else:
                print('Could not move in that direction')
        elif len(userInput) == 2:
            targetItem = ''
            if userInput[0] == 'TAKE' or userInput[0] == 'GET':
                for item in player.room.items:
                    if item.name.upper() == userInput[1]:
                        item.on_take()
                        player.inventory.append(item)
                        player.room.items.remove(item)
                        
            elif userInput[0] == 'DROP':
                for item in player.inventory:
                    if item.name.upper() == userInput[1]:
                        item.on_drop()
                        player.inventory.remove(item)
                        player.room.items.append(item)
                
        

        print(player)

        print('Game Options:\n')

        if len(player.room.items) > 0:
            print('Items in the room:')
            for item in player.room.items:
                print(item.name)
        
        userInput = input("""\n[N] North [S] South [E] East [W] WEST [Q] Quit\n
        [(take) + (name of object)] Takes item [(drop) + (name of object)] Drops Item\n""").upper().split()
        print('#######################################################################################')
game()


#
# If the user enters "q", quit the game.
