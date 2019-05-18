import random
from os import system, name

from item import Item
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Entrance", """North of you, the large, ornate wooden door
lies slightly ajar, beckoning for you to enter.""", Item('feather', 1)),

    'foyer':    Room("Foyer", """Dim light filters in from the south. A bust
of a pompous-looking old man is displayed proudly in
the center of the room with a guest book on a small
table beneath it, the pages worn with time. The
extravagant tile work on the floor is cracked and
filthy. Dusty passages run north and east.""", Item('fountain pen', 50)),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. The only
way out is to the south""", Item('telescope', 60)),

    'narrow':   Room("Narrow Passage", """The narrow passage tees here and leads
to the east, west, and north. The once glorious carpeting is
now trodden with dirt and soot. Gaudy candleholders line
the hallway.""", Item('candle', 8)),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been nearly emptied by
earlier adventurers. Mere trinkets lie glittering in the
semi-darkness. The only exit is to the south.""", Item("bronze cup", 35)),

    'closet': Room('Closet', """You've entered the bedroom closet. Not much here
but some worn shoes and mothballs. To the west is a doorway.
The north wall has a set of shelves with some scrapes on
the floor in front of them. The south wall has an
impressive display of dress belts and a sock basket. The
light above gently sways as if there's a draft.""", Item("dress belt", 30)),

    'bedroom': Room('Bedroom', """This room has a large four poster bed against
the south wall and light streams through the picture windows
on either side of it. A sizeable wardrobe made of a
beautiful cherry wood is on the north wall. To the east and
west are doorways. There is a chandelier that used to hang
over the bed that has since fallen and now lies in pieces
on the bed and floor around it.""", Item('crystal', 40)),

    'wardrobe': Room('Wardrobe', """The wardrobe is definitely big enough for
you to enter and, as you do, you can see why. It has been
built into the wall to disguise it's roominess. There
is just enough room for a small writing desk and safe.
The safe is open and its contents almost empty. Light comes
from the south entrance""", Item("small gold coin", 100)),

    'secret': Room('Secret Chamber', """The shelves slid aside to expose a small
room that you just know has to hold treasures, but as you
shine your light around, you only find old newspapers, many
of which are almost unreadbale with age. On the north wall
is a poster of a long dead actress. To the east, you see a
reading chair with a small table. This was clearly a room used
to hide from the world and relax. There is an opening in the
south wall.""", Item('vintage pipe', 10))
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
room['narrow'].e_to = room['bedroom']
room['bedroom'].w_to = room['narrow']
room['bedroom'].n_to = room['wardrobe']
room['bedroom'].e_to = room['closet']
room['wardrobe'].s_to = room['bedroom']
room['closet'].w_to = room['bedroom']
room['closet'].n_to = room['secret']
room['secret'].s_to = room['closet']


def clearScr():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')


#
# Main
#
# Make a new player object that is currently in the 'outside' room.
possDirections = {
    "n": "North",
    "s": "South",
    "e": "East",
    "w": "West",
    "q": "Quit"
}

player = Player("Billy", room['outside'])
direction = ''
printedLoc = ""
clearScr()
print("""Welcome, {}! You are have found yourself near an ancient mansion.""".format(player.name))
print("----------------------\n")
print("""There are treasures here and you want to preserve them. But someone
has moved the treasures around the house. You're job is to find
all the treasures and put them in their most logical places.""")
print("----------------------\n\n")
print(input("-----Press enter to begin-----"))
clearScr()

while direction != 'q':
    inputOpts = ""
    inputList = " - "

    for opt in possDirections:
        inputOpts += '- %s (%s)' % (possDirections[opt], opt)
        inputList += opt + ' - '

    while direction != 'q':
        actionItem = ''
        print(str(player.currentLoc))
        print('\nItem list: {}'.format(player.currentLoc.showItems()))
        print('Player inventory: ')

        # This code takes the input and decides if it's a direction or action instruction
        # The else block is an error handler that forces the correction message
        directionList = input(
            inputOpts + '\nWhich instruction do you choose? :').split(" ")
        if len(directionList) == 1:
            direction = directionList[0]
        elif len(directionList) == 2:
            direction = directionList[0]
            actionItem = directionList[1]
        else:
            direction = ''

        clearScr()
        if not(actionItem):
            try:
                youWent = "\nYou chose to move " + possDirections[direction]
                if direction == "n":
                    player.currentLoc = player.currentLoc.n_to
                    print(youWent)
                    break
                elif direction == "w":
                    player.currentLoc = player.currentLoc.w_to
                    print(youWent)
                    break
                elif direction == "e":
                    player.currentLoc = player.currentLoc.e_to
                    print(youWent)
                    break
                elif direction == "s":
                    player.currentLoc = player.currentLoc.s_to
                    print(youWent)
                    break
                elif direction == "q":
                    print("\n\nThanks for playing!!")
            except KeyError:
                print('\nPlease choose a valid option:\n{}\n'.format(inputList))
            except AttributeError:
                print("\nRead the description carefully and choose again.\n")

        if actionItem:
            room = player.currentLoc
            itemCount = sum(r.name == actionItem for r in room.items)
            for i in room.items:
                if i.name == actionItem:
                    itemName = i
            # try:
            youWent = 'You said to {} the {}.'.format(direction, actionItem)
            if direction == 'get' and itemCount:
                room.deleteItem(itemName)
                player.addItem(itemName)
            elif direction == 'drop' and player.items.count(actionItem):
                player.deleteItem(actionItem)
                room.addItem(actionItem)
            # except:
            #     print("""Please use an appropriate command \n
            #     (\"get\" or \"drop\") then (item name) """)



# If the user enters "q", quit the game.
