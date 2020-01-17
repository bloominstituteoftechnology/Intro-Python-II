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

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

gear = Item("gear", "This is a small silver gear.")
coin = Item("coin", "A small gold piece.")
key1 = Item("key1", "A small key.")
key2 = Item("key2", "A medium key.")
key3 = Item("key3", "A large key.")
lemon = Item("lemon", "A yellow round piece of fruit.")
banana = Item("banana", "a yellow telephone shaped fruit.")
apple = Item("apple", "a small round red fruit.")
orange = Item("orange", "a small round orange fruit.")
lime = Item("lime", "a small green oval shaped fruit.")
coconut = Item("coconut", "A round medium sized item full of juice. ")


room['foyer'].items.append(gear)
room['foyer'].items.append(banana)
room['foyer'].items.append(key2)
room['overlook'].items.append(key1)
room['overlook'].items.append(coconut)
room['overlook'].items.append(lime)
room['narrow'].items.append(coin)
room['narrow'].items.append(key3)
room['narrow'].items.append(apple)
room['narrow'].items.append(orange)
room['treasure'].items.append(coin)
room['treasure'].items.append(coin)
room['treasure'].items.append(coin)
room['treasure'].items.append(key1)
room['treasure'].items.append(key2)
room['treasure'].items.append(key3)
room['treasure'].items.append(gear)
room['treasure'].items.append(gear)
room['outside'].items.append(apple)
room['outside'].items.append(apple)
room['outside'].items.append(orange)
room['outside'].items.append(orange)

player = Player("Nick", room["outside"])

# Main Controller

while True:

    quit = player.input_instructions()

    if quit == True:
        break