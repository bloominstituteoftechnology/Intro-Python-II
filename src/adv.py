from room import Room
from player import Player
from item import Item

# Declare all the rooms
# Initial commit comment!

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", items=[Item('dagger', 'A short, sharp and pointy piece of metal.')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items=[Item('lantern', 'A cast iron lantern. Useful for lighting your way.')]),

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
curPlayer = Player(room['outside'])
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
userInput = ['']
running = True
while running:
    try:
        while userInput[0] != 'q':
            print(curPlayer.current_room.__str__())
            print('You can move north with \'n\' south with \'s\' east with \'e\' and west with \'w\'.')
            print('You can access your inventory with \'i\' or \'inventory\'')
            userInput = input('What would you like to do?\nPress q to quit.:: ')
            userInput = userInput.split()
            if (userInput[0] == 'q'):
                running = False
            if (len(userInput) == 1):
                if (userInput[0] == 'n' or userInput[0] == 'north'):
                    if (curPlayer.current_room.n_to != 0):
                        curPlayer.current_room = curPlayer.current_room.n_to
                elif (userInput[0] == 's' or userInput[0] == 'south'):
                    if (curPlayer.current_room.s_to !=0):
                        curPlayer.current_room = curPlayer.current_room.s_to
                elif (userInput[0] == 'e' or userInput[0] == 'east'):
                    if (curPlayer.current_room.e_to != 0):
                        curPlayer.current_room = curPlayer.current_room.e_to
                elif (userInput[0] == 'w' or userInput[0] == 'west'):
                    if (curPlayer.current_room.w_to != 0):
                        curPlayer.current_room = curPlayer.current_room.w_to
                elif (userInput[0] == 'i' or userInput[0] == 'inventory'):
                    print(curPlayer.getInventory())
                else:
                    if (userInput[0] != 'q'):
                        print('I don\'t understand. Please try again.')
            elif len(userInput) > 1:
                if (userInput[0] == 'get' or 'take'):
                    for item in curPlayer.current_room.items:
                        if (item.name == userInput[1]):
                            item.on_take(curPlayer)
                        else:
                            print('There are no items here with that name.')
                if (userInput[0] == 'drop'):
                    for item in curPlayer.items:
                        if (item.name == userInput[1]):
                            item.on_drop(curPlayer)
                        else:
                            print('There are no items by that name in your inventory.')
            else:
                if (userInput[0] != 'q'):
                    print('I don\'t understand. Please try again.')
    except IndexError:
        print('Please input a valid command.')
        userInput = ['']
    except:
        print('An error occured.')

