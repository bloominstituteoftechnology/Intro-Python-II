from room import Room
from player import Player
from time import sleep
from item import Item
from os import system

system('cls')
# Declare all the rooms
print("""
###########################
Welcome to the adventure!!!
###########################

GOOD LUCK AND HAVE FUN!!

######################""")
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

    'coward': Room("Coward's Retreat", """By backing away from the cave you've found a
nice place to leisurely reconsider your life choices""",
                   items=[Item('Fire Sword', "A friggin sick flaming sword"),
                          Item("Lion's Heart", "Seems to have once belonged to a Wizard")])
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].s_to = room['coward']
room['coward'].n_to = room['outside']
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
player = Player(room['outside'], name="Bergdorf")
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
### Your location: ###
######################
over = False
valid_directions = ['n', 'e', 's', 'w', 'q']
valid_actions = ['get', 'take']
inv = ['i', 'inventory']
def move(direction, direction_impossible):
    end = '\r'
    for i in range(5):
        if i == 4:
            end = '\n'*3 + '######################\n'
        print(f"You begin to travel {direction}" + i*'.', end=end)
        sleep(0.7)
    system('cls')
    return False

def unable(input_string):
    print('')
    end = '\r'
    for i in range(5):
        if i == 4:
            end = '\n'*3
        print("You are unable to travel in that direction from this room" + i*'.', end=end)
        sleep(0.7)
    input_string = input("Please choose a different direction: ").lower()
    while input_string not in valid_directions:
        input_string = input("Remember that valid directions are n, s, e, or w. Try again: ").lower()
    return input_string
    
while not over:
    print(f'### Your location: ###\n{player.current_room.name}', end='\n' + '######################' + '\n')
    print(f'\n{player.current_room.description}\n')
    print(f'The following items are in this room: {player.current_room.item_names}')

    inp = input("Which action will you take? (q to quit):  ").lower()

    while inp.split()[0] not in (valid_directions + valid_actions + inv):
        print('')
        print("Please choose from North, South, East or West as a direction of travel. Or say 'take'/'drop' followed by an item name.")
        inp = input("Which direction will you travel?(first letter of direction): ").lower()

    if inp == 'q':
        over = True

    if inp in valid_directions:
        direction_impossible = True
        while direction_impossible:
            if inp == 'n':
                  try:
                    player.current_room = player.current_room.n_to
                    direction_impossible = move('North', direction_impossible)
                  except AttributeError:
                    inp = unable(inp)
                    
            if inp == 's':
                  try:
                    player.current_room = player.current_room.s_to
                    direction_impossible = move('South', direction_impossible)
                  except AttributeError:
                    inp = unable(inp)
            if inp == 'e':
                  try:
                    player.current_room = current_room.location.e_to
                    direction_impossible = move('East', direction_impossible)
                  except AttributeError:
                    inp = unable(inp)
            if inp == 'w':
                  try:
                    player.current_room = player.current_room.w_to
                    direction_impossible = move('West', direction_impossible)
                  except AttributeError:
                    inp = unable(inp)
            if inp == 'q':
                direction_impossible = False
                over = True

    if inp.split()[0].lower() == 'drop':
        dropped_item_name = ' '.join(inp.split()[1:]).title()
        if dropped_item_name in player.item_names:
            item_index = player.item_names.index(dropped_item_name)
            dropped_item = player.items.pop(item_index)  # class object
            player.item_names.pop(item_index)  # name list partner
            player.current_room.item_names.append(dropped_item_name)
            player.current_room.items.append(dropped_item)
            dropped_item.on_drop()
            system('cls')
        else:
            print(f"No item named '{dropped_item_name}' exists in your inventory")
            input("Press Enter to continue")
            
    if inp.split()[0].lower() in valid_actions:
        requested_item = ' '.join(inp.split()[1:]).title()
        if requested_item in player.current_room.item_names:
            item_index = player.current_room.item_names.index(requested_item)  # names list indices match items list
            popped_item = player.current_room.items.pop(item_index)  # actual class object
            player.current_room.item_names.pop(item_index)  # removing from name list as well
            player.items.append(popped_item)  # add to player inventory
            player.item_names.append(popped_item.name)  # allows drop functionality similar to take
            popped_item.on_take()
            system('cls')
        else:
            print(f"No item named '{requested_item}' is in this room")
            input("Press Enter to continue")

    if inp.lower() in inv:
        print(f'Your current inventory contains the following:{player.item_names}')
        input("Press Enter to continue")
        system('cls')
