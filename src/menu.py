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
    print('{:░^120}'.format('████████╗██╗░░██╗███████╗░░░██████╗░░█████╗░██╗░░░░░███████╗░░░░█████╗░░█████╗░██╗░░░██╗██████╗░████████╗'))
    print('{:░^120}'.format('╚══██╔══╝██║░░██║██╔════╝░░░██╔══██╗██╔══██╗██║░░░░░██╔════╝░░░██╔══██╗██╔══██╗██║░░░██║██╔══██╗╚══██╔══╝'))
    print('{:░^120}'.format('░░░██║░░░███████║█████╗░░░░░██████╔╝███████║██║░░░░░█████╗░░░░░██║░░╚═╝██║░░██║██║░░░██║██████╔╝░░░██║░░░'))
    print('{:░^120}'.format('░░░██║░░░██╔══██║██╔══╝░░░░░██╔═══╝░██╔══██║██║░░░░░██╔══╝░░░░░██║░░██╗██║░░██║██║░░░██║██╔══██╗░░░██║░░░'))
    print('{:░^120}'.format('░░░██║░░░██║░░██║███████╗░░░██║░░░░░██║░░██║███████╗███████╗░░░╚█████╔╝╚█████╔╝╚██████╔╝██║░░██║░░░██║░░░'))
    print('{:░^120}'.format('░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝░░░░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░'))

def version_title():
    print('{:=^120}'.format(''))
    print('{:^120}'.format('The Pale Court 0.0.2'))
    
def sub_title_encyclopedia():
    print('\n')
    print('{:=^120}'.format('=====/(----------)\====='))
    print('{:^120}'.format('<[  ENCYCLOPEDIA  ]>'))
    print('{:=^120}'.format('=====\(----------)/====='))
    
def sub_title_help():
    print('\n')
    print('{:=^120}'.format('=====/(------------)\====='))
    print('{:^120}'.format('<[  INSTRUCTIONS  ]>'))
    print('{:=^120}'.format('=====\(------------)/====='))


##### MAIN MENU #####
def title_screen(): # Title
    os.system('cls' if os.name == 'nt' else 'clear')
    main_title()
    # print('\n')
    version_title()
    print('\n'*4)
    print('{:^120}'.format('The halls of your lineage, once familiar, now foreign whisper of heresy.'))
    print('\n'*6)
    print('{:^120}'.format('[ enter any key to continue ]'))
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
    'masterGlobal' :{
      'missingItem' : """You aren't not holding any """,
      'inventoryItem' : """You are holding a """
    },
    'generalHelp' : {
        'archetype01': """You rumage through oddities and relics of the past. You make out a weapon through the pile...""",
        'archetype02': """After closer inspection, you find a """,
        'archetype03': """After closer inspection, you find a """
    },
    'answersGlobal': {
        'answer01': """A fair choice."""
    },
    'strangerIntro': {
        'question01': """It's been a while since I've greeted travellers.""",
        'question02': """Most end up here by curiosity, interest, or obssesion.""",
        'question03': """... you don't seem lost.""",
        'question04': """What brings you to our venerable house stranger?"""
    },
    'strangerArchetype': {
        'question01': """Search the locker behind the desk. You'll find forgotten artifacts from the very bellows that once spured this estate to life.""",
        'answer01': """A strong arm, and sharp sword, an anchor of purpose.""",
        'answer02': """A keen eye, and a strong bow, an anchor of purpose."""
    },
}









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
    starterSword01 = RandWeapon(weaponMasterMaterialMelee,
                                weaponMasterPrefixMelee,
                                weaponMeleeStarter)

    starterBow01 = RandWeapon(weaponMasterMaterialRange,
                          weaponMasterPrefixRange,
                          weaponRangeStarter)


    while player_starterWeapon not in ["1", "2"]:
        print(f"\nThere is no such thing here.\n")
        prompt_list(starterWeapon_list)
        print(f"\nSelect your started weapon...")
        player_starterWeapon = input("> ")
    if player_starterWeapon == "1":
        print_pause((speechDict['generalHelp']['archetype02']) + f"{starterSword01}" + ".")
        print_pause([(speechDict['strangerArchetype']['answer01']),
                 (speechDict['answersGlobal']['answer01'])],
                neutralStranger.name)
    elif player_starterWeapon == "2":
        print_pause((speechDict['generalHelp']['archetype03']) + f"{starterBow01}" + " with a sack of wooden arrows.")
        print_pause([(speechDict['generalHelp']['archetype03']),
                 (speechDict['answersGlobal']['answer01'])],
                neutralStranger.name)
    # while player_starterWeapon not in ["1", "2"]:
    #     print(f"\nThere is no such thing here.\n")
    #     prompt_list(starterWeapon_list)
    #     print(f"\nSelect your started weapon...")
    #     player_starterWeapon = input("> ")
    #     if player_starterWeapon == "1":
    #         print('\n')
    #         print_pause((speechDict['generalHelp']['archetype02']) + f"{starterSword01}" + ".")
    #         print_pause([(speechDict['strangerArchetype']['answer01']),
    #                 (speechDict['answersGlobal']['answer01'])],
    #                 neutralStranger.name)
    #     elif player_starterWeapon == "2":
    #         print('\n')
    #         print_pause((speechDict['generalHelp']['archetype03']) + f"{starterBow01}" + " with a sack of wooden arrows.")
    #         print_pause([(speechDict['generalHelp']['archetype03']),
    #                 (speechDict['answersGlobal']['answer01'])],
    #                 neutralStranger.name)
        




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
        

        
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###########################")
    print("###########################")
    print("###########################")
    main_game_loop()






os.system('cls' if os.name == 'nt' else 'clear')
title_screen()

if __name__ == "__main__":
    print('Check!')