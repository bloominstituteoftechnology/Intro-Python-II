from player import Player
from room import Room
import sys


class GameController:
    def __init__(self, commandOptions: [str] = []):
        self.commandOptions = ['n', 'north', 's', 'south', 'e', 'east', 'w', 'west', 'l', 'light']

    def enterRoom(self, player: Player):
        current_room = player.current_room
        if current_room.name == 'outside':
            current_room.isLit = False
        if player.light_source_on:
            current_room.isLit = player.light_source_on

    def roomOperation(self, player: Player, command: str):
        room = player.current_room

        if command == 'q' or command == 'quit':
            sys.exit(1)
        elif command in self.commandOptions:
            if not room.isLit:
                return print(f'It is pitch black in here.\nI better turn some lights on, or I will be lost forever.\n...and that is not a cute end to this story.')
            else:
                self.checkPath(player, command)
                return
        else:
            return print('What are you trying to do?  Maybe you should sit down and think for a minute.')

    def checkPath(self, player: Player, command: str):
        room = player.current_room
        wrongWayText = f'Are you ok?\nYou are not an astral projection!\nStop trying to go through walls!'

        if command == 'n' or command == 'north':
            if room.n_to == None:
                return print(wrongWayText)
            else:
                player.current_room = room.n_to
                return print('\nYou move north.')
        if command == 's' or command == 'south':
            if room.s_to == None:
                return print(wrongWayText)
            else:
                player.current_room = room.s_to
                return print('\nYou move south.')
        if command == 'e' or command == 'east':
            if room.e_to == None:
                return print(wrongWayText)
            else:
                player.current_room = room.e_to
                return print('\nYou move east.')
        if command == 'w' or command == 'west':
            if room.w_to == None:
                return print(wrongWayText)
            else:
                player.current_room = room.w_to
                return print('\nYou move west.')
