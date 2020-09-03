from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

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


'''
looks like from "outisde", if you go north direction
you go to the "foyer" room ok cool.
'''

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
#lay

# Make a new player object that is currently in the 'outside' room.


'''currently player has just self, and room as arg:
changing it to add name
'''





# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).


# * Waits for user input and decides what to do.

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

print("What's your name?")
player_name = input("~ ")
player = Player(player_name, room['outside'])
print(f"\nHi, {player.name}. It's up to you to find the GOLD!\nRight now, you're at the {player.room.name}.\n{player.room.desc}")


while True:
    print(f"Where to, {player.name}? (n, s, e, w to move - q to quit)")
    move = input("~ ")

    if move == 'n':
        if player.room.n_to is not None:
            player.room = player.room.n_to
            print(f"\nOkay, {player.name}. You're now at the {player.room.name}.\n{player.room.desc}")

        else:
            print(f"\nSorry {player.name}, can't go north. Unfortunately you're still at the {player.room.name}.")


    if move == 's':
        if player.room.s_to is not None:
            player.room = player.room.s_to
            print(f"\nOkay, {player.name}. You're now at the {player.room.name}.\n{player.room.desc}")

        else:
            print(f"\nSorry {player.name}, can't go south. Unfortunately you're still at the {player.room.name}.")


    if move == 'e':
        if player.room.e_to is not None:
            player.room = player.room.e_to
            print(f"\nOkay, {player.name}. You're now at the {player.room.name}.\n{player.room.desc}")

        else:
            print(f"\nSorry {player.name}, can't go east. Unfortunately you're still at the {player.room.name}.")


    if move == 'w':
        if player.room.w_to is not None:
            player.room = player.room.w_to
            print(f"\nOkay, {player.name}. You're now at the {player.room.name}.\n{player.room.desc}")

        else:
            print(f"\nSorry {player.name}, can't go west. Unfortunately you're still at the {player.room.name}.")

    
    if move == 'q':
        print(f"GGs {player.name}. Thanks for playing")
        exit()


#
# If the user enters "q", quit the game.


'''
python src/adv.py
'''