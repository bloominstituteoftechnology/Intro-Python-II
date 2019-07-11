from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
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


items={
    "gold1" : Item("gold", "1000 gold"),
    "bag1" : Item("bag","bag")
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

#Add items to room

room['treasure'].add_item(items["gold1"])
room['outside'].add_item(items["bag1"])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player("player1",room["outside"])
print(player1)
player1.current_room.show_item()

def move(player, direction):
    if direction=='n':
        target = player1.current_room.n_to
    elif direction=='s':
        target = player1.current_room.s_to
    elif direction=='w':
        target = player1.current_room.w_to
    elif direction=='e':
        target = player1.current_room.e_to

    if target==None:
        print ("There is no room")
    else:
        player.current_room=target
    print(player)

valid_move =['n','s','w','e']

def search_item(name):
    l = []
    for (key, value ) in items.items():
        if value.name==name:
            l.append(items[key])
    #l = [i for (key,value) in items if i.value.name==name]
    return l

def get_item_function(name):
    l = search_item(name) #get the item list by name
    found = False
    for i in l :          #check if any of the item in the current room
        if i in player1.current_room.item_list:
            found = True
            break
    if found==False:
        print(f"{name} does not exist in this room")
    else:
        player1.get_item(i)
        player1.current_room.remove_item(i)


def drop_item_function(name):
    l = search_item(name) #get the item list by name
    found = False
    for i in l :          #check if any of the item in the current room
        if i in player1.inventory:
            found = True
            break
    if found==False:
        print(f"{player1.name} does not have {name}")
    else:
        player1.drop_item(i)
        player1.current_room.add_item(i)


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


while True:
    cmd = input("Input a direction [n,s,e,w] or [q] to quit: ")
    sentence = cmd.split()

    if len(sentence)==1:
        if cmd=='q':
            break
        elif cmd=="i":
            player1.show_item()
        if cmd in valid_move:
            move(player1,cmd)
        #player1.current_room.show_item()


    elif len(sentence)==2:
        if sentence[0]== "get":
            get_item_function(sentence[1])
        if sentence[0]== "drop":
            drop_item_function(sentence[1])
    #    player1.action(sentence[0], sentence[1])

    player1.current_room.show_item()
