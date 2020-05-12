from room import Room
from player import Player


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


# Main
name = input('What is your name, adventurer? ')

player = Player(name, room['outside'])

print(f'Welcome, {player.name}! Your current location is: {player.room_info()}')

def gameplay(player):
    direction = input('Which direction would you like to go? (N for north, S for south, E for east, W for west, Q to quit) ')
    direction = direction.lower()

    if direction == 'n':
        location = player.current_room.n_to
        if location != None:
            player = Player(name, location)
            print(player.room_info())
            gameplay(player)
        else:
            print('There is nothing to the north. Please choose a different direction.')
            gameplay(player)
    elif direction == 's':
        location = player.current_room.s_to
        if location != None:
            player = Player(name, location)
            print(player.room_info())
            gameplay(player)
        else:
            print('There is nothing to the north. Please choose a different direction.')
            gameplay(player)
    elif direction == 'e':
        location = player.current_room.e_to
        if location != None:
            player = Player(name, location)
            print(player.room_info())
            gameplay(player)
        else:
            print('There is nothing to the north. Please choose a different direction.')
            gameplay(player)
    elif direction == 'w':
        location = player.current_room.w_to
        if location != None:
            player = Player(name, location)
            print(player.room_info())
            gameplay(player)
        else:
            print('There is nothing to the north. Please choose a different direction.')
            gameplay(player)
    elif direction == 'q':
        print('Farewell, adventurer!')
    else:
        print('FAILURE')

if __name__ == '__main__':
    gameplay(player)
