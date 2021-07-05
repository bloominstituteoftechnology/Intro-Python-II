from room import Room
from player import Player
from item import Item
# Declare all the rooms

#dictionary
room = {
    #key     :  value
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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

#inventory linking
room['outside'].inventory = [Item("key", """key to treasure box"""), Item("lantern", """a light to guide you""")]
room['foyer'].inventory =  [Item("wand", """just in case you need magic"""),Item("shield", """to protect you"""),]
room['overlook'].inventory = [Item("cape", """because it's cold out here"""),Item("snack", """because low blood sugar"""),]
room['narrow'].inventory = [Item("beer", """who doesn't want beer in narrow passages??"""),Item("diamond", """because shiny"""),]
room['treasure'].inventory = [Item("gold", """it's about time this pays off"""),Item("job offer", """ongoing income is always nice"""),]

'''LEFT TO DO 
- Add two-word commands to the parser
- Add the get and drop commands to the parser
'''
# Main

#done: Make a new player object that is currently in the 'outside' room.
player =  Player(room['outside']) 

# done: Write a loop that:

# * done: Prints the current room name
# * done: Prints the current description (the textwrap module might be useful here).
# * done: Waits for user input and decides what to do.

while True:
    print(player.current_room)
    print(player.current_room.name)
    print(player.current_room.description)
    print(f"Inventory: {player.current_room.inventory}")
    s = input("enter N/S/E/W direction to move OR enter 'take' to take inventory: ").lower()[0] 

    if s == 'q':
        print('see you later')
    elif s == 't':
        for i in player.current_room.inventory:
            i.on_take()
    elif s == 'n'or's'or'e'or'q':
        player.current_room = player.try_move(s)
    else:
        print("oops")



'''Should work n, N, north, North, NORTH <---- for each cardinal direction, 
could use .lower or .upper on input or just take first letter ("/n>").lower()[0]'''

# done:If the user enters a cardinal direction, attempt to move to the room there.
# done: Print an error message if the movement isn't allowed.

# done:If the user enters "q", quit the game.


