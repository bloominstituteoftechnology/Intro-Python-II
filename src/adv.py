from room import Room
from player import Player
from item import Item
from monster import Monster
import random

# Declare all the rooms
monsterList = {
    'Ogre':  Monster("Ogre", "A giant brown mutant-like monster", 50, Item("Cleaver", "A giant steel meat cutter", random.randint(13,15), 'weapon')),
    'Goblin': Monster("Goblin", "Small green impish creature", 10, Item("Dagger", "A worn small but sharp dagger", 4, 'weapon'))
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [],[]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [],[]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [],[monsterList['Ogre'], monsterList['Goblin']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [],[]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Club", "well worn wooden club",random.randint(4,7), 'weapon'), Item("Sword", "damaged and rusted iron sword", random.randint(9,12), 'weapon'), Item("Bread", "a piece of moldy bread", 0, 'food')],[]),
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


def checkLists(list, input):
    for item in list:
        if item.name.upper() == input:
            return item
        else:
            print('Target does not exist')

#
# Main
#



def game():  
# Make a new player object that is currently in the 'outside' room.
    none = Item('Nothing', 'Empty', 2, 'Nothing')
    player = Player(room['outside'], [], 100, none)
    print(player)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    print('Game Options:')
    userInput = input("""[N] North [S] South [E] East [W] WEST [Q] Quit [C] Controls\n""").upper().split()
    print('#######################################################################################')

    while not userInput[0][0] == 'Q':
        
        if len(userInput) == 1 and len(player.room.monsters) == 0:
            if (userInput[0][0] == 'N') and (hasattr(player.room, 'n_to') == True):
                player.room = player.room.n_to
            elif userInput[0][0] == 'S' and (hasattr(player.room, 's_to') == True):
                player.room = player.room.s_to
            elif userInput[0][0] == 'E' and (hasattr(player.room, 'e_to') == True):
                player.room = player.room.e_to
            elif userInput[0][0] == 'W' and (hasattr(player.room, 'w_to') == True):
                player.room = player.room.w_to
            elif userInput[0] == 'I' or userInput[0] == 'INVENTORY':
                print('My Inventory:')
                for item in player.inventory:
                    print(item.name + ' ' + item.type + ' ' + str(item.damage))
                print(f'\nEquipped Weapon: {player.onhand_weapon.name}')
            elif userInput[0][0] == 'C':
                print("""
                    I => Inventory
                    Equip [item] => Equips selected weapon
                    Unequip [item] => Unequips onhand item
                    Take [item] => Takes selected item from room
                    Drop [item] => Drops selected weapon
                    """)
            else:
                print('Could not move in that direction')
        elif len(userInput) == 2:
            if (userInput[0] == 'TAKE' or userInput[0] == 'GET') and len(player.room.monsters) == 0:
                item = checkLists(player.room.items, userInput[1])
                if item: 
                    item.on_take()
                    player.inventory.append(item)
                    player.room.items.remove(item)       
            elif userInput[0] == 'DROP' and len(player.room.monsters) == 0:
                item = checkLists(player.inventory, userInput[1])
                if item:
                    item.on_drop()
                    player.inventory.remove(item)
                    player.room.items.append(item)
            elif userInput[0] == 'EQUIP':
                item = checkLists(player.inventory, userInput[1])
                if item and item.type == 'weapon':
                    player.onhand_weapon = item
                else:
                    print("That is not a weapon!")
            elif userInput[0] == 'UNEQUIP':
                if not player.onhand_weapon.type == 'None':
                    player.onhand_weapon = none
            elif userInput[0] == 'ATTACK':
                target = checkLists(player.room.monsters, userInput[1])
                if target and target.on_attack(player.onhand_weapon.type) == True:
                    target.health = target.health - player.onhand_weapon.damage
                else:
                    print("Oh no, you're attack missed!")
               
            

                    

        

        print(player)

        print('Game Options:\n')

        if len(player.room.items) > 0:
            print('Items in the room:')
            for item in player.room.items:
                print(item.name)
        if len(player.room.monsters) > 0:
            print(f"YOU'VE RUN INTO {len(player.room.monsters)} MONSTERS")
            for monsters in player.room.monsters:
                print(f'{monsters.name} {monsters.health}')

        
        userInput = input("""\n[N] North [S] South [E] East [W] WEST [Q] Quit [C] Controls\n""").upper().split()
        print('#######################################################################################')
game()


#
# If the user enters "q", quit the game.


