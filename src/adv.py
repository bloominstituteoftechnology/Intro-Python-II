from random import random
from utils import find_key

from rooms import rooms
from player import Player

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

dirs = ['n', 's', 'e', 'w']

player = Player('Dom', rooms['outside'], [])


run_count = 0

while True:

    run_count += 1

    room_key = find_key(player.current_room)

    if run_count == 1:
        print("""\n--------------------------------------------------------------------------------------------\n
Welcome to Lambda Quest IV! Will you find the treasure,
or perish along the way like the many adventurers that came before you?\n
--------------------------------------------------------------------------------------------\n""")

    player.print_current_room()
    player.current_room.check_light(player)
    player.look_around()

    #
    # GET PLAYER INPUT
    #

    action = input('What do you want to do?\n').strip().split()

    if 'q' in action:
        exit()

    for i in dirs:
        if i in action:
            chosen_direction = i
            player.move(chosen_direction)

    if ('get' in action or 'take' in action) and len(action) == 2:
        player.take(action)

    if 'drop' in action:
        player.drop(action)
        
    if 'check' in action or 'inventory' in action:
        player.inventory(action)

    if 'attack' in action and len(player.current_room.enemies) > 0:
        # todo
        pass

    if player.current_room.has_unique_action is True:
        player.current_room.run_room_action(room_key, player, action)


    if room_key == 'dark':
        if 'read' in action:
            print(
                "You take your lamp in one hand and squint at the note. You can make out some text\n")
            print(
                "1T'S A TR4P! DON'T G0 THROUGH THE SECRET DOOR IN EAST SIDE OF THE TREASURE ROOM!\n")
            for i in player.current_room.items:
                if i.name == 'note':
                    player.items.append(i)
                    player.current_room.items.remove(i)

    if room_key == 'treasure':
        for i in player.items:
            if i.name == 'note':
                print("""Looking closely at the east side of the room, you can see a faint outline among
the rocks. Brushing the dust away, you see the outline of a dusty, stone-coloured door. In the centre
is a keypad and a screen. You're puzzled by this sudden thematic inconsistency with the fantasy theme 
that this game has so far maintained.""")
        sub_action = input("What do you do?").strip().split()
        if 'enter' in sub_action or 'type' in sub_action:
            if sub_action[1] == '140':
                print("The door swings open!")
                player.current_room = find_key(rooms['final'])
            else:
                print("Nothing happens.")