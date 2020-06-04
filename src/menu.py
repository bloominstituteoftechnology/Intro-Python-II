import cmd
import textwrap
import sys
import os
import time
import random

from player import Player
from enemies import *

myPlayer = Player()

##### Title Screen #####
def title_screen_options():
    option = input("> ")
    main_screen()

##### Main Screen #####
def main_screen_options():
    option = int(input("> "))
    if option == 1:
        # print('Starting game!')
        setup_game()
    elif option == 2:
        # print('Help menu...')
        help_menu()
    elif option == 3:
        # print('Encyclopedia menu...')
        encyclopedia_menu()
    elif option == 9:
        sys.exit()
    while option not in [1, 2, 3, 9]:
        print("Please enter a valid option.")
        option = input("> ")
        if option == 1:
            setup_game()
        elif option == 2:
            help_menu()
        elif option == 3:
            encyclopedia_menu()
        elif option == 9:
            sys.exit()
            
def sub_screen_options():
    option = int(input("> "))
    if option == 1:
            main_screen()
    while option not in [1]:
        print("Please enter a valid option.")
        option = int(input("> "))
        if option == 1:
            main_screen()

##### SIZE = 25
##### HEADERS #####
def main_title():
    print('{:^103}'.format('████████╗██╗░░██╗███████╗  ██████╗░░█████╗░██╗░░░░░███████╗  ░█████╗░░█████╗░██╗░░░██╗██████╗░████████╗'))
    print('{:^103}'.format('╚══██╔══╝██║░░██║██╔════╝  ██╔══██╗██╔══██╗██║░░░░░██╔════╝  ██╔══██╗██╔══██╗██║░░░██║██╔══██╗╚══██╔══╝'))
    print('{:^103}'.format('░░░██║░░░███████║█████╗░░  ██████╔╝███████║██║░░░░░█████╗░░  ██║░░╚═╝██║░░██║██║░░░██║██████╔╝░░░██║░░░'))
    print('{:^103}'.format('░░░██║░░░██╔══██║██╔══╝░░  ██╔═══╝░██╔══██║██║░░░░░██╔══╝░░  ██║░░██╗██║░░██║██║░░░██║██╔══██╗░░░██║░░░'))
    print('{:^103}'.format('░░░██║░░░██║░░██║███████╗  ██║░░░░░██║░░██║███████╗███████╗  ╚█████╔╝╚█████╔╝╚██████╔╝██║░░██║░░░██║░░░'))
    print('{:^103}'.format('░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝  ░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░'))

def version_title():
    print('{:=^103}'.format(''))
    print('{:^103}'.format('The Pale Court 0.0.2'))
    
def sub_title_encyclopedia():
    print('\n')
    print('{:=^103}'.format('=====/(----------)\====='))
    print('{:^103}'.format('<[  ENCYCLOPEDIA  ]>'))
    print('{:=^103}'.format('=====\(----------)/====='))
    
def sub_title_help():
    print('\n')
    print('{:=^103}'.format('=====/(------------)\====='))
    print('{:^103}'.format('<[  INSTRUCTIONS  ]>'))
    print('{:=^103}'.format('=====\(------------)/====='))


##### MAIN MENU #####
def title_screen(): # Title
    os.system('cls' if os.name == 'nt' else 'clear')
    main_title()
    # print('\n')
    version_title()
    print('\n'*3)
    print('{:^103}'.format('The halls of your lineage, once familiar, now foreign whisper of heresy.'))
    print('\n'*7)
    print('{:^103}'.format('[ enter any key to continue ]'))
    print('\n'*6)
    
    title_screen_options() # Title screen input
    

def main_screen(): # Main menu
    os.system('cls' if os.name == 'nt' else 'clear')
    main_title()
    # print('\n')
    version_title()
    print('\n'*4)
    print('                                         [1]     - Play -                                               ')
    print('\n')
    print('                                         [2]     - How to Play -                                        ')
    print('\n')
    print('                                         [3]     - Encyclopedia -                                       ')
    print('\n')
    print('                                         [9]     - Quit -                                               ')
    print('\n'*5)

    main_screen_options() # Main menu input


def help_menu(): # Instructions page
    os.system('cls' if os.name == 'nt' else 'clear')
    sub_title_help()
    print('\n'*2)
    print('{:^103}'.format('Instructions lies here.'))
    print('\n'*16)
    print('[1] Back')
    print('\n')
    sub_screen_options()
    
    
