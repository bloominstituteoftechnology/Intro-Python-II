
from player import Player
from room import Room
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

rock = Item("rock", "This is a rock")
sword = Item("sword", "This is a sword")

pizza = Item("pizza", "This is a pizza")
donut = Item("donut", "This is a donut")

pillow = Item("pillow", "This is a pillow")
chair = Item("chair", "This is a chair")

room["outside"].items.append(rock)
room["foyer"].items.append(sword)
room["overlook"].items.append(pizza)
room["narrow"].items.append(donut)
room["treasure"].items.append(pillow)
room["outside"].items.append(chair)

#itemName = "Rock"
#itemList = room["outside"].items


current_room = room["outside"]
name = input("Please input your name: ")
player = Player(name, current_room)
playerRoom = Room(current_room.name, current_room.description)

while True:

   # print(playerRoom)
   # print(player)
    print(f'Items in current room: {player.current_room.items}')
    print(f'Your current inventory: {player.inventory}')

    direction = input("Please input a direction n/s/e/w: ")

    if direction in ["n", "s", "e", "w"]:
        player.travel(direction)
    elif direction == "q":
        break
    else:
        print("Movement not allowed. Please enter valid direction.")

    action = input("Please input an action get item or drop item: ")
    detail = action.split(" ")
    print(detail)

    if detail[0] == "get":
        item = player.current_room.get_item(detail[1])
        if item == None:
            print("That item is not in the room.")
        else:
           player.current_room.items.remove(item)
           player.inventory.append(item)
           item.on_take()
    elif detail[0] == "drop":
        item = player.get_item(detail[1])
        if item == None:
            print("That item is not in your inventory.")
        else:
            player.current_room.items.append(item)
            player.inventory.remove(item)
            item.on_drop()

print("Thank you for playing!")

'''

current_room = "outside"
# make current_room = room["outside"]
name = input("Please input your name: ")

while True:
    player = Player(name, current_room)
    playerRoom = Room(room[current_room].name , room[current_room].description)
    print(playerRoom)
    print(player)

    direction = input("Please input a direction n/s/e/w: ")

    if direction == "q":
        break
    elif current_room == "outside":
        if direction == "n":
            current_room = "foyer"
        else:
            print("That movement is not allowed")
            continue
    elif current_room == "foyer":
        if direction == "s":
            current_room = "outside"
        elif direction == "n":
            current_room == "overlook"
        elif direction == "e":
            direction == "narrow"
        else:
            print("That movement is not allowed")
            continue
    elif current_room == "overlook":
        if direction == "s":
            current_room = "foyer"
        else:
            print("That movement is not allowed")
            continue
    elif current_room == "narrow":
        if direction == "w":
            current_room = "foyer"
        elif direction == "n":
            current_room = "treasure"
        else:
            print("That movement is not allowed")
            continue
    elif current_room == "treasure":
        if direction == "s":
            current_room = "narrow"
        else:
            print("That movement is not allowed")
            continue

print("Thank you for playing!")
'''


