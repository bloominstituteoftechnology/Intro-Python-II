from room import Room
from maps import build_rooms, link_rooms
from item import Item
from player import Player
from monster import Monster
import gameplay


map_name='default'
room = build_rooms()
link_rooms(room)

# player = Player(input('What is your name?\n'), 'outside')
player = Player('Debugger Steve', room['outside']) # Speed up tests!

cardinals = ('n','e','w','s',)
cmd = ''

print(f'Welcome {player.name}!\nGood luck on your adventure!\n')
gameplay.print_surroundings(player)

while cmd != 'q':
    cmd = input("What do you do?\n~~>").lower()
    if cmd in cardinals:
        player.change_room(cmd)
    else: gameplay.process_cmd(player, cmd)

print('Thanks for playing!')
