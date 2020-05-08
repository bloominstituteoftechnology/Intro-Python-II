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
   
    'secret': Room("Secret", """You've found the long-lost treasure
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
room['secret'].n_to = room['outside']


sword = Item("sword", "cutting through flesh")
axe = Item("axe", "battle axe")
torch = Item("torch", "torch")
dagger = Item("dagger", "hunting")
gold = Item("gold", "Yea Buddy")

room['outside'].items = []
room['foyer'].items = [torch]
room['overlook'].items = [dagger]
room['narrow'].items = [axe, sword]
room['treasure'].items = [gold]
room['secret'].items =[map]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newPlayer =Player('Dave', room['outside'])
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

print("\033[1;31;40m \n")

while True:
    action = input('Enter an action: ⚔🤩').split(" ")
    if len(action) == 1 :
        action = action[0]
    
    elif len(action) == 2 :
        new_item = action[1]
        action = action[0]
        

    if action == 'start😎':
        if newPlayer.current_room:
            print(f'{newPlayer.current_room}')
        else:
            print('no path in that direction')
    if action == 'n':
        if newPlayer.current_room.n_to:    
            newPlayer.current_room=newPlayer.current_room.n_to
            print(f'{newPlayer.current_room}')
        else: 
            print('you cannot go north')
    if action == 's':
        if newPlayer.current_room.s_to:
            newPlayer.current_room=newPlayer.current_room.s_to
            print(f'{newPlayer.current_room}')
        else:
            print('no path in that direction')
    if action == 'e':
        if newPlayer.current_room.e_to:
            newPlayer.current_room=newPlayer.current_room.e_to
            print(f'{newPlayer.current_room}')
        else:
            print('no path in that direction')
    if action == 'w':
        if newPlayer.current_room.w_to:
            newPlayer.current_room=newPlayer.current_room.w_to
            print(f'{newPlayer.current_room}')
        else:
            print('no path in that direction')
    if action == 'q':
       exit()

    if action == 'look':
        if newPlayer.current_room.items:
            for obj in newPlayer.current_room.items:    
                print(obj.name)
        else:
            print('no items in your room')

    if action == 'inv':
        newPlayer.print_inventory()
    
    if action in ["take", "get"]:
        for inv in newPlayer.current_room.items:
            if inv.name == new_item:
                newPlayer.add(inv)
                newPlayer.current_room.on_take(inv)
            else:
                print('item is not in the room')

    if action in ["drop", "d"]:
        for inv in newPlayer.inventory:
            if inv.name == new_item:
                newPlayer.remove(inv)
                newPlayer.current_room.on_drop(inv)
            else:
                print('item is not in inventory')

               


