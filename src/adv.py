from room import Room
from player import Adventurer
from item import Item

# Declare all the rooms
room = {
    'outside': Room("Outside the Cave Entrance", """North of you, the cave mount beckons.""", lit=True),

    'entrance': Room("Ingress", """Dim light filters in from  cave entrance to the south. Dusty passages run north and east. There is a cool draft from a large crack in the rock to the west.""", lit=True),

    'overlook': Room("Thief's Overlook", """A steep cliff appears before you, falling into the darkness. Below to the west, you hear the faint echoes of water, but there is no way across the chasm.""", 
    dark_description="""It's pitch black, you can't see anything! Below you, you hear the faint echoes of water dripping."""),

    'cavern': Room("Cavern", """You step into a cavernous chamber echoing with the squeaks of thousands of bats roosting overhead. The stench of ammonia and mold engulfs you. You almost fail to notice the narrow, uneven stairs carved into the stone, descending into the dark westward.""",
    dark_description="""Your ears fill with a cacophony of echoing squeaks and screeches. The stench of ammonia burns your nostrils...bats? There is too little light to tell."""),

    'stairs': Room("Stairway", """You carefully decend the wet steps. The smell of damp lime permeates the air. You hope the occasional heavy drips on your cloak are water and not guano.""",
    dark_description="""Its too dark to watch your step properly! Better turn around and find a light."""),

    'grotto': Room("Grotto", """Finally, you reach a grotto on a turquoise lake. Stalagmites grow from the floor and walls, making it impossible to continue on without entering the ominous water...""",
    dark_description="""Its too dark to watch your step properly! Better turn around and find a light."""),
    
    'lake': Room("Crystal Lake", """The calm, cool water appears to be shallow near the shore. You step into it. From the dephs ahead, a monstrous crab rises...""",
    dark_description="""Its too dark to watch your step properly! Better turn around and find a light."""),

    'crag': Room("Crag", """The tapering passage winds along the crag from west to north. A low whistle pierces the wind streaming over the cliff cascading into the darkness below the footpath.""", lit=True),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been looted by earlier adventurers. Was this really what you came for? There must be someting useful in here somwehere... The only exit is to the south.""", lit=True)
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
    'lantern': Item("Old Lantern", """A dusty, dented lantern lies on the ground. The glass panels are shattered but it's oil compartment is still full. Not a bad find!""", light=True),
    
    'sword': Item("Thief's Sword", """Leaning against the limestone wall is a rusty short sword. This blade might have seen better days, but it's better than nothing.""" )
}


# place items
room['treasure'].contents[items['lantern']] = 1
room['overlook'].contents[items['sword']] = 1


# Player commands
actions = {'r': 'search',
        'l' : 'loot',
        'i': 'inventory'}

# search room for item
def search(adventurer, item_name):
    player_has_light = False
    for item in adventurer.inventory.keys():
        player_has_light = player_has_light or item.light
    if len(item_name) == 0:
        print(adventurer.room.__str__(player_has_light))
    else:
        if player_has_light or adventurer.room.illuminated():
            for name in item_names:
                try:
                    if items[name] in adventurer.inventory or \
                        items[name] in adventurer.room.contents:
                        print(items[name].full)
                    else:
                        print(f"That doesn't appear to be visible at the moment.")
                except KeyError:
                    print(f"That doesn't appear to be visible at the moment.")
        else:
            print("It's too dark here for that!")

# player get item
def loot(adventurer, item_name):
    for name in item_name:
        try:
            if items[name] in adventurer.room.contents:
                adventurer.inventory[items[name]] += 1
                adventurer.room.contents[items[name]] -= 1
                if adventurer.room.contents[items[name]] == 0:
                    adventurer.room.contents.pop(items[name])
                    print(f"You have picked up {items[name].description}.")
            else:
                print(f"The {name} doesn't seem to be something you can pick up, at least not here and now.")
        except KeyError:
            print(f"The {name} doesn't seem to be something you can pick up, at least not here and now.")

# check player inventory
def inventory(adventurer, filter):
    if len(adventurer.inventory) == 0:
        print("You are empty-handed.")
    else:
        print("You are carrying: ")
        for item, count in adventurer.inventory.items():
            if ' '.join(filter) in item.description:
                if count == 1:
                    print(item.description)
                else:
                    print(f"{count} of {item.description}")

#
# Main
#

# create player object, starts in the 'outside' room
adventurer = Adventurer(room['outside'])

greeting = """
Greetings Adventurer! You can move around the world using:
\n n -> North \n s -> South \n e -> East \n w -> West
\nTo search the current room for items, use: 
\nr to search \nl to loot
\nCheck your inventory with 'i'
\nYou may end your adventure at anytime with 'q'
"""
print(greeting)
print("Your adventure begins at:")

directions = ['n','s','e','w']
prompt = '> '
action = input(f"{adventurer.room} \n\n {prompt}")

# if the user enters a cardinal direction, attempt to move to the room there
while action != 'q':
        try:
            action = action.lower().split()
            if action[0] in actions:
                action[0] = actions[action[0]]
            elif action[0] == 'go':
                if len(action) == 1:
                    print("Go where?")
                else:
                    action = action[1:]
            try:
                adventurer.room = adventurer.room.exits[action[0]]
                player_has_light = False
                for item in adventurer.inventory.keys():
                    player_has_light = player_has_light or item.light
                print(adventurer.room.__str__(player_has_light))
            except (TypeError, KeyError):
                eval(f'{action[0]}(adventurer, {action[1:]})')
        except NameError:
            print(f"Hmm.. It seems like there is no obvious way to do that")
        except Exception as e:
            print(e)
        finally:
            action = input(f"\n{prompt}")

#    try:
#        adventurer.room = adventurer.room.exits[action]
#        action = input(f'{adventurer.room}\n\nWhich way would you like to go? \n{prompt}')
#    except KeyError:
#        action = input(f'Hmm.. It seems like there is no obvious way to do that.\n\n{prompt}') # error message

# quitting the game
while action == 'q':
    print("Farewell...")
    quit()



# victory condition
adventurer.victory = False
victory_message = """
You stand exhausted, thigh-deep in the pale blue water, and notice a golden glimmer from
the direction the giant crab appeared from. Treasure!
As you turn a gold bullion over in your hand, you catch a glimpse of your own reflection.
You look back at the crab carcass silently splayed across the lakebed.
Not only have you earned the prize, but have scored an excellent dinner.
                    
        ___     ___
     .i .-'   `-. i.
   .'   `/     \'  _`.
   |,-../ o   o \.' `|
(| |   /  _\ /_  \   | |)
 \\\  (_.'.'"`.`._)  ///
  \\`._(..:   :..)_.'//
   \`.__\ .:-:. /__.'/
    `-i-->.___.<--i-'
    .'.-'/.=^=.\`-.`.
   /.'  //     \\  `.\
  ||   ||       ||   ||
  \)   ||       ||  (/
       \)       (/  
"""