def encyclopedia_menu(): # Encyclopedia page
    os.system('cls' if os.name == 'nt' else 'clear')
    sub_title_encyclopedia()
    print('\n'*2)
    print('{:^103}'.format('Here lies the world.'))
    print('\n'*16)
    print('[1] Back')
    print('\n')
    sub_screen_options()

import cmd
import textwrap
import sys
import os
import time
import random

##### MASTER FUNCTIONS #####
def print_pause(line, name=None, pause=0.02, postpause=1):
    if name is not None and line != 1: #> Name AND many lines
        print(f'[{name}]')
        for block in line:
            wrapper = textwrap.fill(block, initial_indent='    ', subsequent_indent='    ')    
            for char in wrapper:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(pause)
            time.sleep(postpause)
            print('\n')
    elif name is not None and line == 1: #> Name AND one line
        print(f'[{name}]')
        wrapper = textwrap.fill(line)    
        for char in wrapper:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(pause)
        time.sleep(postpause)
        print('\n')
    elif name is None and line != 1: # No nome AND many line
            print("")
            wrapper = textwrap.fill(line)  
            for char in wrapper:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(pause)
            time.sleep(postpause)
            print('\n')
    # elif name is not None and line == 1: # No nome AND one line
    #     wrapper = textwrap.fill(line)    
    #     for char in wrapper:
    #         sys.stdout.write(char)
    #         sys.stdout.flush()
    #         time.sleep(pause)
    #     time.sleep(postpause)
    #     print('\n')


def prompt_list(option):
    num = 1
    n = 0
    while num <= len(option):
        print(f'[{num}] {option[n]}')
        num += 1
        n += 1
        

speechDict = {
    'generalHelp' : {
        'archetype01': """You rumage through oddities and relics of the past. You make out a weapon through the pile...""",
        'archetype02': """After closer inspection, you find an ornate shortsword.""",
        'archetype03': """After closer inspection, you find a yew bow with a sack of wooden arrows."""
    },
    'answersGlobal': {
        'answer01': """Fair choice."""
    },
    'strangerIntro': {
        'question01': """It's been a while since I've greeted wayfarers.""",
        'question02': """Most end up here by curiosity, interest, or obssesion.""",
        'question03': """... you don't seem lost.""",
        'question04': """What brings you to our venerable house stranger?"""
    },
    'strangerArchetype': {
        'question01': """Search the locker behind the desk. You'll find forgotten artifacts from the very forges and bellows that once spured this damned estate to life.""",
        'answer01': """A strong arm, and sharp sword, anything to anchor purpose.""",
        'answer02': """A keen eye, and a strong bow, anything to anchor purpose."""
    },
}








##### MAP #####
"""
# a1 a2 ... # PLAYER STARTS AT D4
# [] [] [] [] a4
# [] [] [] [] b4
# [] [] [] [] ...
# [] [] [] []
"""

zone_map = {
    'outside': {
        'NAME': "Outside Cave Entrance",
        'DESCRIPTION': """North of you, the cave mount beckons.""",
        'INSPECT': "",
        'NORTH': 'foyer',
        'SOUTH': '',
        'EAST': '',
        'WEST': '',
        'STATUS': ['empty', 'explored']
    }, 
    'foyer': {
        'NAME': "Foyer",
        'DESCRIPTION': """Dim light filters in from the south. Dusty
        passages run north and east.""",
        'INSPECT': "",
        'NORTH': 'overlook',
        'SOUTH': 'outside',
        'EAST': 'narrow',
        'WEST': '',
        'STATUS': ['empty', 'explored']
    },
    'overlook': {
        'NAME': "Grand Overlook",
        'DESCRIPTION': """A steep cliff appears before you, falling
        into the darkness. Ahead to the north, a light flickers in
        the distance, but there is no way across the chasm.""",
        'INSPECT': "",
        'NORTH': '',
        'SOUTH': 'foyer',
        'EAST': '',
        'WEST': '',
        'STATUS': ['empty', 'explored']
    },
    'narrow': {
        'NAME': "Narrow Passage",
        'DESCRIPTION': """The narrow passage bends here from west
        to north. The smell of gold permeates the air.""",
        'INSPECT': "",
        'NORTH': 'treasure',
        'SOUTH': '',
        'EAST': '',
        'WEST': 'foyer',
        'STATUS': ['empty', 'explored']
    },
    'treasure': {
        'NAME': "Treasure Chamber",
        'DESCRIPTION': """You've found the long-lost treasure
        chamber! Sadly, it has already been completely emptied by
        earlier adventurers. The only exit is to the south.""",
        'INSPECT': "",
        'NORTH': '',
        'SOUTH': 'narrow',
        'EAST': '',
        'WEST': '',
        'STATUS': ['empty', 'explored']
    }
}

