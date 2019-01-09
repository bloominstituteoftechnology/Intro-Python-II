from room import Room
from player import Player
from item import Item
import time
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('torch', "it's used to light the way"), Item('coin', "One shiny coin.")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",  [Item('sword', "its very sharp. Ow!"), Item('coin', "One shiny coin.")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",  [Item('chestpiece', "Heavy, but effective!"), Item('coin', "One shiny coin.")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",  [Item('rock', "its pretty heavy"), Item('dagger', "Why was this stuck here?.")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",  [Item('note', "it says IOU. Funny."), Item('coin', "One shiny coin.")]),
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
newPlayer = Player("Grobak The Barbarian", room['outside'], [''])
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
        print(f'You see a {item.name}, {item.description}')
    time.sleep(2)
    print("\nPlease enter n to go up, e to go right, w to go left, or s to go down. Or enter q to quit. ")
    print("\nIf the room has an item, type 'get' and the item name to pick it up!")
    choice = input().lower()
    print('-----')
    print(f'You chose {choice}')
    print('-----')
    choice = choice.split(" ")
    if(len(choice) == 1):
        if(choice[0] == "n"):
            try:
                time.sleep(1)
                newPlayer.currentRoom = newPlayer.currentRoom.n_to
            except AttributeError:
                print("Cannot move North, try a different direction")
                time.sleep(3)
        elif(choice[0] == "e"):
            try:
                time.sleep(1)
                newPlayer.currentRoom = newPlayer.currentRoom.e_to
            except AttributeError:
                print("Cannot move East, try a different direction")
                time.sleep(3)
        elif(choice[0] == "w"):
            try:
                time.sleep(1)
                newPlayer.currentRoom = newPlayer.currentRoom.w_to
            except AttributeError:
                print("Cannot move West, try a different direction")
                time.sleep(3)
        elif(choice[0] == "s"):
            try:
                time.sleep(1)
                newPlayer.currentRoom = newPlayer.currentRoom.s_to
            except AttributeError:
                print("Cannot move South, try a different direction")
                time.sleep(3)
        elif(choice[0] == "q"):
            quit(1)
        elif(choice[0] == "i" or "inventory"):
            if(newPlayer.inventory == ['']):
                print("\nYou have no items. . .")
                time.sleep(3)
            else:
                print(f'\nYou cuurently have {newPlayer.inventory}')
                time.sleep(3)
        else:
            time.sleep(1)
            print("Invalid choice. Please try again.")
            time.sleep(3)
            print('-----\n')
            print('-----\n')
    elif(len(choice) == 2):
        keywords = ["get", "take", "drop"]
        if any(keyword in choice for keyword in keywords):
            if(choice[0] == 'get'):
                for item in newPlayer.currentRoom.items:
                    print(item.name)
                    if(item.name == choice[1]):
                        newPlayer.currentRoom.items.remove(choice[1])
                        newPlayer.inventory.append(choice[1])
                        print(f'You picked up a {choice[1]}')
                        time.sleep(3)
                        break
                    else:
                        print("There is no item in this room with that name")
                        time.sleep(3)
            elif(choice[0] == 'take'):
                if(newPlayer.currentRoom.items["name"] == choice[1]):
                    newPlayer.inventory.append(choice[1])
                else:
                    print("There is no item in this room with that name")
                    time.sleep(3)
            elif(choice[0] == 'drop'):
                if(newPlayer.inventory.name == choice[1]):
                    print(f'You dropped a {choice[1]}')
                    time.sleep(3)
