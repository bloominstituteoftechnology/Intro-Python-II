from room import Room
from player import Player
from item import Item
import time
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('torch'), Item('coin')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",  [Item('sword'), Item('coin')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",  [Item('chestpiece'), Item('coin')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",  [Item('rock'), Item('dagger')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",  [Item('note'), Item('coin')]),
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
print("Please enter a name for your player. . .")
name = input(">> ")
# Make a new player object that is currently in the 'outside' room.
# (Player name, starting room, initial inventory)
newPlayer = Player(name, room['outside'], [])
time.sleep(1)
print(f'Welcome to the game, {newPlayer.playerName}')
time.sleep(2)
print("Your adventure awaits. . .")
time.sleep(2)
print("You have been tasked with finding the lost gold of Erilith.")
time.sleep(2)
print("Fortune favors the brave. Go and find the treasure. . .")
time.sleep(2)
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
while True:

    print('-----')
    print(f'\nThe current room is {newPlayer.currentRoom.name}\n')
    print('--------------------------------------')
    time.sleep(1)
    print(newPlayer.currentRoom)
    print('--------------------------------------')
    time.sleep(2)
    for item in newPlayer.currentRoom.items:
        print(f'You see a {item}')
    time.sleep(2)
    print("\nPlease enter n to go up, e to go right, w to go left, or s to go down. Or enter q to quit.\nIf you need to access your inventory, you can do so by typing 'i' or 'inventory' ")
    print("\nIf the room has an item, type 'get' and the item name to pick it up!")
    choice = input("'Enter Command'>> ").lower()
    print('-----')
    print(f'You chose {choice}')
    print('-----')
    choice = choice.split(" ")
    # checks if the length of the array is 1 or 2
    # if one, do this set of if/elif statements
    if(len(choice) == 1):
        if(choice[0] == "n"):
            try:
                time.sleep(1)
                # changes the current room to what newPlayer.currentRoom.n_to is equal too
                newPlayer.currentRoom = newPlayer.currentRoom.n_to
            # checks for attribute error which throws if there isnt a room in that direction
            except AttributeError:
                print("Cannot move North, try a different direction")
                time.sleep(3)
        elif(choice[0] == "e"):
            try:
                time.sleep(1)
                # changes the current room to what newPlayer.currentRoom.e_to is equal too
                newPlayer.currentRoom = newPlayer.currentRoom.e_to
             # checks for attribute error which throws if there isnt a room in that direction
            except AttributeError:
                print("Cannot move East, try a different direction")
                time.sleep(3)
        elif(choice[0] == "w"):
            try:
                time.sleep(1)
                # changes the current room to what newPlayer.currentRoom.w_to is equal too
                newPlayer.currentRoom = newPlayer.currentRoom.w_to
             # checks for attribute error which throws if there isnt a room in that direction
            except AttributeError:
                print("Cannot move West, try a different direction")
                time.sleep(3)
        elif(choice[0] == "s"):
            try:
                time.sleep(1)
                # changes the current room to what newPlayer.currentRoom.s_to is equal too
                newPlayer.currentRoom = newPlayer.currentRoom.s_to
             # checks for attribute error which throws if there isnt a room in that direction
            except AttributeError:
                print("Cannot move South, try a different direction")
                time.sleep(3)
        elif(choice[0] == "q"):
            quit(1)
        elif(choice[0] == "i" or "inventory"):
            # checks if the inventory is an empty list
            if(newPlayer.inventory == []):
                print("\nYou have no items. . .")
                time.sleep(3)
            else:
                # lets the play know what is in his inventory
                # note: needs to loop through, currently displays as a list
                print(f'\nYou currently have {newPlayer.inventory}')
                time.sleep(3)
        else:
            time.sleep(1)
            print("Invalid choice. Please try again.")
            time.sleep(3)
            print('-----\n')
            print('-----\n')
    # checks if the length is two (has two words)
    elif(len(choice) == 2):

        if(choice[0] == 'get' or choice[0] == 'take'):
            try:
                # loops through the items in the room
                for index, item in enumerate(newPlayer.currentRoom.items):
                        # if it finds an item with the same name user typed in
                    if(item.name == choice[1]):
                        # adds item to the Player inventory
                        newPlayer.inventory.append(item.name)
                        # removes item from the room
                        newPlayer.currentRoom.items.remove(item)
                        print(f'You picked up a {choice[1]}')
                        time.sleep(3)
                        break
                    elif(index == len(newPlayer.currentRoom.items)-1):
                        # if no item is in the room, print it doesnt exist
                        print("There is no item in this room with that name")
                        time.sleep(3)
                        break
            except AttributeError:
                for index, item in enumerate(newPlayer.currentRoom.items):
                    if(item == choice[1]):
                        # adds item to the Player inventory
                        newPlayer.inventory.append(item)
                    # removes item from the room
                        newPlayer.currentRoom.items.remove(item)
                        print(f'You picked up a {choice[1]}')
                        time.sleep(3)
                        break
                    elif(index == len(newPlayer.currentRoom.items)-1):
                        # if no item is in the room, print it doesnt exist
                        print("There is no item in this room with that name")
                        time.sleep(3)
                        break
        elif(choice[0] == 'drop'):
            # loops through inventory list and checks for item
            for index, item in enumerate(newPlayer.inventory):

                # if it finds the item in inventory

                if(newPlayer.inventory[index] == choice[1]):
                    # remove item from inventory
                    newPlayer.inventory.remove(item)
                    # add item to current room items

                    newPlayer.currentRoom.items.append(item)

                    print(f'You dropped a {choice[1]}')
                    time.sleep(3)
                elif(index == len(newPlayer.inventory)-1):
                    # if no item is in the room, print it doesnt exist
                    print("There is no item in your inventory that matches that name")
                    time.sleep(3)
                    break
