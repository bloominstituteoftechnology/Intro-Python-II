from room import Room

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

# Declare all the items

items = {
    'sword':    Item("sword", """a close range weapon used to defeat enemies, cut tall grass and break open clay pots"""),
    'rupee':    Item("rupee", """this is the primary local unit of currency and can be used to purchase items from the local store"""),
    'key':      Item("key", """this key looks like it would fit into a lock on a treasure chest."""),
    'potion':   Item("potion", """drink this potion to replenish your health if you are running low."""),
    'hookshot': Item("hookshot", """a spring-loaded, trigger -pulled hook attached to some lengthy chains. It can atttack enemies at a distance"""),    
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

# Add items to room:

room['outside'].items = [item['sword']]
room['foyer'].items = [item['ruppee'], item['potion']]
room['overlook'].items = [item['hookshot']]
room['treasure'].items = [item['key']]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

def print_valid_commands():
    print("""Valid commands:
          \'n\', \'s\', \'e\', or \'w\'   move North, south, east, or west
          \'take <item>\'            pickup an item, where <item> is the item name and
          \'drop <item>\'            drop an item, where <item> is the item name
          \'i\' or \'inventory\'     view the items currently in your inventory
          \'q\'                      quit\n""")
    
    
    # Program Start:
    
    possible_directons = ['n', 's', 'e', 'w']
    player = Player("David", room["outside"])
    
    player.print_location_status()
    print_valid_commands()
    
    # REPL Start:
    cmd = input("What would you like to do?").strip().lower().split
    num_words = len(cmd)
    
    if num_words == 1:
        cmd = cmd[0]
        if cmd == 'q':
            print("\nThanks for playing!\n")
            # break
        if cmd in possible_directons:
            player.try_direction(cmd)
            # continue
        elif cmd == 'i' or cmd == 'inventory':
            player.print_inventory()
            # continue
        elif num_words == 2:
            verb = cmd[0]
            item_name = cmd[1]
            if verb == 'get' or verb == 'take':
                player.try_add_item_to_inventory(item_name)
                # continue
            elif verb == 'drop':
                player.try_drop_item_from_inventory(item_name)
                # continue
            
        print("Invalid input, please try again.\n")
        print_valid_commands()


