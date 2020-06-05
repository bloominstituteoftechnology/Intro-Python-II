from room import Room
from textwrap import wrap 
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
# room['outside'].s_to = "Blocked"
# room['outside'].w_to = "Blocked"
# room['outside'].e_to = "Blocked"
# room['foyer'].w_to =  "Blocked"

room['outside'].items_list = {
    'sword': Item('Sword', ' Small tiny sword, looks very fundamental!')
}

room['foyer'].items_list = {
    'Beer': Item('Beer', 'Time to open a party'),
    'Potion': Item('Potion', ' A potion that seems rad')
}

room['narrow'].items_list = {
    'Map': Item('Map', ' This map will guide us through')
}

room['overlook'].items_list = {
    'glasses' : Item('Glasses', ' This glasses are enchanted with a magic. Will be able to see ghosts with it')
}

room['treasure'].items_list = {
    'Wand': Item('Wand', 'The most strong wand you can ever have in the world')
}

#
# Main
#

David = Player("David",room['outside'])


def move_player(user_input):

    if hasattr(David.current_room, f"{user_input}_to"):
        David.current_room = getattr(David.current_room, f"{user_input}_to")
        print(f"You entered [{David.current_room.name}]")
        print(f"{David.current_room.description}")
    else:
    
        print("=======No Door To Next Room=======")
    gaming_running()

def not_valid_needed():
    print("Please enter a valid command, or q to quit the game!")
    gaming_running()

def take_item(item):
    present = 0
    for key, value in David.current_room.items_list.items():
        if value.name.lower() == item:
            David.inventory.append(value)
            value.on_take()
            present = 1
            number = key
    if present == 1:
        David.current_room.items_list.pop(number)
    else:
        print("That item isn't in this room!")
    
    gaming_running()

def drop_item(item):
    present = 0
    for i in range(len(David.inventory)):
        if David.inventory[i].name.lower() == item:
            David.current_room_items.items_list[David.inventory[i].name] = David.inventory[i]

            David.inventory[i].on_drop()
            David.inventory.pop(x)
            present = 1
    if present == 0:
        print(f"Your item, {item}, is not with you")
    gaming_running()

def gaming_running():
    
    #current location
    print(f"\nCurrent Location =>{David.current_room.name}\n{David.current_room.description}")

    print("This room has:")
    if len(David.current_room.items_list) == 0:
        print("There are no items in this room")
    else:
        for key, value in David.current_room.items_list.items():
            print(f"{value.name}:{value.description}")
    print("\n")
    user_input= input("Your Character wants to move either [s]outh, [n]orth, [w]est, [e]ast, [I]nventory, or if you want quit type [q]uit:").lower().split(" ")
    if len(user_input) == 1:
        user_input = user_input[0]
        if user_input == "q":
            print("Dr. Strange says `We are in the endgame now`")
        elif user_input =="i":
            David.print_inventory()
            gaming_running()
        elif user_input == "n" or user_input == "e" or user_input == "s" or user_input == "w":
          move_player(user_input)
        else:
           not_valid_needed()
    elif len(user_input) == 2: 
        if user_input[0] == "take" or user_input[0] == "get":
            David.take_item(user_input[1])
            gaming_running()
        if user_input[0] =="drop":
            David.drop_item(user_input[1])
            gaming_running()
        else:
            not_valid_needed()
    else:
        not_valid_needed()


gaming_running()