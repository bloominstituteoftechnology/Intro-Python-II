from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item("rake", "A dusty old thing. Looks like it is used to pick up leaves."), Item("bucket", "A bucket with holes in it. Not very useful")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east""", [Item("hour glass", "A broken hour glass. You can't keep track of the time with this.")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm""", [Item("candle", "A partially used candle. Just need a way to light it.")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air""", [Item("gold coin", "A gold coin. Must be getting close to the treasure room."), Item("torch", "An old torch. Needs a way to light it.")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south""", [Item("empty chest", "A dusty, old chest. Completely useless."), Item("skull", "Skull of someone who has been dead for a long time.")])
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
new_player = Player("Jackson", room["outside"], [])

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
print(new_player.current_room)
selection = input('Please select a direction to move using n, s, e, w. You can add items to your inventory with g and drop them with d. If you want to quit, press q.\n')
while(selection != 'q'):
    if selection == 'g':
        if len(new_player.current_room.items) == 0:
            selection = input('There are no more items to pick up. Please make your next move:\n')
        else:
            new_player.pickup_item(new_player.current_room.items[0])
            new_player.current_room.remove_item(new_player.current_room.items[0])
            selection = input('Make your next move:\n')
    if selection == 'd':
        if len(new_player.current_items) < 1:
            selection = input('You have no items to drop. Please make your next move:\n')
        else:
            new_player.current_room.add_item(new_player.current_items[0])
            new_player.drop_item(new_player.current_items[0])

    if new_player.current_room == room['outside'] and selection == 'n':
        new_player.current_room = room['foyer']
        print(new_player.current_room)
        selection = input('Make your next move:\n')
    

    elif new_player.current_room == room['foyer'] and selection == 's':
        new_player.current_room = room['outside']
        print(new_player.current_room)
        selection = input('Please select a direction to move using n, s, e, w, or quit with q:\n')
    

    elif new_player.current_room == room['foyer'] and selection == 'n':
        new_player.current_room = room['overlook']
        print(new_player.current_room)
        selection = input('Please select a direction to move using n, s, e, w, or quit with q:\n')
    

    elif new_player.current_room == room['overlook'] and selection == 's':
        new_player.current_room = room['foyer']
        print(new_player.current_room)
        selection = input('Please select a direction to move using n, s, e, w, or quit with q:\n')
    

    elif new_player.current_room == room['foyer'] and selection == 'e':
        new_player.current_room = room['narrow']
        print(new_player.current_room)
        selection = input('Please select a direction to move using n, s, e, w, or quit with q:\n')
    

    elif new_player.current_room == room['narrow'] and selection == 'w':
        new_player.current_room = room['foyer']
        print(new_player.current_room)
        selection = input('Please select a direction to move using n, s, e, w, or quit with q:\n')
    

    elif new_player.current_room == room['narrow'] and selection == 'n':
        new_player.current_room = room['treasure']
        print(new_player.current_room)
        selection = input('Please select a direction to move using n, s, e, w, or quit with q:\n')
    

    elif new_player.current_room == room['treasure'] and selection == 's':
        new_player.current_room = room['narrow']
        print(new_player.current_room)
        selection = input('Please select a direction to move using n, s, e, w, or quit with q:\n')
    

    
    
