from player import Player
from room import Room
from item import Item, LightSource
import time

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.  There is an old door to the west."""),

    'dungeon':  Room("Dungeon", """The door creaks open to reveal a moldy smelling 
dungeon. You notice a skeleton in the corner of one cell."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", is_light=False),

    'door':     Room("Closed Door", """You find a large door at the north end of 
the passage. It appears to be locked.""", locks=["north"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Something is glittering in the middle! The only exit is to the south."""),
}

# Add items
room['overlook'].add_item(LightSource('torch'))
room['dungeon'].add_item(Item('key'))
room['treasure'].add_item(Item('treasure'))

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['dungeon']
room['dungeon'].e_to = room['foyer']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['door']
room['door'].n_to = room['treasure']
room['door'].s_to = room['narrow']
room['treasure'].s_to = room['door']

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
    
    # If the door is locked...
    if direction in player.current_room.locks:
        if player.has_item("key"):
            print("You open the door with your key.")
            # then move like normal
        else:
            print("The door is locked!")
            return  # do not move

    # Normal movement
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
while not (game_over or player.has_item("treasure")):
    # Print the current room name and description
    print("\n----------------------------------")
    player.current_room.print_description(player.has_light())

    # Ask for player input
    #print("\nWhich direction would you like to go?")
    command = input("\nWhat now? ")

    # Check for empty commands
    if command == "":
        print("No command was entered")
        continue  # go back to top of loop

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

if player.has_item("treasure"):
    print("\n----------------------------------")
    print("You found the treasure!  You win!")

# Out of the loop, game is over
print("\nThanks for playing!")
