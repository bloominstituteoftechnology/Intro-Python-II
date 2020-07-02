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

item = {
    'stick': Item('stick', 'It\'s sharp at both ends.')
}
# stick = Item('stick', 'It\'s sharp at both ends.')

# Make a new player object that is currently in the 'outside' room.
p = Player(room['outside'])

p.get_stuff(item['stick'])

print('Welcome to life. Please make a decision.')

valid_directions = ('n', 's', 'e', 'w')

def parse(s):
    l = s.split()
    if len(l) == 2:
        try:
            print(l)
            print(f'p.{l[0]}_stuff(item[\'{l[1]}\'])')
            
            print(a)
            print('got past 1')
            p.a(item[l[1]])
            print('got past 2')
        except:
            print('huh?')
    else: 
        print('That don\'t make no sense.')


# Game Play Loop
while True:
    print(p.current_room.name)
    print(p.current_room.description)
    print('What will you do?')
    user = input("[n] North  [s] South  [e] East  [w] West  [i] Inventory [q] Quit\n")
    if user == 'q':
        print('Goodbye')
        exit(0)
    elif user in valid_directions:
        p.move(user)
    elif user == 'i':
        print('You have: ')
        for obj in p.stuff:
            print(getattr(obj, 'name'))
        action = input('Enter verb noun: \n')
        parse(action)
    else:
        print("You must be confused by the limitations of this world. Try to find your way again.")
        # user = input("[n] North  [s] South  [e] East  [w] West  [i] Inventory [q] Quit\n")
