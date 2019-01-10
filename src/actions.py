import os


def move_player(direction, player):
    try:
        if direction == 'n':
            player.room = player.room.n_to
            os.system('cls' if os.name == 'nt' else 'clear')
        elif direction == 'e':
            player.room = player.room.e_to
            os.system('cls' if os.name == 'nt' else 'clear')
        elif direction == 's':
            player.room = player.room.s_to
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            player.room = player.room.w_to
            os.system('cls' if os.name == 'nt' else 'clear')
    except AttributeError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Can't go that way. Try another direction.\n")
