from player import Player
from room import Room
from item import Item, LightSource
import time
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", is_light=False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Something is glittering in the middle! The only exit is to the south."""),
}

# Add items
room['overlook'].add_item(LightSource('torch'))
room['treasure'].add_item(Item('treasure'))

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

def attempt_move(direction):
    """ attempts to move the player in the given direction """

    global back # set the global variable if we move succsesfully

    # If it is dark...
    if not (player.current_room.is_light or player.has_light()):
        # Too dark to move, can only go back
        if direction != back:
            print("It is too dark to see!  You must go back.")
            return
        # Else, player is already going back so move like normal
        
    if direction == "north":
        if player.current_room.n_to is None:
            print("There is no room to the north")
        else:
            player.current_room = player.current_room.n_to
            back = "south"

    elif direction == "south":
        if player.current_room.s_to is None:
            print("There is no room to the south")
        else:
            player.current_room = player.current_room.s_to
            back = "north"

    elif direction == "east":
        if player.current_room.e_to is None:
            print("There is no room to the east")
        else:
            player.current_room = player.current_room.e_to
            back = "west"

    elif direction == "west":
        if player.current_room.w_to is None:
            print("There is no room to the west")
        else:
            player.current_room = player.current_room.w_to
            back = "east"


def print_wrapped(message, width=50):
    """ Prints a message using the textwrap module """
    wrapper = textwrap.TextWrapper(width) 
    message = wrapper.wrap(message) 
    for line in message: 
        print(line)


# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

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

print("--- Welcome to Lambda adventure! ---")
print("To move, enter a direction")
print('To quit, enter "q" or "quit"')

back = ""
game_over = False
while not game_over:
    # Print the current room name and description
    print("\n----------------------------------")
    print_wrapped(player.current_room.name)
    if player.current_room.is_light or player.has_light():
        print_wrapped(player.current_room.description)
    else:
        print("It's pitch black in here!")

    if player.current_room.is_light or player.has_light():
        # Show all items in the room
        for item in player.current_room.items:
            print("You see a", item.name)
    else:
        # Only show light sources
        for item in player.current_room.items:
            if type(item) == LightSource:
                print("You see a", item.name)

    # Ask for player input
    #print("\nWhich direction would you like to go?")
    command = input("\nWhat now? ")

    # Convert to lower case to understand more input options
    command = command.lower()
    
    # Used for multi-word commands
    commands = command.split()

    # Handle player input
    # quit command
    if command in ["q", "quit"]:
        game_over = True
    
    # 5 movement commands
    elif command in ["n", "north"]:
        attempt_move("north")

    elif command in ["s", "south"]:
        attempt_move("south")

    elif command in ["e", "east"]:
        attempt_move("east")
 
    elif command in ["w", "west"]:
        attempt_move("west")
    
    elif command in ["back"]:
        if back == "":
            print("You haven't moved yet, and cannot go back")
        else:
            attempt_move(back)

    # show inventory
    elif command in ["i", "items", "inventory"]:
        if len(player.items) == 0:
            print("You are not holding any items")
        else:
            for item in player.items:
                print("You are holding a", item.name)

    # pick up items
    elif commands[0] in ['get', 'take']:
        # commands[1] should be the item name, attempt to take it
        item = player.current_room.take_item(commands[1])

        if item == None:
            # No item with that name was found in the room
            print(f"There is no {commands[1]} in this room")
        else:
            player.items.append(item)
            item.on_take()  # this also prints the take message

    # drop items
    elif commands[0] in ['drop']:
        # commands[1] should be the item name, attempt to drop it
        player.drop_item(commands[1])

    else:
        print("Sorry, I don't know that command")
    
    time.sleep(.5)  # pause for a moment, helps player see what happens better

# Out of the loop, game is over
print("Thanks for playing!")
