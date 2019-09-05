from room import Room
from player import Player
from item import Item
import textwrap

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

items_of_room = {
    'map':  Item("map", "Don't get lost in a cave"),
    'rope': Item("rope", 'Rope can come in handy'),
    'axe': Item("axe", 'Who does not need axe'),
    'backpack': Item("backpack", 'Help you to carry your items'),
    'water': Item("water", 'A sip of fresh water on your journey, what can be better'),
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


# Adding items to the room


room['outside'].items = [items_of_room["map"].name, items_of_room["rope"].name, items_of_room["axe"].name]
room['foyer'].items = [items_of_room["backpack"].name, items_of_room["water"].name]
room['overlook'].items = ['crampons', 'hook']
room['narrow'].items = ['torch']
room['narrow'].items = ['coin']

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

player1 = Player("Player One", "outside")
direction = ''
item_managing = ''

def ask_to_pick_up_item():
    global item_managing
    item_managing = input("Type 'take *item name*' to take the item or 'drop *item name*' to drop it \nTYPE HERE: ")
    manage_inventory(item_managing)

def manage_inventory(item):
    print(f"room {player1.current_room}")
    check_if_item_exist = False
    array_of_command = item.split()

    #['take' case]
    if array_of_command[0] == 'take':

        for thing in room[player1.current_room].items:

            if thing == array_of_command[1]:

                player1.inventory.append(array_of_command[1])
                room[player1.current_room].items.remove(array_of_command[1])
                print(f"Your inventory: {player1.inventory} Items left in the room: {room[player1.current_room].items}")
                items_of_room[array_of_command[1]].on_take()
                check_if_item_exist = True
                return
            
        if not(check_if_item_exist):
            print(f"Sorry this room does not have this item. Choose another item from this room {array_of_command[1]} thing: {thing}")
            ask_to_pick_up_item()

             

def ask_for_location():
    global direction
    direction = input("Type q to quit the game or choose the direction you want to go next: w, n, e, s \nTYPE HERE: ")
    startGame(direction)

def describe_the_room():
    for key, value in room.items():
        if player1.current_room == key:
            print(f"Current Room: \n      {key} \n{value}")
            
    

def startGame(direction):
    if direction == 'q': 
        print("You successfully exited the game")
        return
    if player1.current_room == "outside":
        if direction == 'n':
           player1.current_room = "foyer"
           describe_the_room()
           ask_to_pick_up_item()
           ask_for_location()

        else:
            print ("You hit the wall, try again. You can only go North from outside.")
            ask_for_location()

    elif player1.current_room == "foyer":

        if direction == 's':
           player1.current_room = "outside"
           describe_the_room()
           ask_to_pick_up_item()
           ask_for_location()

        elif direction == 'n':
           player1.current_room = "overlook"
           describe_the_room()
           ask_for_location()

        elif direction == 'e':
           player1.current_room = "narrow"
           describe_the_room()
           ask_for_location()
       
        else:
            print ("You hit the wall, try again. You can not go West from foyer.")
            ask_for_location()

    elif player1.current_room == "overlook":
        if direction == 's':
           player1.current_room = "foyer"
           describe_the_room()
           ask_for_location()

        else:
            print ("You hit the wall, try again. You can only go South from overlook.")
            ask_for_location()

    elif player1.current_room == "narrow":
        if direction == 'w':
           player1.current_room = "foyer"
           describe_the_room()
           ask_for_location()
        
        elif direction == 'n':
           player1.current_room = "treasure"
           describe_the_room()
           ask_for_location()

        else:
            print ("You hit the wall, try again. You can only go West and North from narrow room.")
            ask_for_location()

    elif player1.current_room == "treasure":
        if direction == 's':
           player1.current_room = "narrow"
           describe_the_room()
           ask_for_location()

        else:
            print ("You hit the wall, try again. You can only go South from treasure room.")
            ask_for_location()

describe_the_room()
ask_to_pick_up_item()
ask_for_location()
    