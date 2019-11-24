from room import Room
from player import Player
from constants import Constants
from item import Item
from item import Weapon
from item import Shield
from item import Armor
from item import HealthPotion
# DECLARATIONS

# ITEMS
items = {
    'health_potion': HealthPotion('Greater Health Potion', 'Consumption of this potion will increase player hp by 60hp',60),

    'sword': Weapon('Elven Blade', 'Power eminates from this weapon. Equipping this weapon will increase your attack power by 20', 20),

    'shield': Shield('Elven Steel Shield', 'The shield is covered in scrapes and is dented from battle. Equpping it will increase your defense by 20', 20),

    'helm': Armor('Elven Helmet', 'This helmet has been through many battles. Equipping it will increase defense by 5', 5, 'helm'),

    'chest': Armor('Elven Chest Plate', 'The battle worn steel should still provide protection from direct attacks. Equipping this will increase your defense by 12', 12, 'chest'),

    'gloves': Armor('Elven Gloves', 'The leather is worn but should still provide good protection. Equipping these gloves will increase your defense by 3', 3, 'gloves'),

    'pant': Armor('Elven Leg-Guards', 'These should save me from losing a leg. Equipping these will increase your defense by 10', 10, 'pant'),

    'boots': Armor('Elven Combat Boots', 'You can tell the boots have been worn many times. Equipping these should increase your defense by 3', 3, 'boot')
}

# ROOMS
room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons \n"),

    'foyer': Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.", [ items['health_potion'], items['sword'] ], 'As you look around, you notice a glimmer in a dark corner. Upon approaching the corner you see that there are items hidden there! \n'),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", [ items['chest'], items['gloves'] ], 'In the center of the room you notice a corpse. As you search the corpse you find some items! \n'),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air.", [ items['pant'], items['boots'] ], 'As you walk through the passage you knock over a large pot. In it you discover some items! \n'),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.", [ items['shield'], items['health_potion'] ], 'Disappointed that the room is empty, you begin to search around the room anyway, hoping the previous Adventurers missed something. You notice an odd looking stone on a wall near you. Pressing it reveals a secret safe containing some items! \n'),
}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# PLAYER INTRO
print(Constants['intro'])
print(Constants['stranger_intro'])

name = input(Constants['name_prompt'])
current_player = Player(name, room['outside'])

print(f'\n Artemis: Hello {name}, before you awaits a great adventure. \n Beyond this door peril awaits you. \n Should you survive and find the secret room you will be greatly rewarded. \n Failure will only be met with death. Good luck {name}, may the gods be with you \n \n')

print(f'You look around and see that you are in the {current_player.current_room.name} \n')
print(current_player.current_room)
print('\n')

def is_cardinal(d):
    if d == 'n' or d == 'e' or d == 's' or d == 'w':
        return True
    else:
        return False

status = True

while status:
    direction = input(Constants['direction_prompt'])

    try:
        if direction == 'q':
            print(Constants['user_quit'])
            status = False

        if is_cardinal(direction):
            current = f'{direction}_to'

            if current_player.current_room.__dict__[current] == None:
                print(Constants['obstacle'])
            else:
                current_player.current_room = current_player.current_room.__dict__[current]
                print(f'\n You walked {direction} through a door and enter a new room... \n')
                print(current_player.current_room)
                print('\n')

                if len(current_player.current_room.items) > 0:
                    look = input(Constants['look_around'])
                    if look == 'y':
                        current_player.current_room.look_around_room()
                        current_player.current_room.prnt_items()
                        equip = input(Constants['pick_up_prompt'])

                        if equip == 'y':
                            for item in current_player.current_room.items:
                                if item.name == 'Greater Health Potion':
                                    current_player.add_to_inventory(item)
                                else:
                                    current_player.equip_armor_slot(item, item.slot)
                                current_player.current_room.player_took_items()
                        else:
                            print(Constants['dont_pickup'])
                    else:
                        print(Constants['dont_inspect'])
    except ValueError:
        print('I do not recognize this input \n')

