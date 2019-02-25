from room import Room
from player import Player

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

room['foyer'].addItem('rusty sword', 'a rusty sword - don\'t trust it in a fight!')
room['foyer'].addItem('chest', 'a small chest - what does it contain?')
room['foyer'].addItem('sign', 'a sign on the wall - might be worth a read')
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player("Waldo", "outside",[])

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
current_location = room['outside']

def change_rooms(current_room,direction):
    global current_location
    room_attrs = {
        "n":"n_to",
        "s":"s_to",
        "w":"w_to",
        "e":"e_to"
    }
    try:
        #current_room = current_room[room_attrs[direction]]
        print(room_attrs[direction])
        current_location = getattr(current_room, room_attrs[direction])

    except AttributeError:
        print('You can\'t go in that direction!')
while True:
    print(f'You are in {current_location.name}')
    print(current_location.description)
    print('(To move to another room, enter a cardinal direction in form \'n\', \'s\', \'w\', \'e\')')
    action = input('What do you want to do?').lower()
    actionList = action.split()
    if len(actionList) > 1:
        if actionList[0]=='get':
            print('room items',
            current_location.list)
            if any(obj.name==actionList[1] for obj in current_location.list):
                print('found it!')

                thisItem = next((item for item in current_location.list if item.name == actionList[1]), None)
                player1.addItem(thisItem)
                current_location.removeItem(thisItem)
                print(type(thisItem))
                print('in the middle')
                player1.listItems()
                current_location.listItems()
            else:
                print('no such item')
    elif action == 'q':
        break
    else:
        change_rooms(current_location, action)
