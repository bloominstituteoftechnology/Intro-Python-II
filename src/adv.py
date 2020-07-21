from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside': Room("cave entrance", "North of you, the cave mouth beckons."),

    'entrance': Room("entrance", """Dim light filters in from the south. Dusty passages run north, east and west."""),

    'cliff': Room("steep cliff", """A steep cliff appears before you, falling into the darkness. 
    There is a passage to the north, overgrown with what might be tree roots. There appears to be no way across the chasm."""),

    'passage1': Room("narrow passage", """A narrow passage bends here from west to north."""),

    'chamber': Room("chamber", """You've found a small alcove. The only exit is to the south."""),

    'passage2': Room("wide passage", """A wide passage stretches out before you. You can't see the end of it. 
    You think you see some faint light in the east."""),
    # Future rooms, accessible only by hookshot.
    'chasm': Room("other side of the chasm", """You've made it over the chasm! But there is no way to get back across. 
    A faint light flickers in the passage to the north. Hopefully it leads to a way out."""),

    'passage3': Room("dimly lit passage", """A musty smell fills the air in this damp passage.  
    There is a dim light coming from the north, or you can walk into the darkness to the south."""),

    'cavern': Room("large cavern", """The passage leads you into a large cavern with a small lake.  
    There is a hole in the ceiling here.  Light is streaming through the hole, making the lake glimmer.""")
}

#Declare all the items

item = {
    'sword': Item("rusty sword", """A rusty sword lies here."""),

    'coin': Item("gold coin", """There is a small gold coin here. Might be valuable."""),

    'key': Item("key", """A dingy key lies here. Might be useful."""),

    'rations': Item("rations", """Some old military rations are here. Hopefully they haven't expired."""),

    'hookshot': Item("hookshot", """A spring-loaded, trigger-pulled hook attached to
        lengthy chains. It can can attack enemies at a distance, 
        retrieve remote items, and attach onto certain surfaces 
        (like wood) to pull you across large distances."""),

    'chest': Item("chest", """A dusty old chest lies in the corner here.""", True, False, True, True),
}


# Link rooms together

room['outside'].n_to = room['entrance']
room['entrance'].s_to = room['outside']
room['entrance'].n_to = room['cliff']
room['cliff'].s_to = room['entrance']
room['passage1'].n_to = room['chamber']
room['chamber'].s_to = room['passage1']
room['entrance'].e_to = room['passage1']
room['passage1'].w_to = room['entrance']
room['passage2'].e_to = room['entrance']
room['entrance'].w_to = room['passage2']
room['passage2'].w_to = room['passage2']
# Chasm will be north of the cliff, once the hookshot is functional.
room['chasm'].n_to = room['passage3']
room['passage3'].s_to = room['chasm']
room['passage3'].n_to = room['cavern']
room['cavern'].s_to = room['passage3']

# Add items to room
room['cliff'].items = [item['key']]
room['chamber'].items = [item['chest']]
#TODO: Add items inside of chest.

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

def print_commands():
    print("""Commands:
    \'n\', \'s\', \'e\', or \'w\'   Move north, south, east, or west.
    \'inv\'                         Look at your inventory.
    \'look\'                        Look around.
    \'look at <item>\'              Look at an item.
    \'look in <item>\'              See all the items in a container.
    \'take <item>\'                 Pickup an item.
    \'drop <item>\'                 Drop an item.
    \'unlock <item> with <key>\'    Unlock a locked item.
    \'open <item>\'                 Open a closed item.
    \'help\'                        See this command list again.
    \'q\'                           Quit\n""")

# Begin Program
possible_directions = ['n', 's', 'e', 'w']
player_name = input("\nPlease enter your name.\n")
print(f"\nHi {player_name}.  Good luck on your adventure. Type 'help' for a list of commands.")
player = Player(player_name, room['outside'])
player.print_location_status()

# REPL 
while True:
    cmd = input("What would you like to do?\n").strip().lower().split()   
    num_words = len(cmd)

    if num_words == 1:
        cmd = cmd[0]
        if cmd == 'q':
            print(f"\nSee you soon, {player_name}.\n")
            break
        if cmd in possible_directions:
            player.try_direction(cmd)
            continue
        elif cmd == 'look':
            player.print_location_status()
        elif cmd == 'help':
            print_commands()
        elif cmd == 'inv':
            player.look_at_inventory()
            continue
    elif num_words == 2:
        verb = cmd[0]
        item_name = cmd[1]
        if verb == 'get' or verb == 'take':
            player.try_add_item_to_inventory(item_name)
            continue
        elif verb == 'drop':
            player.try_drop_item_from_inventory(item_name)
            continue
        elif verb == 'open':
            player.open_item(item_name)
            continue
        elif verb == 'unlock':
            print(f"\nWhat should I unlock the {item_name} with?")
    elif num_words == 3:
        verb = cmd[0]
        preposition = cmd[1]
        item_name = cmd[2]
        if verb == 'look':
            if preposition == 'at':
                player.look_at_item(item_name)
                continue
            elif preposition == 'in':
                # look in container
                continue
    elif num_words == 4:
        verb = cmd[0]
        item_name = cmd[1]
        key_name = cmd[3]
        if verb == 'unlock':
            player.unlock_item(item_name, key_name)
    else:
        print("\nInvalid input, please try again.")