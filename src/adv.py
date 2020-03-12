from room import Room
from maps import build_rooms, link_rooms, stock_rooms, populate_rooms
from item import Item
from player import Player
from monster import Monster

# Build map:
map_name = 'default'
room = build_rooms()
link_rooms(room)
stock_rooms(room)
populate_rooms(room)


# player = Player(input('What is your name?\n'), 'outside')
player = Player('Debugger Steve', room['outside']) # Speed up tests!

item_cmds = ['get','take','drop','leave','throw','swing','eat','drink']
cardinals = ['n','e','w','s','north', 'east','west','south']
room_cmds = ['search']

cmd = ''
print(f'Welcome {player.name}!\nGood luck on your adventure!\n')
while cmd != 'q':
    print('\n', player.current_room.description, '\n')
    print('Current Inventory:', player.inventory)
    print('Room Contents', player.current_room.contents)
    cmd = input("What do you do?\n").lower()
    split_cmd = cmd.split()
    if cmd in cardinals:
        try:
            player.change_room(cmd)
        except AttributeError: 
            print('You cant go that way!\n')
    elif split_cmd[0] in item_cmds:
        try:
            player.item_interaction(split_cmd[0],split_cmd[-1])
        except AttributeError:
            print('Can\'t use item in that way')
    elif split_cmd[0] in room_cmds:
        try:
            player.room_interaction(split_cmd[0])
        except AttributeError:
            print('Nothing in the room to do that with!')    
    else:
        print('not recognized')
        print('That\'s not possible!')  
print('Thanks for playing!')
