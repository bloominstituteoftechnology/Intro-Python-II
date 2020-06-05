from room import Room
from player import Adventurer
from item import Item

# Declare all the rooms
room = {
    'outside': Room("Outside the Cave Entrance", """North of you, the cave mount beckons."""),

    'entrance': Room("Ingress", """Dim light filters in from the south. Dusty passages run north and east. There is a cool draft from a large crack in the rock to the west."""),

    'overlook': Room("Thief's Overlook", """A steep cliff appears before you, falling into the darkness. Below to the west, you hear the faint sounds of water, but there is no way across the chasm. """),

    'cavern': Room("Cavern", """You step into a cavernous chamber echoing with the squeaks of thousands of bats. The stench of ammonia and mold engulfs you. You almost fail to notice the narrow, uneven stairs carved into the stone, descending into the dark westward."""),

    'stairs': Room("Stairway", """You carefully decend the wet steps. The smell of damp lime permeates the air. You hope the occasional heavy drips on your cloak are water and not guano."""),

    'grotto': Room("Grotto", """Finally, you reach a grotto on a turquoise lake. Stalagmites grow from the floor and walls, making it impossible to continue on without entering the ominous water..."""),
    
    'lake': Room("Crystal Lake", """The calm, cool water appears to be shallow near the shore. You step into it. From the dephs ahead, a monstrous crab rises..."""),

    'crag': Room("Crag", """The tapering passage winds along the crag from west to north. A low whistle pierces the wind streaming over the cliff cascading into the darkness below the footpath."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been looted by earlier adventurers. Was this really what you came for? The only exit is to the south."""),
}


# Link rooms together
room['outside'].exits['n'] = room['entrance']

room['entrance'].exits['s'] = room['outside']
room['entrance'].exits['n'] = room['cavern']
room['entrance'].exits['e'] = room['crag']
room['entrance'].exits['w'] = room['overlook']

room['overlook'].exits['e'] = room['entrance']

room['cavern'].exits['s'] = room['entrance']
room['cavern'].exits['w'] = room['stairs']

room['stairs'].exits['e'] = room['cavern']
room['stairs'].exits['w'] = room['grotto']

room['grotto'].exits['e'] = room['stairs']
room['grotto'].exits['w'] = room['lake']

room['lake'].exits['e'] = room['grotto']

room['crag'].exits['w'] = room['entrance']
room['crag'].exits['n'] = room['treasure']

room['treasure'].exits['s'] = room['crag']


# Declare all items
items = {
    'lantern': Item("Old Lantern", """A dusty, dented lantern lies on the ground. The glass panels are shattered but it's oil compartment is still full. Not a bad find!"""),
    
    'sword': Item("Thief's Sword", """Leaning against the limestone wall is a rusty short sword. This blade might have seen better days, but it's better than nothing.""" )
}


# place items
room['treasure'].contents[items['lantern']] = 1
room['overlook'].contents[items['sword']] = 1


# Player commands
actions = {'s': 'search',
        'l' : 'loot',
        'i': 'inventory'}
# search room for item
def search(player, item_name):
    if len(item_name) == 0:
        print(player.room)
    else:
        for name in item_name:
            try:
                if items[name] in player.inventory or \
                 items[name] in player.room.contents:
                    print(items[name].full)
            except KeyError:
                print(f'The {name} doesn\'t appear to be visible at the '
                      'moment.')
# player get item
def loot(player, item_name):
    for name in item_name:
        try:
            if items[name] in player.room.contents:
                player.inventory[items[name]] += 1
                player.room.contents[items[name]] -= 1
                if player.room.contents[items[name]] == 0:
                    player.room.contents.pop(items[name])
                    print(f'You have picked up {items[name].description}.')
            else:
                print(f'The {name} doesn\'t seem to be something you can pick up, '
                      'at least not here and now.')
        except KeyError:
            print(f'The {name} doesn\'t seem to be something you can pick up, '
                  'at least not here and now.')
# check player inventory
def inv(player, filter):
    if len(player.inventory) == 0:
        print('You are empty-handed.')
    else:
        print('You are carrying:')
        for item, count in player.inventory.items():
            if ' '.join(filter) in item.description:
                if count == 1:
                    print(item.description)
                else:
                    print(f'{count} of {item.shdescriptionort}')

#
# Main
#

# create player object, starts in the 'outside' room
adventurer = Adventurer(room['outside'])

greeting = """
Greetings Adventurer! You can move around the world using:
\n n -> North \n s -> South \n e -> East \n w -> West
\nTo search the current room for items, use: 
\ns to search \nl to loot
\nCheck your inventory with 'i'
\nYou may end your adventure at anytime with 'q'
"""
print(greeting)
print("Your adventure begins at:")

directions = ['n','s','e','w']
prompt = '> '

action = input(f'{adventurer.room} \n Proceed north and enter the cave? \n{prompt}')

# if the user enters a cardinal direction, attempt to move to the room there
while action != 'q':
    try:
        adventurer.room = adventurer.room.exits[action]
        action = input(f'{adventurer.room}\n\nWhich way would you like to go? \n{prompt}')
    except KeyError:
        action = input(f'Hmm.. It seems like there is no obvious way to do that.\n\n{prompt}') # error message
# quitting the game
while action == 'q':
    print("Farewell...")
    quit()
