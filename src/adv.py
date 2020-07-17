import random

from room import Room
from player import Player
from item import Item, Treasure, LightSource, Equipment
from utils import clear
from battle import Battle
# Declare all the rooms


item = {
    'sword': Equipment('sword', 'very sharp stuff', 10, 0),
    'shield': Equipment('shield', 'blocks sharp stuff', 0, 10),
    'gold': Treasure('gold', 'shiny stuff', 500),
    'candle': LightSource('candle', 'illuminates dark areas')
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", item, encounter_chance=7),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", dark=True),

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

# Start player at room 'Outside Cave Entrance'

me = Player(room['outside'],50, 10, 5)
# print(me.base_attack, me.base_defense, me.base_hp)
random_battle = random.randint(0, 10) <= me.location.encounter_chance

mode = "explore"

prev_obj = ""

while mode == "explore":
    isDark = me.location.dark and not me.hasLightSource()
    if isDark:
        print(f"-------------------\nIt's too dark to see!\n\
Items cannot be seen")
    else:
        print(f"-------------------\nPlayer's current location: {me.location.name}")
        print(me.location.list_items(),"\n")
    player_input = input("Where shall you go next? (n, s, w, e)\n\
verbs - go, take, drop\n\
menu options - q - quit, d -location's description, i - inventory\n")

    clear()

    verb, obj = "", ""

    try:
        verb, obj = player_input.split(" ")
        if obj == "it" and prev_obj:
            obj = prev_obj
    except:
        verb = player_input

    if verb == "q": mode = False

    elif verb == 'd': 
        if isDark: print("It's pitch black!")
        else: print(f"location's description: {me.location.desc}")

    elif verb == 'i': print(me.list_items())
        
    elif verb == 'take': me.loot(obj)
        
    elif verb =='drop': me.drop_item(obj)
        
    elif verb == 'go': me.move(obj)
        
    else: print("Invalid input, try again")

    prev_obj = obj

while mode == "battle":
    active_monsters = me.location.monsters
    print(f"Monsters encountered! Get ready for combat.\n-------------------")
    battle_room = Battle(me, active_monsters)
    while len(active_monsters) > 0:
        player_input = input(f"Select your attack")


