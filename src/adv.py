from room import Room
from player import Player
from item import Item
import time

# create list of items
item = {
    'torch': Item('small torch',
                  """A small torch that lights up the player's current room.
This effect lasts for three room changes."""),
    'key': Item('treasure key',
                 "A small key with a treasure chest encrypted on the side.")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     n_to='foyer'),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty 
passages run north and east.
Sitting upon the wall to your right the soft glow of a torch beckons your attention.""",
                     n_to='overlook', s_to='outside', e_to='narrow',
                     items=item['torch']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.
Next to the chasm you see a faint glimmer of light. Upon closer inspection you recognize it as a key.""",
                     s_to='foyer', items=item['key']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.
At the end of the path to the north is what appears to be a locked door. 
A faint golden glow emanates from a keyhole above the door knob.""",
                     n_to='treasure', w_to='foyer'),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     s_to='narrow'),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['narrow']
room['treasure'].s_to = room['narrow']

# Create input parser 
def input_parser():

    command = input("""Please type one of the following commands: 
n (to go north), s (to go south), e (to go east), w (to go west), p (to pickup an item), u (to use an item), c (to check current inventory), or q (to exit the game)\n""")

    return command

def use_item(player):

    use_item = input(f"In your inventory you have the following item/s: {[i for i in player.inventory]}. Which item would you like to use? ")
    return use_item

def pick_up_item(player):

    try:
            player.inventory.append(player.current_room.items.name)

            print(f"You have picked up {player.current_room.items.name.split('and')}")

            player.current_room.items = None

    except:
            print("There are no items to be found within this room.")

def check_inventory(player):
    try:

        print(f"In your inventory you have the following item/s: {player.inventory}.")

    except:

        print("You currently have no items in your inventory.")

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Daniel", room['outside'])

# welcome player to the game
print(f"Welcome {player.name} to Adventure Text")
time.sleep(1)

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

while True:
    # print player's current location and location description
    print(f"You currently reside in the {player.current_room.name}")
    time.sleep(1)
    print(player.current_room.description)
    time.sleep(1)

    # call input parser for user command
    command = input_parser()

    # player movement based on user input

    # if player input == 'q'
    if command == 'q':
        exit()

    # player input == 'n'
    if command == 'n':
        try:

            if player.current_room.n_to:
                player.current_room = player.current_room.n_to
                print(f"You move north and enter the {player.current_room.name}")
                time.sleep(1)

        except:
            print("You have run into a dead end. try selecting a different direction.")

    # player input == 's'
    if command == 's':
        try:

            if player.current_room.s_to:

                player.current_room = player.current_room.s_to
                print(f"You move south and enter the {player.current_room.name}")
                time.sleep(1)
            
        except:
            print("You have run into a dead end. try selecting a different direction.")

    # player input == 'e'
    if command == 'e':
        try:

            if player.current_room.e_to:

                player.current_room = player.current_room.e_to
                print(f"You move east and enter the {player.current_room.name}")
                time.sleep(1)

        except:
            print("You have run into a dead end. try selecting a different direction.")
    
    # player input == 'w'
    if command == 'w':
        try:

            if player.current_room.w_to:

                player.current_room = player.current_room.w_to
                print(f"You move west and enter the {player.current_room.name}")
                time.sleep(1)
 
        except:
            print("You have run into a dead end. try selecting a different direction.")

    # player input == 'p'
    if command == 'p':
        
        pick_up_item(player)

    # player input == 'u'
    if command == 'u':
        try:
            command = use_item(player)

            if command == 'treasure key':
                
                if (player.current_room.name == "Narrow Passage") and ('treasure key' in player.inventory):

                    print("""You withdraw the key from your pouch, reach forward to insert 
it into the keyhole before you, and you hear a satisfying 'click' as the door is unlocked.""")       
                    room['narrow'].n_to = room['treasure']
                    player.inventory.remove('treasure key')

                else:

                    if player.current_room.name == "Narrow Passage":

                        print("You currently do not posess the treasure key. Try searching elsewhere.")

                    elif 'treasure key' in player.inventory:

                        print("You have no where to use the treasure key.")

        except:

            print("You have no items you can use within this room. Try searching elsewhere.")

    # player input == 'c'
    if command == 'c':

        check_inventory(player)