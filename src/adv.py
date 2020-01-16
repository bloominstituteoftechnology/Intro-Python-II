from room import Room
from player import Player
from item import *

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. \
Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, \
falling into the darkness. Ahead to the north, a light flickers in the distance, \
but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west\
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure \
chamber! There are some flickering torches lining the room. You can see the overlook \
from here. Sadly, it has already been completely emptied by earlier adventurers. The \
only exit is to the south."""),
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


# Set dress rooms
room['outside'].items = [
    Rock("Pebbles"),
    Rock("Rocks"),
    Item("Caterpiller")
]

room['foyer'].items = [
    Chair("Chair"),
    Item("BrokenStool"),
    Item("Doorknob")
]

room['overlook'].items = [
    Item("Spiderweb"),
    Rock("Stone")
]

room['narrow'].items = [
    Item("Dust")
]

room['treasure'].items = [
    Item("SeveralCoins"),
    Item("EmptyTreasureChest"),
    Item("LooseTorch")
]
#
# Main
#
# Write a loop that:

    

# Make a new player object that is currently in the 'outside' room.
player = Player(input("Enter your character's name: "), room['outside'])

def printHelp():
    print("""
    The following inputs are valid:
        n - move to the room to the north
        s - move to the room to the south
        e - move to the room to the east
        w - move to the room to the west

        l - look around the room you're in
        i - see what you're holding

        grab/use/drop [item] - interact with items

        q - quit the game
        h - show this help
    """)


directions = ["n", "s", "e", "w"]
inventory = ["i", "inventory"]
lookAround = ['l', "look"]
validTakeCommands = ["take", "grab"]
validUseCommands = ["use"]
validDropCommands = ["drop", "set"]
validCommands = validTakeCommands + validDropCommands + validUseCommands
gameCommands = ['q', 'quit', 'h', 'help']

def promptPlayerInput():
    cmd = input("What do you want to do?: ").lower().split(" ")
    baseCmd = cmd[0]

    if baseCmd in directions:
        changeRooms(baseCmd)
        return

    if baseCmd in inventory:
        player.showInventory()
        return

    if baseCmd in lookAround:
        player.lookAroundRoom()
        return

    if baseCmd in validCommands:
        analyzeInteraction(*cmd)
        return

    if baseCmd in gameCommands:
        analyzeGameCommand(baseCmd)
        return

    # Print an error message if the movement isn't allowed.
    print("Invalid input. Try again.")

def analyzeGameCommand(command):
    # If the user enters "q", quit the game.
    if command == "q" or command == "quit":
        print("Exiting game.")
        exit()
    elif command == "h" or command == "help":
        printHelp()
        return True

def performTake(interaction):
    room = player.current_room
    try:
        itemName = interaction.split(" ")[1]
    except:
        print("No item described. Try again.")
    item = room.itemNamed(itemName)
    if item:
        player.pickUpItem(item)
    else:
        print(f"There's no item named {itemName}")

def analyzeInteraction(*interactions):
    if len(interactions) < 2:
        return
    room = player.current_room
    command = interactions[0]

    try:
        itemName = interactions[1]
    except:
        print("No item described. Try again.")
        return

    roomItem = room.itemNamed(itemName)
    playerItem = player.itemNamed(itemName)

    if command in validTakeCommands:
        if roomItem:
            player.pickUpItem(roomItem)
        else:
            print(f"There's no item in the room named {itemName}")
            return False
    elif command in validUseCommands:
        if playerItem:
            player.useItem(playerItem)
        else:
            print(f"You're not holding an item named {itemName}")
            return False
    elif command in validDropCommands:
        if playerItem:
            player.dropItem(playerItem)
        else:
            print(f"You're not holding an item named {itemName}")
            return False
    else:
        print("Somehow you broke the game!")
        return False
    return True


def changeRooms(direction):
    newRoom = player.current_room.roomInDirection(direction)
    if newRoom:
        player.changeRoom(newRoom)
    else:
        print("That way is blocked! Try something else.")
        promptPlayerInput()


def gameLoop():
    global player
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # print(f"\n{player.name} entered {player.current_room.name}. {player.current_room.description}")
    promptPlayerInput()

def main():
    player.announceCurrentRoom()
    while True:
        gameLoop()

main()
