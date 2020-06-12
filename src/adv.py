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

# Room Items
room['outside'].items = [Item("Magic Sword", "Sword will melt your enemies")]
room['foyer'].items = [Item("Glowing Orb", "Lights up the darkest of rooms")]
room['overlook'].items = [Item("Shield", "Protects against lightning")]
room['narrow'].items = [Item("Hat", "Instant wisdom!")]
room['treasure'].items = [Item("Golden Chest", "Grants infinite wealth")]
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input("Enter your characters name: ")
player = Player(player_name, room["outside"])
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
def next_move(direction_input):
    directions = {
        "n":("n_to","north"),
        "e":("e_to", "east"),
        "s":("s_to", "south"),
        "w":("w_to", "west"),
    }

    if direction_input.lower() == 'q' or direction_input.lower() == 'quit':
        return False

    possible_room = player.current_room.__getattribute__(directions[direction_input][0])

    if possible_room != None:
        player.current_room = possible_room
    else:
        print (f"""there is no available room to the {directions[direction_input][1]}""")  
        print (f"this is possible room {possible_room}")
    return True       


continue_adventure = True   

while continue_adventure:
    print(player)
    print(player.current_room)
    selection = input(
      """Please select a direction that you would like to go in 
      n - North
      e - East
      s - South
      w - West
      i, inventory - inventory
      q, quit - Quit
      """)

    if len(selection) > 1:
        if selection[0] == "take":
            player.take_item(selection[1]) 
        elif selection[0]  == "drop":
            player.drop_item(selection[1])    

    else:
        if selection[0] == "i" or selection[0] == "inventory":
            player.show_inventory()  
        else:
            continue_adventure = next_move(selection[0])              

    

