from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Rake", "Primarily used for gardening or fire wood")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Compass", "It's lost"), Item("Torch", "To light your path")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Torch", "Not the superhero")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Coins", "Several coins")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Nothing", "Y'know...nothing")]),
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

def get_room_and_input():
    print(player.current_room)
    print()
    move = input("What direction would you like to go? (n, e, w, s) ~~> ")
    move_list = move.split()
    return move.lower(), move_list

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('player1', room['outside'])

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

if __name__ == "__main__":
    directions = ['n', 's', 'e', 'w']
    move, move_list = get_room_and_input()

    while not move == 'q':
        if len(move_list) == 1:
            ### Where you go to move to new rooms
            if move in directions:
                player.move(move) # attempts to move in requested direction          
                print()
                move, move_list = get_room_and_input()
            elif (move == 'i' or move == 'inventory'): # Looking at inventory
                print("Current inventory: ")
                if (len(player.items) == 0):
                    print('No items')
                for i in range(len(player.items)):
                    print(player.items[i])
                print()
                move, move_list = get_room_and_input()
            else:
                print()
                print('~~~~~~~~~~That command could not be recognized. Please try again.~~~~~~~~~~')
                print()
                move, move_list = get_room_and_input()
        
        else:
            ### Where you go to take/drop items
            if (move_list[0].lower() in ['take', 'get']):
                for room_item in player.current_room.items:
                    if (move_list[1].lower() == room_item.name.lower()):
                        player.get_item(room_item)
                        room_item.on_take()
                        player.current_room.remove_item(room_item)
                        print()
            #if you want to drop an item in your inventory
            elif (move_list[0].lower() in ['drop']): 
                for item in player.items:
                    if (move_list[1].lower() == item.name.lower()): #checks to make sure the item requested is in player inventory
                        player.drop_item(item)
                        item.on_drop()
                        print()
            else:
                print()
                print("~~~~~~~~~~Bad command. Try again...~~~~~~~~~~")
                print()
            move, move_list = get_room_and_input()
