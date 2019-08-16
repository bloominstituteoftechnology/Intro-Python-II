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


rock = Item('rock', 'this is a rock')
broken_sword = Item('broken_sword', 'this sword is useless might have useable parts')
healing_herb = Item('healing_herb', 'this herb has a common healing agent')
common_sword = Item('common_sword', 'this is an everyman sword')
gold_coin = Item('single_gold_coin', 'this is worth $1')
barrel = Item('barrel', 'this was used to make mead but empty now')
broken_shaft = Item('broken_shaft', 'broken speak shaft might have some use')

room["outside"].items.append(rock)
room["outside"].items.append(healing_herb)
room["foyer"].items.append(common_sword)
room["foyer"].items.append(broken_sword)
room["treasure"].items.append(gold_coin)
room["treasure"].items.append(barrel)
room["narrow"].items.append(broken_shaft)



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

inital_room = room["outside"]
name = input("Enter your name: ")
player1 = Player(name, inital_room)

print("Hello " + name + " welcome to adventure quest!")
print("you are currently " + player1.current_room.name + " and " + player1.current_room.description)
# print(f"current items in the room is: {inital_room.items}")
while True:

    print(f'Your current inventory is: {player1.inventory}')

    print(f"current items in the room is: {player1.current_room.items}")
    action = input("Do you want to 'get x' and item or 'drop x' an item: ")
    detail = action.split(" ")

    # print(detail)

    if detail[0] not in ["get", "drop"]:
        pass
    elif detail[0].lower() == 'get':

        item = player1.current_room.get_item(detail[1])
        # print(item)

        if item == None:
            print("That item is not in the room.")
        else:
            player1.current_room.items.remove(item)
            player1.inventory.append(item)
            item.take_item()
            print(f'Your current inventory is: {player1.inventory}')
            print(f"current items in the room is: {player1.current_room.items}")


    elif detail[0].lower() == 'drop':
        # print(player1.get_item(detail[1]))
        item = player1.get_item(detail[1])
        # print(item)
        if item == None:
            print("That item isn't in your inventory")
        else:
            player1.current_room.items.append(item)
            player1.inventory.remove(item)
            item.drop_item()
            print(f'Your current inventory is: {player1.inventory}')
            print(f"current items in the room is: {player1.current_room.items}")


    direction = input("Which direction would you like to go? (n/s/e/w or q to end) ")

    if direction in ['n', 's', 'e', 'w']:
        print("You moved towards " + direction)
        player1.move(direction)

    elif direction == 'q':
        break

    else:
        print("Unrecognized direction please input n/s/e/w or q")

print("Bye Thanks for playing!")
