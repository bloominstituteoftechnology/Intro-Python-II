from actions import move_player


class Quit(Exception):
    pass


def input_command(player):
    command = input("Enter command: ").lower()
    if command in ('quit', 'q'):
        raise Quit
    elif command in ('n', 'e', 's', 'w'):
        move_player(command, player)
    else:
        return command
