import os


def move_player(attribute, player):
    if hasattr(player.room, attribute):
        player.room = getattr(player.room, attribute)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Can't go that way. Try another direction.\n")
