import os


class Quit(Exception):
    pass


def input_command(player):
    user_input = input("Enter command: ").lower()
    command = user_input.split()[0]
    if len(user_input.split()) == 2:
        noun = user_input.split()[1]

    os.system('cls' if os.name == 'nt' else 'clear')
    if command in ('quit', 'q'):
        raise Quit
    elif command in ('n', 'e', 's', 'w', 'north', 'east', 'south', 'west'):
        player.move_player(command[0] + '_to')
        print(player.room)
    elif command in ('search', 'look'):
        print(player.room)
        player.room.search_room()
    elif command.split()[0] in ('take', 'get', 'drop'):
        print(player.room)
        print('take/drop test')
    else:
        return command
