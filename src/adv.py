

from room import Room
from player import Player
from item import Item
from utils import clear
# Declare all the rooms


item = {
    'sword': Item('sword', 'very sharp stuff'),
    'shield': Item('shield', 'blocks sharp stuff')
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", item),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

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

me = Player(room['outside'])

running = True

while running:
    print(f"-------------------\nPlayer's current location: {me.location.name}")
    print(f"Items in the room: {me.location.list_items()}.")
    player_input = input("Where shall you go next? (n, s, w, e)\n\
verbs - go, take, drop\n\
menu options - q - quit, d -location's description\n")

    clear()

    verb, obj = "", ""

    try:
        verb, obj = player_input.split(" ")
    except:
        verb = player_input

    if verb == "q": running = False

    elif verb == 'd': print(f"location's description: {me.location.desc}")
        
    elif verb == 'take': me.loot(obj)
        
    elif verb =='drop': me.drop_item(obj)
        
    elif verb == 'go': me.move(obj)
        
    else: print("Invalid input, try again")
        

