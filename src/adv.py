from player import Player
from room import Room
from item import Item
# Declare all the rooms

#
# Main
#
# Make a new player object that is currently in the 'outside' room. n_to
# create obj
# bracket in dict room
# player_room = starter room

item = {
    'teddys': Item('Teddy', 'A childs favorite stuffed animal'),
    'rocket ship': Item('Rocket Ship', 'for the little Nasa that always lived inside of you'),
    'Pug': Item('Pug', 'The dog everyone talks about and always wanted'),
    'Computer desk': Item('Computer Desk', 'I think we all can agree, we want a new one'), 
    'Love': Item('Love', 'we all need more of it in 2020!!!')
}



room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", item['teddys']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", 
                     item['rocket ship']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", 
                     item['Pug']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",  
                    item['Computer desk']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", 
                    item['Love']),
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



player_name = input("Choose your name: ")
player_room = room["outside"]

player = Player(player_name, player_room, [])
print(player)

new_player = Player(player_name, room['outside'])

print(f'Welcome back, {new_player}')



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
    
    
    current_room = player.current_room
    print(
        f'You are located at {current_room.name} that is {current_room.description}')
    print("where to next?")
    enter = input('Enter n, s , e, w and q to quit the game: ')

    if enter == 'q':
        print(f'Thanks for playing, {player_name}. See you again soon!')
    if enter == 'n':
        # The hasattr() method returns true if an object has the given named attribute and false if it does not.
        if hasattr(current_room, 'n_to'):
            print("going North")
            player.current_room = current_room.n_to
            print(current_room.items)
               # Take coin or Take book, take car 
            str = input('If you want to take an item from a room. Please follow this format: verb + subject ex take coin, take dog')
            # slice - coin, car
            str = slice(2)
                # current_room.remove(str)
            # player_item.add(str)
        else:
            print(f'{player_name} enter another location, this area is closed down ')
    elif enter == 's':
        if hasattr(current_room, 's_to'):
            print(f'{player_name} you are going South my friend')
            player.current_room = current_room.s_to
        else:
            print(f'{player_name} enter another location, this area is closed down')
    elif enter == 'e':
        if hasattr(current_room, 'e_to'):
            print(f'{player_name} you are moving East!')
            player.current_room = current_room.e_to
        else:
            print(f'{player_name} enter another location, this area is closed down')
    elif enter == 'w':
        if hasattr(current_room, 'w_to'):
            print(f'{player_name} going out West')
            player.current_room = current_room.w_to
        else:
            print(f'{player_name} enter another location, this area is closed down')
    else:
        print('Please enter a valid location')
        break
