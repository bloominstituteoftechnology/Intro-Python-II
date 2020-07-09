
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

#
# Main
#
#
# items = Item('Sword', 'a killing machine')
# newcod = [
# (1, 'new', 'cody'),
# (2, 'neww', 'dalton')
# ]
#
# print(newcod[1])

items = [
    Item(1, 'Sword', 'a killing machine'),
    Item(2, 'Knife', 'a slaying machine'),
    Item(3, 'Pistol', 'Sig Sauer P320'),
    Item(4, 'Revolver', 'Limb Ripping Handgun'),
    Item(5, 'Rifle', '.338 Lapua Magnum - Sniper'),
    Item(6, 'Shotgun', 'Benelli 12 Gauage Pump')
]




print('Available weapons: ')
print(*items, sep = '\n')



# print(items.print_items())


# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])



while True:


    print(f'\nThe room that you are currently in is....{player.room.name}\n')
    print(f'Heres a hint...{player.room.description}\n')


    pickup = input('What weapon? ')

    chosen_weapon = items[int(pickup)-1]
    player.add_weapon(chosen_weapon)

    print(player.currentinv())

    


    selection = input('Please select a direction in which to go: select "n" for North, "e" for East, "s" for South, "w" for West. ')


    if selection == 'q':
        print('\nSee you next time!\n')
        break

    try:
        if selection == 'n':
            player.room = player.room.n_to

    except:
        print("you can't go that way")

    try:
        if selection == 'e':
            player.room = player.room.e_to

    except:
        print("you can't go that way")

    try:
        if selection == 's':
            player.room = player.room.s_to

    except:
        print("you can't go that way")

    try:
        if selection == 'w':
            player.room = player.room.w_to
    except:
        print("you can't go that way")












#end
