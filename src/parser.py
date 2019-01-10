from actions import move_player


class Quit(Exception):
    pass


def input_command(player):
    command = input("Enter command: ").lower()
    if command in ('quit', 'q'):
        raise Quit
    elif command in ('n', 'e', 's', 'w', 'north', 'east', 'south', 'west'):
        move_player(command[0] + '_to', player)
    else:
        return command
