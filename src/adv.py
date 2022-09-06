from room import Room
from player import Player
from item import Item
# Declare all the rooms

item = {
    'rusty spoon': Item('rusty spoon', """Just a rusty old spoon, 
                            however you do feel a strange urge to take it outside and get a better look at it"""),
    'dusty sword': Item('dusty sword', 'Just a dusty old sword'),
    'musty cloak': Item('musty cloak', 'Just a musty old cloak'),
    'crusty bones': Item('crusty bones', 'Just some crusty old bones'),
    'lusty tome': Item('lusty tome', 'You dirty dog, you!'),
    'trusty lantern': Item('trusty lantern', 'Just a trusty old lantern')
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     False,
                     [item['trusty lantern'],]
                    ),

    'foyer':    Room("Foyer", 
                    """Dim light filters in from the south. 
                    Dusty passages run north and east.""",
                    True,
                    [item['crusty bones'], item['dusty sword']]
                    ),

    'overlook': Room("Grand Overlook", 
                    """A steep cliff appears before you, falling into the darkness. 
                    Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
                    False,
                    [item['musty cloak'], item['lusty tome']]
                    ),

    'narrow':   Room("Narrow Passage", 
                    """The narrow passage bends here from west to north. 
                    The smell of gold permeates the air.""",
                    True,
                    ),

    'treasure': Room("Treasure Chamber", 
                    """You've found the long-lost treasure chamber! 
                    Sadly, it has already been completely emptied by earlier adventurers. 
                    The only exit is to the south.""",
                    True,
                    [item['rusty spoon']]
                    ),
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
playerName = input('Please enter a name for your hero: ')
hero = Player(playerName, room['outside'])
hero.victory = False
victory_message = """You stand at the cave entrance examining your meager prize.
                    As you turn the rusty spoon over you catch a glimpse of your own reflection.
                    You're filled with a fleeting and bittersweet joy..."""

def actionParser(act):

    if "take " in act:
        itmName = act.replace("take ", "")
        if checkRoomFor(itmName):
            hero.current_room.loot.remove(item[itmName])
            hero.inventory.append(item[itmName])
            print(f"picked up {itmName}")
        else:
            print(f"There is no {itmName} in this room. Try searching the room to reveal any items!")

    elif "pick up " in act:
        itmName = act.replace("pick up ", "")
        if checkRoomFor(itmName):
            hero.current_room.loot.remove(item[itmName])
            hero.inventory.append(item[itmName])
            print(f"picked up {itmName}")
        else:
            print(f"There is no {itmName} in this room. Try searching the room to reveal any items!")

    elif "inspect " in act:
        itmName = act.replace("inspect ", "")
        if checkInventoryFor(itmName):
            if itmName == 'rusty spoon' and hero.current_room.name == "Outside Cave Entrance":
                hero.victory = True
            else:
                print(item[itmName].__str__())
        else:
            print(f"You don't have any {itmName} in your inventory")
    
    elif "drop " in act:
        itmName = act.replace("drop ", "")
        if checkInventoryFor(itmName):
            hero.inventory.remove(item[itmName])
            hero.current_room.loot.append(item[itmName])
            print(f"dropped {itmName}")
        else:
            print(f"You don't have any {itmName} in your inventory")

def checkInventoryFor(itm):
    hasItem = False
    for i in hero.inventory:
        if i.name == itm:
            hasItem = True
    return hasItem

def checkRoomFor(itm):
    hasItem = False
    for l in hero.current_room.loot:
        if l.name == itm:
            hasItem = True
    return hasItem

def checkDarkness():
    if checkInventoryFor('trusty lantern'):
        return False
    elif hero.current_room.isDark == False:
        return False
    else:
        return True


while True:
    
    if hero.victory == True:
        print(victory_message)
        print('Thanks for playing and congrats on making it to the end!')
        break

    if checkDarkness():
        print("It's too dark to see!")
    else:
        print(hero.current_room.__str__())

    action = input("What do you wish to do: ")
    
    if action == "n":
        try: hero.current_room.n_to  
        except: print("You can't go that way")
        else:
            hero.current_room = hero.current_room.n_to

    elif action == "s":
        try: hero.current_room.s_to 
        except: print("You can't go that way")
        else:
            hero.current_room = hero.current_room.s_to

    elif action == "e":
        try: hero.current_room.e_to
        except: print("You can't go that way")
        else:
            hero.current_room = hero.current_room.e_to

    elif action == "w":
        try: hero.current_room.w_to
        except: print("You can't go that way")
        else:
            hero.current_room = hero.current_room.w_to

    elif action == "search":
        if checkDarkness():
            print("It's too dark to search")
        else:
            hero.current_room.searchRoom()

    elif "take " in action:
        actionParser(action)

    elif "pick up " in action:
        actionParser(action)
    
    elif "inspect " in action:
        if checkDarkness():
            print("It's too dark to inspect")
        else:
            actionParser(action)

    elif "drop " in action:
        actionParser(action)

    elif action == "i":
        hero.showInventory()

    elif action == "q":
        confirm = input("You will lose all progress! Are you sure (y to confirm, any other key to cancel)")
        if confirm == 'y':
            print("thanks for playing")
            break
    else:
        print("Please choose a valid action!")