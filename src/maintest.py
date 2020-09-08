from player import *
from items import *
from intro import *
from menu import *
# import intro
# import world

myPlayer = Player()

#####                         ##### 
#####    STRING FORMATTING    #####
#####                         ##### 
def textFormat(x):
    if len(x) % 2 == 0:
        print('{:^120}'.format(str(x)))
    elif len(x) % 2 !=0:
        print('{:^119}'.format(str(x)))


def print_pause(line, name=None, pause=0.02, postpause=1, header=False, center=False, dot=False):
    lineLenght = len(line) + 10
    if header == True and center == False:
        print("")
        wrapper = textwrap.fill(line, width=lineLenght)  
        for char in wrapper:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(pause)
        time.sleep(postpause)
    elif header == True and center == True:
        print("")
        wrapper = textwrap.fill(line, width=lineLenght, initial_indent=' '*10)  
        for char in wrapper:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(pause)
        time.sleep(postpause)
    elif (header == False and center == False) and dot == True:
        wrapper = textwrap.fill(line, width=120)  
        for char in wrapper:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(pause)
        time.sleep(postpause)

    #####
    elif name is not None and line != 1: #> Name AND many lines
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

##### Move line
# sys.stdout.write("\033[F"*28)

#### Replace line string f{}
# for i in range(10):
#     time.sleep(1)
#     print(f'{i}\r', end='')












#####                           ##### 
#####    MAIN SCREEN DISPLAY    ##### 
#####                           ##### 

def title_screen_options():
    option = input("> ")
    main_screen()

##### Main Screen Options #####
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
            
##### Secondary Screen Options #####
def sub_screen_options():
    option = int(input("> "))
    if option == 1:
            main_screen()
    while option not in [1]:
        print("Please enter a valid option.")
        option = int(input("> "))
        if option == 1:
            main_screen()

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
        
if __name__ == "__main__":
    
    boundingScreen()
    
    ##### GATE INTERACTION #####



        
    # def main_game_loop():
    #     while myPlayer.isAlive is True:
    #         prompt()
            

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
            



        
    
    
    
    # print(theOutskirts._description)
#     print('Check!')

# #     myPlayer.inventory = [Torch(), Silver(15)]
# #     for attr in ['name', 'description']:
# #         print(getattr(myPlayer.inventory[0], attr))
# #     print('\n')

# # # if myPlayer.location._north != None:
# # #     print(myPlayer.location)
# # #     print(myPlayer.location._north)
# # # myPlayer.location = myPlayer.location._north
# # # print(myPlayer.location)
# #     #    print(dictWorld['theOutskirts']._intro)
   
#     def introParser(x):
#         os.system('cls' if os.name == 'nt' else 'clear')
#         myPlayer._location._intro
#         print('\n'*8)
#         time.sleep(4)
#         os.system('cls' if os.name == 'nt' else 'clear')
#         # introName()
        

#     def movementDev_loop():
#         print("\nMovementDev [1] North  [2] South")
#         user_InputDev = input("> ")

#         while user_InputDev not in ["1", "2"]:
#             print('Invalid input...')
#             print("\nMovementDev [1] North  [2] South")
#             user_InputDev = input("> ")

#         if user_InputDev == "1":
#             if myPlayer.location._north == None:
#                 print("Nothing North.")
#                 movementDev_loop()
#             else:
#                 myPlayer._location = dictWorld[myPlayer._location._north]
#                 introVar = myPlayer._location._intro
#                 var = myPlayer._location._intro
#                 introParser(var)
#                 print(f"You've reached {myPlayer.location._name}...")
#                 print('***')
#                 print(myPlayer._location)
#                 print(type(myPlayer._location))
#                 print('***')
#                 movementDev_loop()
#         elif user_InputDev == "2":
#             if myPlayer.location._south == None:
#                 print("Nothing South.")
#                 movementDev_loop()
#             else:
#                 myPlayer._location = dictWorld[myPlayer._location._south]
#                 introVar = myPlayer._location._intro
#                 var = myPlayer._location._intro
#                 introParser(var)
#                 print(f"You've reached {myPlayer.location._name}...")
#                 print('***')
#                 print(myPlayer._location)
#                 print(type(myPlayer._location))
#                 print('***')
#                 movementDev_loop()
                
    
#     movementDev_loop()
#     os.system('cls' if os.name == 'nt' else 'clear')
    # var = 'theOutskirts'
    # introParser(var)
    
    # movementDev_loop()
    # myPlayer._name = 'Alaric'
    
    # print('***')
    # print(myPlayer._location)
    # print(type(myPlayer._location))
    # print('***')
    
    # myPlayerLocation = myPlayer._location
    # myPlayer._location = dictWorld[myPlayerLocation]
    # print(myPlayer._location)
    
    
    # print(myPlayer._name)
    # repr(myPlayer.location.__dict__['_name'])
    # # print(myPlayer.location._north.__dict__['_east'])
    # myPlayer.location = myPlayer.location._north.__dict__['_east']
    # # print(myPlayer.location)
    
    # myPlayer._location = myPlayer.location._north
    
    # print(myPlayer.location)
    
    # myPlayer.location = thePaleGate
    # myPlayer.location = myPlayer.location._north
    # print(myPlayer.location._description)
    # print(myPlayer.location._north._description)
    # myPlayer.location = theOutskirts._north
    # print('\n')
    # print(myPlayer.location.__repr__)
    
    # print(myPlayer.location)

    # print(myPlayer.location._south)  
    
    # print((dictWorld['theOutskirts']))
    # print(myPlayer.location.north)
    # title_theTorchedHalls()
 
    # var = myPlayer._location._intro
    # introParser(var)
 
    # print(myPlayer._location._intro)
    # print(myPlayer._location._north)
    # myPlayerLocation = myPlayer._location._north
    # myPlayer._location = dictWorld[myPlayerLocation]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
