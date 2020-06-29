from room import Room
import textwrap
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

# Items
room['treasure'].add_item(Item("Treasure Chest", 50))
room['overlook'].add_item(Item("Key", 1))
room['foyer'].add_item(Item("Gold", 20))
room['narrow'].add_item(Item("Sword", 15))

#
# Main
#
player = Player("Wyatt", room['outside'])
def print_menu():
    print(f"----MENU----")
    print("N: Travel north")
    print("S: Travel south")
    print("E: Travel east")
    print("W: Travel west")
    print("I: Check the room for items")
    print("Take [item]: Pick up an item from the room")
    print("Drop [item]: Drop an item from your inventory")
    print("M: Print current location")
    print("L: Print menu")
    print("Q: Quit the game")
def print_location():
    print(f"---Current Location---\n{player.location.get_name()}")
    for line in textwrap.wrap(player.location.get_description()):
        print(f"{line}")
print_menu()
print()
print_location()
while True:
    choice = input("\nAction > ")
    if choice.lower() == "n":
        if player.location.n_to == None:
            print("Nothing in this direction.")
        else:
            player.location = player.location.n_to
            print(f"---Current Location:---\n{player.location.get_name()}")
            for line in textwrap.wrap(player.location.get_description()):
                print(line)
    elif choice.lower() == "e":
        if player.location.e_to == None:
            print("Nothing in this direction.")
        else:
            player.location = player.location.e_to
            print(f"---Current Location:---\n{player.location.get_name()}")
            for line in textwrap.wrap(player.location.get_description()):
                print(line)
    elif choice.lower() == "s":
        if player.location.s_to == None:
            print("Nothing in this direction.")
        else:
            player.location = player.location.s_to
            print(f"---Current Location:---\n{player.location.get_name()}")
            for line in textwrap.wrap(player.location.get_description()):
                print(line)
    elif choice.lower() == "w":
        if player.location.w_to == None:
            print("Nothing in this direction.")
        else:
            player.location = player.location.w_to
            print(f"---Current Location:---\n{player.location.get_name()}")
            for line in textwrap.wrap(player.location.get_description()):
                print(line)
    
    elif choice.lower() == "take treasure chest":
        hasKey = False
        for item in player.inventory:
            if item.name == "Key":
                item = player.location.take_item("Treasure Chest")
                player.add_item(item)
                hasKey = True
        if hasKey == False:
            print("You need a key in your inventory to pick up the treasure chest.")
        else:
            print("Congratulations, you win. Game Over.")
            break
    elif choice.lower() == "take key":
        item = player.location.take_item("Key")
        player.add_item(item)
    elif choice.lower() == "take sword":
        item = player.location.take_item("Sword")
        player.add_item(item)
    elif choice.lower() == "take gold":
        item = player.location.take_item("Gold")
        player.add_item(item)
    elif choice.lower() == "drop key":
        item = player.drop_item("Key")
        player.location.add_item(item)
    elif choice.lower() == "drop sword":
        item = player.drop_item("Sword")
        player.location.add_item(item)
    elif choice.lower() == "drop gold":
        item = player.drop_item("Gold")
        player.location.add_item(item)
    elif choice.lower() == "i":
        print(player.location.get_items())
    elif choice.lower() == "l":
        print_location()
    elif choice.lower() == "m":
        print_menu()
    elif choice.lower() == "q":
        print("Game Over.")
        break
    else:
        print("Invalid action. Please try again.")


