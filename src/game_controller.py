from player import Player
from room import Room
import sys


class GameController:
    def __init__(self, commandOptions: [str] = []):
        self.commandOptions = ['n', 'north', 's', 'south', 'e', 'east', 'w', 'west', 'l', 'light']

    def roomOperation(self, room: Room, player: Player, command: str):
        if command == 'q' or command == 'quit':
            print('entered q check')
            sys.exit(1)
        elif command in self.commandOptions:
            print('inside elif')
            if not room.isLit:
                return print(f'It is pitch black in here.\nI better turn some lights on, or I will be lost forever.\n...and that is not a cute end to this story.')


            return print(f'command in the list')
        else:
            return print('What are you trying to do?  Maybe you should sit down and think for a minute.')