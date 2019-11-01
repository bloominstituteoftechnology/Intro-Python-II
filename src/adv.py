"""
A classic-style text-based adventure game!
"""
from player import Player
from mapping import rooms


class Parser:
    """Parse user input into game commands.

    """

    def __init__(self) -> None:
        self.actions = ['move', 'look', 'get', 'drop', 'use', 'inventory', 'quit']
        self.directions = ['n', 's', 'e', 'w']

    def print_actions(self) -> None:
        """Print actions available to user."""
        print(f'Available actions: {self.actions} \n')

    def parse(self, player: Player, commands: str) -> None:
        """Parse user input and call corresponding player method.

        :var player: Player instance
        :var commands: str - user input
        """
        print(f"\nOkay, I'll try to {commands} \n")
        command = commands.split()

        if command[0] in self.actions:
            eval(f'player.{command[0]}({command[1:]})')
        else:
            print(f'Unknown action: {command[0]}')
            self.print_actions()
            player.print_position()


class Game:
    """Wraps player instantiation method and command parser method.

    """

    def __init__(self):
        self.player = None
        self.parser = Parser()

    def set_player(self, name: str = None, **kwargs) -> Player:
        """Validate user input and set instantiate Player with input.

        :var name: name of Player used for setting up players manually
        """
        if not name:
            while True:
                try:
                    name = input('\nWhat is your name? \n:')
                    if not name == "":
                        break
                    else:
                        print("I didn't catch that. \n")
                        continue
                except ValueError:
                    print("I didn't understand that. \n")
                    continue
        player = Player(name, **kwargs)
        if not self.player:
            self.player = player
        return player

    def get_player_input(self) -> None:
        """Validate user input and feed to parser."""
        parser = Parser()
        while True:
            try:
                command = input('What should I do? \n:')
            except ValueError as e:
                print("I didn't understand that. \n")
                print(e)
                continue
            else:
                if command.lower().startswith('q'):
                    break
                if command == "":
                    parser.print_actions()
                    continue
            parser.parse(self.player, command)
        print('Thanks for playing!')


def main(rooms: dict) -> None:
    """Instantiates game, sets up current room, starts game.

    :var rooms: dict mapping of game rooms
    """
    game = Game()

    game.set_player()
    game.player.current_room = rooms['rest_stop']
    rooms['rest_stop'].characters[game.player.name] = game.player

    bear = game.set_player('The Bear', attackpts=20)
    bear.current_room = rooms['trail_east']
    rooms['trail_east'].characters[bear.name] = bear
    print(f"\nThe Adventure Begins! \nGood luck {game.player.name}!!")

    doggo = game.set_player('doggo')
    rooms['doggo'].characters[doggo.name] = doggo

    game.player.print_position()
    game.parser.print_actions()
    game.get_player_input()


if __name__ == '__main__':
    main(rooms)
