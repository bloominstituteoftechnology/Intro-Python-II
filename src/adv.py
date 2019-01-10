import textwrap

from player import Player
from room import Room


def wonderland():

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

    room['outside'].n_to = room['foyer']
    room['foyer'].s_to = room['outside'] 
    room['foyer'].n_to = room['overlook']
    room['foyer'].e_to = room['narrow']
    room['overlook'].s_to = room['foyer']
    room['narrow'].w_to = room['foyer']
    room['narrow'].n_to = room['treasure']
    room['treasure'].s_to = room['narrow']

    intro ='Out of the corner of your eye, you see a White Rabbit with a pocketwatch. You start following the White Rabbit and suddenly start falling down and down and down ... You open your eyes and are surrounded in darkness. Slowly your eyes adjust and you see a faint light. You start walking in that direction.\n'

    
    # * Intro
    # Make a new player object that is currently in the 'outside' room.

    print('\nWELCOME TO WONDERLAND!\n')
    next_victim = input('By order of the Queen, you are required to enter\nyour name to enter this realm.\n')

    print(textwrap.fill(intro, width=50))
    
    player = Player(next_victim or 'Alice', 'outside')
    print(player)
    here = '{}'.format(room[player.get_room()])
    print(textwrap.fill(here, width=50))

    # * Write a loop that:
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.


    which_way = '\nWhich direction would you like to go?\n[n] North   [e] East   [s] South   [w] West   [o] Outside   [q] Quit\n'

    nsew = input(which_way).lower()[0]
    
    


# * If the user enters a cardinal direction, attempt to move to the room there.
# * Print an error message if the movement isn't allowed.
# * If the user enters "q", quit the game.

    while not nsew == 'q':

        if nsew == 'o':
            print(room['outside'])
            player.return_outside()

        if nsew in list('news'):

        # print('you are not lost!')

            if nsew == 'n':
                try:
                    room[player.get_room()].n_to
                except:
                    print('Choose another direction')
                    nsew = input(which_way).lower()[0]
                else:
                    x = [k for k, v in room.items() if v == room[player.get_room()].n_to]
 
            elif nsew == 'e':
                try:
                    room[player.get_room()].e_to
                except:
                    print('Choose another direction')
                else:
                    x = [k for k, v in room.items() if v == room[player.get_room()].e_to]

            elif nsew == 'w':
                try:
                    room[player.get_room()].w_to
                except:
                    print('Choose another direction')
                else:
                    x = [k for k, v in room.items() if v == room[player.get_room()].w_to]
            elif nsew == 's':
                try:
                    room[player.get_room()].s_to
                except:
                    print('Choose another direction')
                else:
                    x = [k for k, v in room.items() if v == room[player.get_room()].s_to]
            else:
                print('YOU ARE LOST!!!!')

            player.set_room(x[0])
            print(' ')
            print(room[(player.get_room())])

            nsew = input(which_way).lower()[0]

if __name__ == '__main__':
  wonderland()

#   print("Guess the number!")

#   secret_number = random.randrange(101)

#   while True:
#     guess = input("Input your guess: ")
    
#     try:
#       guess = int(guess)
#     except ValueError:
#       print("Please enter an integer.")
#       continue

#     print(f"You guessed: {guess}")

#     if guess == secret_number:
#       print("You win!")
#       break
#     elif guess < secret_number:
#       print("Too small!")
#     else:
#       print("Too big!")

# if __name__ == '__main__':
#   guessing_game()