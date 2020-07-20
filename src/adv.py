from room import Room
from player import Player
from item import Item
from character import Enemy

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run west and east. To the north, the room opens up into the grand overlook."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. 
You can go south, or go west."""),

    'narrow':   Room("Narrow Passage", """The narrow passage splits in two here, one way bending to the north
and the other continuing east. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'library': Room("Library", """All four walls have ceiling-high shelves filled with books. 
West of you is the narrow passage you came in through."""),

    'parlor': Room("Parlor", """The room is elegant and eery. The black furniture, dark yet comfortable, seem to eminate more darkness. 
You feel a wave of sudden extreme anxiety, accompanied by the feeling of being unwelcome and unwanted. 
There are two other doors on the north and west walls."""),

    'music': Room("Music Room", """This room is strangely different from all the other rooms. You feel happy and hear calming music. 
The only door leads back east to the parlor."""),

    'kitchen': Room("Kitchen", """Straigh through on the other side is large entrance leading even further north to the dining room."""),    

    'dining': Room("Dining Room", """You see a large fireplace and a table set with crystal. To the east are double doors leading to the grand overlook."""),
}


# Link rooms together
room['outside'].link_room(room['foyer'], 'north')
room['foyer'].link_room(room['outside'], 'south')
room['foyer'].link_room(room['overlook'], 'north')
room['foyer'].link_room(room['narrow'], 'east')
room['foyer'].link_room(room['parlor'], 'west')
room['parlor'].link_room(room['foyer'], 'east')
room['parlor'].link_room(room['kitchen'], 'north')
room['kitchen'].link_room(room['parlor'], 'south')
room['kitchen'].link_room(room['dining'], 'north')
room['dining'].link_room(room['kitchen'], 'south')
room['dining'].link_room(room['overlook'], 'east')
room['parlor'].link_room(room['music'], 'west')
room['music'].link_room(room['parlor'], 'east')
room['overlook'].link_room(room['foyer'], 'south')
room['overlook'].link_room(room['dining'], 'west')
room['narrow'].link_room(room['foyer'], 'west')
room['narrow'].link_room(room['treasure'], 'north')
room['narrow'].link_room(room['library'], 'east')
room['library'].link_room(room['narrow'], 'west')
room['treasure'].link_room(room['narrow'], 'south')

# charactors 
evilCasper = Enemy('Evil Casper', 'An angry evil spirit!')
evilCasper.set_conversation('You are not welcome here, human. Prepare to die.')
evilCasper.set_weakness('crossbow')

# add charactors into rooms
room['parlor'].set_character(evilCasper)

#add items into rooms 
room['library'].add_item_to_room("treasure", "You win.")
room['music'].add_item_to_room("crossbow", "A powerful, ancient weapon.")
room['dining'].add_item_to_room("key", "Unlocks secret room.")
room['overlook'].add_item_to_room("gun", "A pistol.")
# room['library'].add_add_to_room("treasure", "you are winning")
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input('Welcome brave adventurer! Enter your name to get started: ')
player = Player(name, room['outside'])
playing = True

current_room = player.current_room # new variable that holds the starting room. 
# current_room.get_info()
print(F"{player.name}, to play navigate with 'west', 'north', 'south', or 'east', \n To obtain items, type 'get [item]'. To fight enter 'fight' and chose your weapon wisely! \n Find the treasure to win. Beware of enemies!")
print(current_room.get_info())

while playing is True:
    inhabitant = current_room.get_character()
    room['library'].locked = True

    if inhabitant is not None:
        inhabitant.describe()
        inhabitant.talk()
        print("You must fight or die! Enter 'fight' to begin the battle!")
    else: 
        current_room.get_info()
        current_room.list_items()

    print('-------------------')
    
    # if 'key' in player.get_inventory():
    #     room['treasue'].locked = False

    first, *second = input("Enter command >> ").lower().split(' ')
    try: 
        # if the user enters single command and that command is a direction or q or d 
        if first in ['north', 'south', 'east', 'west', 'd', 'q']:
            # if the command is d then print all possible directions 
            if first == 'd':
                current_room.get_info()
                player.get_inventory()
            # if the 
            elif first == 'q':
                print('Goodbye')
                playing = False
            else:
                current_room = current_room.move(first)


        elif first in ['get', 'take' 'pick']:
            item = second[0]

            if item in current_room.list_items():
                print("** You picked up the " + item + " It's been added to your inventory. ** \n")
                player.get_item(item)
                current_room.set_items([])
            else: 
                print('** That item is not in this room **')
        
        elif first == 'fight':
            if inhabitant is None:
                print('** There are no enemies to fight, not yet. **')
            # player
            print(f'{player.name} vs {inhabitant.name}')
            print('Choose your weapon')
            weapon = input()
            if weapon not in player.get_inventory():
                print('You do not have that! Find items by exploring rooms and type get [item]')
            else:
                victory = inhabitant.fight(weapon)
                if victory is True:
                    current_room.set_character(None)
                else:
                    print("You lost! Try again.")
                    playing=False

        else:
            print('come agein')
    except ValueError: 
        print("That move isn't allowed please choose another direction. ") # Print an error message if the movement isn't allowed.