##### GATE INTERACTION #####
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location + ' #')
    print('# ' + zone_map[myPlayer.location][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    
def prompt():
    print("\n" + "========================")
    print("<What would you like to do?>")
    action = input("> ")
    possible_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'look']
    while action.lower() not in possible_actions:
        print("Unkknown action, try again.\n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'look']:
        player_examine(action.lower())
        
def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask.lower())
    if dest in ['up', 'north']:
        destination = zone_map[myPlayer.location][NORTH]
        movement_handler()
    elif dest in ['down', 'south']:
        destination = zone_map[myPlayer.location][SOUTH]
        movement_handler()
    elif dest in ['right', 'east']:
        destination = zone_map[myPlayer.location][EAST]
        movement_handler()
    elif dest in ['down', 'west']:
        destination = zone_map[myPlayer.location][WEST]
        movement_handler()

def movement_handler(destination):
    print("\n" + "You moved to the " + destination + ".")
    myPlayer.location = destination
    print_location
    
def player_examine(action):
    if zone_map[myPlayer.location][STATUS] == 'explored':
        print("You have already explored this zone.")
    






##### GATE INTERACTION #####
def start_game():
    return


    
def main_game_loop():
    while myPlayer.isAlive is True:
        prompt()
        

def setup_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_pause([(speechDict['strangerIntro']['question01']),
                 (speechDict['strangerIntro']['question02']),
                 (speechDict['strangerIntro']['question03']),
                 (speechDict['strangerArchetype']['question01'])],
                neutralStranger.name)
    
    print_pause((speechDict['generalHelp']['archetype01']))
    
    starterWeapon_list = ["Sword", "Bow and Quiver"]
    prompt_list(starterWeapon_list)
    
    print("\nSelect your starting weapon...")
    player_starterWeapon = input("> ")
    
    
    ##### Starter Weapon #####
    if player_starterWeapon == "1":
        print_pause((speechDict['generalHelp']['archetype02']))
        print_pause([(speechDict['strangerArchetype']['answer01'])], neutralStranger.name)
    elif player_starterWeapon == "2":
        print_pause((speechDict['generalHelp']['archetype03']))
        print_pause([(speechDict['strangerArchetype']['answer02'])], neutralStranger.name)
    while player_starterWeapon not in ["1", "2"]:
        print(f"\nThere is no such thing here.\n")
        prompt_list(starterWeapon_list)
        print(f"\nSelect your started weapon...")
        player_starterWeapon = input("> ")
        if player_starterWeapon == "1":
            print('\n')
            print_pause((speechDict['generalHelp']['archetype02']))
            print_pause([(speechDict['strangerArchetype']['answer01'])], neutralStranger.name)
        elif player_starterWeapon == "2":
            print('\n')
            print_pause((speechDict['generalHelp']['archetype03']))
            print_pause([(speechDict['strangerArchetype']['answer02'])], neutralStranger.name)
        
    


    myPlayer.name = player_name

    ##### ARCHETYPE COLLECTING #####
    playerQuestion_archetype = "What ?\n"
    print_pause(playerQuestion_archetype, 0.05)    
    print("['Warrior', 'Mage', 'Ranger']\n")
    
    player_archetype = input("> ")
    valid_archetype = ['warrior', 'mage', 'ranger']
    if player_archetype.lower() in valid_archetype:
        myPlayer.archetype = player_archetype.title()
        print("Welcome, " + player_archetype + ".")
    while player_archetype.lower() not in valid_archetype:
        print("Ah ah, right!")
        player_archetype = input("> ")

    if myPlayer.archetype is 'warrior':
        myPlayer.health = 120
        myPlayer.mana = 20
    elif myPlayer.archetype is 'mage':
        myPlayer.health = 60
        myPlayer.mana = 80
    elif myPlayer.archetype is 'ranger':   
        myPlayer.health = 100
        myPlayer.mana = 40
        
    ### INTRODUCTION ###
    question3 = "Welcome, " + player_name + " the " + player_archetype + ".\n"
    for char in question3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.4)
        
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###########################")
    print("###########################")
    print("###########################")
    main_game_loop()






os.system('cls' if os.name == 'nt' else 'clear')
title_screen()
