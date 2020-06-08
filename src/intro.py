import cmd
import textwrap
import sys
import os
import time
import random
from itertools import repeat

from player import *
from enemies import *

#####                      ##### 
#####   Text Formatting    #####
#####                      #####
def textFormat(x):
    if len(x) % 2 == 0:
        print('{:^120}'.format(str(x)))
    elif len(x) % 2 !=0:
        print('{:^119}'.format(str(x)))
#####
def print_pause(line, name=None, pause=0.02, postpause=1, header=False, center=False, dot=False):
    lineLenght = len(line) + 10
    if header == True and center == False: ## header
        print("")
        wrapper = textwrap.fill(line, width=lineLenght)  
        for char in wrapper:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(pause)
        time.sleep(postpause)
    elif header == True and center == True: ## header indent
        print("")
        wrapper = textwrap.fill(line, width=lineLenght, initial_indent=' '*10)  
        for char in wrapper:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(pause)
        time.sleep(postpause)
    elif (header == False and center == False) and dot == True: ## special dot
        wrapper = textwrap.fill(line, width=120)  
        for char in wrapper:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(pause)
        time.sleep(postpause)
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
            
            
def print_pauseUpdate(line, name=None, pause=0.02, postpause=1, initIndent=0, subIndent=0, n=False):
    initIndentList = ""
    subIndentList = ""
    for i in repeat(None, initIndent):
        initIndentList += "    "
    for i in repeat(None, subIndent):
        subIndentList += "    "
    if name == None: #> Name AND one line
        wrapper = textwrap.fill(line, initial_indent=initIndentList, subsequent_indent=subIndentList)    
        for char in wrapper:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(pause)
        time.sleep(postpause)
        if n == True:
            print('n')
        elif n == False:
            pass
    else:
        print(f'[{name}]')
        for block in line:
            wrapper = textwrap.fill(block, initial_indent=subIndentList)    
            for char in wrapper:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(pause)
            time.sleep(postpause)
            if n == True:
                print('n')
            elif n == False:
                pass
    # elif name is None and line != 1: # No nome AND many line
    #         print("")
    #         wrapper = textwrap.fill(line)  
    #         for char in wrapper:
    #             sys.stdout.write(char)
    #             sys.stdout.flush()
    #             time.sleep(pause)
    #         time.sleep(postpause)
    #         print('\n')
#####                    ##### 
#####   Title Screens    #####
#####                    #####
def title_zoneDicovery():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n'*2)
    print_pause('█▄█ █▀█ █░█   █▀▄ █ █▀ █▀▀ █▀█ █░█ █▀▀ █▀█ █▀▀ █▀▄', pause=0.01, postpause=0, header=True, center=True)
    print_pause('░█░ █▄█ █▄█   █▄▀ █ ▄█ █▄▄ █▄█ ▀▄▀ ██▄ █▀▄ ██▄ █▄▀', pause=0.01, postpause=0, header=True, center=True)
    print_pause(' ▄ ▄ ▄',name=None, pause=0.25, postpause=0.50, header=False, center=False, dot=True)
    print('\n'*7)
def title_theTorchedHalls():
    title_zoneDicovery()
    textFormat('▀▀█▀▀ █░░█ █▀▀   ▀▀█▀▀ █▀▀█ █▀▀█ █▀▀ █░░█ █▀▀ █▀▀▄   ▒█░▒█ █▀▀█ █░░ █░░ █▀▀') 
    textFormat('░▒█░░ █▀▀█ █▀▀   ░▒█░░ █░░█ █▄▄▀ █░░ █▀▀█ █▀▀ █░░█   ▒█▀▀█ █▄▄█ █░░ █░░ ▀▀█')      
    textFormat('░▒█░░ ▀░░▀ ▀▀▀   ░▒█░░ ▀▀▀▀ ▀░▀▀ ▀▀▀ ▀░░▀ ▀▀▀ ▀▀▀░   ▒█░▒█ ▀░░▀ ▀▀▀ ▀▀▀ ▀▀▀')       
    textFormat('▒▀░░▀▀▀▒▀░░▒░░▀▀▀▀▒░▀░▀▀▀▀▀▒▀░░▀▀░▀▒░▒░▒░░▀▒▓▀░▒▓░▀▀▀▀░▒▀▒▀▀░▒▀░░▒░░░▀▀░░▒░▒▒▒▀▀▀') #75 #81 (6)
    textFormat('  ░    ▒ ░▒░ ░    ░  ░       ░     ░ ▒ ▒░  ░▒ ░ ▒░    ░  ▒   ▒ ░▒░ ░░  ░▒░ ░ ▒   ')
    textFormat('░      ░  ░░ ░    ░                  ░ ▒   ░░    ░           ░  ░░ ░    ░░ ░ ░   ')
    textFormat('          ░                            ░    ░                   ░       ░  ░     ')
    print('\n'*6)
def title_theOutskirts():
    title_zoneDicovery()
    textFormat('▀▀█▀▀ █░░█ █▀▀ 　 ▒█▀▀▀█ █░░█ ▀▀█▀▀ █▀▀ █░█ ░▀░ █▀▀█ ▀▀█▀▀ █▀▀')
    textFormat('░▒█░░ █▀▀█ █▀▀ 　 ▒█░░▒█ █░░█ ░░█░░ ▀▀█ █▀▄ ▀█▀ █▄▄▀ ░░█░░ ▀▀█')
    textFormat('░▒█░░ ▀░░▀ ▀▀▀ 　 ▒█▄▄▄█ ░▀▀▀ ░░▀░░ ▀▀▀ ▀░▀ ▀▀▀ ▀░▀▀ ░░▀░░ ▀▀▀\n')
    textFormat('▒▀░░▀▀▀▒▀░░▒░░░▀▒░▀░▀▀▀░▀▒░▒░▒░░▒▓▒▀▒▀▒▀▀▒▀░░▀▀▒▀▒▓▒▀▒▀░░▀▀▒▀▒▓▒▀▒▀░')
    textFormat('  ░    ▒ ░▒░ ░░ ░  ░     ░ ▒ ▒░░░▒░ ░ ░    ░   ░ ░▒  ░ ░   ░ ░▒  ░ ░')
    textFormat('       ░  ░░ ░           ░ ░ ▒  ░░░ ░ ░        ░  ░  ░        ░  ░  ')
    textFormat('          ░                  ░    ░                                 ')
    print('\n'*6)
def title_thePaleGate():
    title_zoneDicovery()
    textFormat('▀▀█▀▀ █░░█ █▀▀   ▒█▀▀█ █▀▀█ █░░ █▀▀   ▒█▀▀█ █▀▀█ ▀▀█▀▀ █▀▀')
    textFormat(' ░▒█░░ █▀▀█ █▀▀   ▒█▄▄█ █▄▄█ █░░ █▀▀   ▒█░▄▄ █▄▄█ ░░█░░ █▀▀')
    textFormat(' ░▒█░░ ▀░░▀ ▀▀▀   ▒█░░░ ▀░░▀ ▀▀▀ ▀▀▀   ▒█▄▄█ ▀░░▀ ░░▀░░ ▀▀▀\n')
    textFormat('▒▀░░▒▀░░▒░░░▀▀▀▀▒▓▒░▀░▀▀░▒▒▀▀▀▓▒█░▀▀░░▀▒░▀░▀▀▀▀░▒▀▀▀▒▀▒▒▀▀▀▓▒█░▒')
    textFormat('  ░ ▒ ░▒░ ░░    ░▒ ░      ▒   ▒▒ ░  ░░ ░  ░     ░   ░  ▒   ▒▒ ░ ')
    textFormat('    ░  ░░ ░     ░         ░   ▒        ░        ░   ░  ░   ▒    ')
    textFormat('       ░                                            ░      ░    ')
    print('\n'*6)
def title_theBattlements():
    title_zoneDicovery()
    textFormat('▀▀█▀▀ █░░█ █▀▀   ▒█▀▀█ █▀▀█ ▀▀█▀▀ ▀▀█▀▀ █░░ █▀▀ █▀▄▀█ █▀▀ █▀▀▄ ▀▀█▀▀ █▀▀')
    textFormat('░▒█░░ █▀▀█ █▀▀   ▒█▀▀▄ █▄▄█ ░░█░░ ░░█░░ █░░ █▀▀ █░▀░█ █▀▀ █░░█ ░░█░░ ▀▀█')
    textFormat('░▒█░░ ▀░░▀ ▀▀▀   ▒█▄▄█ ▀░░▀ ░░▀░░ ░░▀░░ ▀▀▀ ▀▀▀ ▀░░░▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀\n')
    textFormat('▒▀░░▀▀▀▒▀░░▒░░░▀▒░▀░▀▀▀░▒▓███▀▒▒▒▀▀▀▀▒░▀▀▀░▀▀░░▀▒░▀░▀▒░▀▀▀▒▀▒▀▀▒▀░░▀▀▒▀▒▓▒▀▒▀░')
    textFormat('  ░    ▒ ░▒░ ░░ ░  ░   ▒░▒   ░  ▒     ░      ░░ ░  ░ ░░   ░ ▒░   ░   ░ ░▒  ░ ░')
    textFormat('          ░░ ░  ░       ░    ░  ░               ░     ░   ░ ░        ░  ░  ░  ')
    textFormat('          ░             ░                       ░           ░              ░  ')
    print('\n'*6)
def title_theAshbourneConcourse():
    title_zoneDicovery()
    textFormat('▀▀█▀▀ █░░█ █▀▀   ░█▀▀█ █▀▀ █░░█ █▀▀▄ █▀▀█ █░░█ █▀▀█ █▀▀▄ █▀▀   ▒█▀▀█ █▀▀█ █▀▀▄ █▀▀ █▀▀█ █░░█ █▀▀█ █▀▀ █▀▀')
    textFormat('░▒█░░ █▀▀█ █▀▀   ▒█▄▄█ ▀▀█ █▀▀█ █▀▀▄ █░░█ █░░█ █▄▄▀ █░░█ █▀▀   ▒█░░░ █░░█ █░░█ █░░ █░░█ █░░█ █▄▄▀ ▀▀█ █▀▀')
    textFormat('░▒█░░ ▀░░▀ ▀▀▀   ▒█░▒█ ▀▀▀ ▀░░▀ ▀▀▀░ ▀▀▀▀ ░▀▀▀ ▀░▀▀ ▀░░▀ ▀▀▀   ▒█▄▄█ ▀▀▀▀ ▀░░▀ ▀▀▀ ▀▀▀▀ ░▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀\n')
    textFormat('▀░░▒░░░▀▒░▀░▀▀▀▀▒▒▀▀▀▓▒█▒▀▒▓▒▀▒▀░▒▀░░▒░░▒▓███░░▀▒░▒░▒░░▒▓░▀▀▀▒▀▀▀▀░▒▀▒▀▀░▀▒░▒░▒░░▒▓▒▀▒▀▒░▀▒▓▀░▒▓▒▀▒▓▒▀▒▀░░▀▒░▀░')
    textFormat(' ░▒░ ░░ ░  ░     ▒   ▒▒ ░ ░▒  ░ ░▒ ░▒░ ▒░▒   ░  ░ ▒ ▒░░░▒░   ░    ░  ▒    ░ ▒ ▒░░░▒░ ░ ░  ░▒ ░ ▒░ ░▒  ░ ░░ ░  ░')
    textFormat('  ░░ ░           ░   ▒  ░  ░  ░  ░  ░░ ░░    ░  ░ ░ ▒  ░░░   ░            ░ ░ ▒  ░░░ ░ ░  ░░   ░░  ░  ░    ░   ')
    textFormat('  ░  ░               ░        ░     ░  ░          ░ ░                         ░    ░       ░          ░    ░   ')  
    print('\n'*6)                                      
def title_theBlacksmith():
    title_zoneDicovery()
    textFormat('▀▀█▀▀ █░░█ █▀▀   ▒█▀▀█ █░░ █▀▀█ █▀▀ █░█ █▀▀ █▀▄▀█ ░▀░ ▀▀█▀▀ █░░█')
    textFormat('░▒█░░ █▀▀█ █▀▀   ▒█▀▀▄ █░░ █▄▄█ █░░ █▀▄ ▀▀█ █░▀░█ ▀█▀ ░░█░░ █▀▀█')
    textFormat('░▒█░░ ▀░░▀ ▀▀▀   ▒█▄▄█ ▀▀▀ ▀░░▀ ▀▀▀ ▀░▀ ▀▀▀ ▀░░░▀ ▀▀▀ ░░▀░░ ▀░░▀\n')
    textFormat('▒▀░░▀▀▀▒▀░░▒░░░▀▒░▀░▀▀▀░▒▓███▀░▀▒░▓▀▀▒▒▀▀▀▓▒█░▀░▒▀▒▀▀▒▀▒▒▀▓▒▀▀▀▒▀░░▒░▒')
    textFormat('  ░    ▒ ░▒░ ░░ ░  ░   ▒░▒   ░░ ░ ▒  ░▒   ▒▒ ░ ░  ▒  ░ ░▒ ▒░   ▒ ░▒░ ░')
    textFormat('          ░░ ░  ░       ░    ░    ░   ░   ▒  ░       ░ ░░ ░░   ░  ░░ ░')
    textFormat('          ░             ░         ░       ░          ░  ░      ░  ░  ░')
    print('\n'*6)
def title_theGrainCellars():
    title_zoneDicovery()
    textFormat('▀▀█▀▀ █░░█ █▀▀   ▒█▀▀█ █▀▀█ █▀▀█ ░▀░ █▀▀▄   ▒█▀▀█ █▀▀ █░░ █░░ █▀▀█ █▀▀█ █▀▀')
    textFormat('░▒█░░ █▀▀█ █▀▀   ▒█░▄▄ █▄▄▀ █▄▄█ ▀█▀ █░░█   ▒█░░░ █▀▀ █░░ █░░ █▄▄█ █▄▄▀ ▀▀█')
    textFormat('░▒█░░ ▀░░▀ ▀▀▀   ▒█▄▄█ ▀░▀▀ ▀░░▀ ▀▀▀ ▀░░▀   ▒█▄▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ▀░▀▀ ▀▀▀\n')
    textFormat('▀░░▒░░░▀▀▀▀▀▀▀▒░▀▒▓▀░▒▓░▒▒▀▀▀▓▒█░▓▀░▀▒░▀▀▀▒▀▒▀▀▀▀░▀░▒▀▒▀▀░░▀▒░▀▓▒█░▀▀░▒▓▒▀▒▓▒▀▒▀░')
    textFormat(' ░░ ░  ░      ░  ░▒ ░ ▒░ ▒   ▒▒ ░▒ ░ ░░   ░ ▒░     ░  ▒   ░ ░  ▒▒ ░  ░ ▒░ ░▒  ░ ░')
    textFormat(' ░  ░         ░  ░░   ░  ░   ▒   ▒ ░  ░   ░ ░               ░  ▒       ░░  ░  ░  ')
    textFormat(' ░  ░         ░   ░          ░   ░          ░               ░  ░              ░  ')
    print('\n'*6)
def title_theUndercroft():
    title_zoneDicovery()
    textFormat('▀▀█▀▀ █░░█ █▀▀   ▒█░▒█ █▀▀▄ █▀▀▄ █▀▀ █▀▀█ █▀▀ █▀▀█ █▀▀█ █▀▀ ▀▀█▀▀')
    textFormat('░▒█░░ █▀▀█ █▀▀   ▒█░▒█ █░░█ █░░█ █▀▀ █▄▄▀ █░░ █▄▄▀ █░░█ █▀▀ ░░█░░')
    textFormat('░▒█░░ ▀░░▀ ▀▀▀   ░▀▄▄▀ ▀░░▀ ▀▀▀░ ▀▀▀ ▀░▀▀ ▀▀▀ ▀░▀▀ ▀▀▀▀ ▀░░ ░░▀░░\n')
    textFormat('▒▀░░▀▀▀▒▀░░▒░░▀▀▀░▀▀▀░▒▓▒▀▒▀▒░▀▒░▀▒▓░▀░▀▒▓▀░▒▓░▀░▒▀▒▀▀░▀▒▓▀░▒▓░▀▀▀▀▒▀░░')
    textFormat('   ▒ ░▒░ ░░ ░    ░░▒░ ░ ░░ ░░   ░ ▒ ░▒ ░ ▒░ ░  ▒    ░▒ ░ ▒░ ░ ▒        ')
    textFormat('   ░  ░░ ░         ░░ ░ ░   ░   ░ ░ ░░   ░░         ░░   ░░ ░ ░        ')
    textFormat('      ░             ░                ░    ░          ░                 ')
    print('\n'*6)
def title_theReliquary():
    title_zoneDicovery()
    textFormat('▀▀█▀▀ █░░█ █▀▀   ▒█▀▀█ █▀▀ █░░ ░▀░ █▀▀█ █░░█ █▀▀█ █▀▀█ █░░█')
    textFormat('░▒█░░ █▀▀█ █▀▀   ▒█▄▄▀ █▀▀ █░░ ▀█▀ █░░█ █░░█ █▄▄█ █▄▄▀ █▄▄█')
    textFormat('░▒█░░ ▀░░▀ ▀▀▀   ▒█░▒█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀█ ░▀▀▀ ▀░░▀ ▀░▀▀ ▄▄▄█\n')
    textFormat('▒▀░░▀▒▀░░▒░░░▀▀▀▒▓▀░▒▓░░▀▒░▀░▀▀▀░▒▓▒▀▒▀▒▀▒▒▀▀▀▓▒█░▀▒▓▀░▒▓░▀█▒▒▒▀▀')
    textFormat('  ░  ▒ ░▒░ ░░   ░▒ ░ ▒░░ ░  ░   ░░▒░ ░ ░  ▒   ▒▒ ░ ░▒ ░ ▒▓  ░▒░  ')
    textFormat('     ░  ░░ ░    ░░   ░   ░       ░░░ ░ ░  ░   ▒    ░░   ░▒  ░░   ')
    textFormat('        ░        ░                 ░          ░     ░    ░       ')
    print('\n'*6)
def title_theProfaneShrine():
    title_zoneDicovery()
    textFormat('▀▀█▀▀ █░░█ █▀▀   ▒█▀▀█ █▀▀█ █▀▀█ █▀▀ █▀▀█ █▀▀▄ █▀▀   ▒█▀▀▀█ █░░█ █▀▀█ ░▀░ █▀▀▄ █▀▀')
    textFormat('░▒█░░ █▀▀█ █▀▀   ▒█▄▄█ █▄▄▀ █░░█ █▀▀ █▄▄█ █░░█ █▀▀   ░▀▀▀▄▄ █▀▀█ █▄▄▀ ▀█▀ █░░█ █▀▀')
    textFormat('░▒█░░ ▀░░▀ ▀▀▀   ▒█░░░ ▀░▀▀ ▀▀▀▀ ▀░░ ▀░░▀ ▀░░▀ ▀▀▀   ▒█▄▄▄█ ▀░░▀ ▀░▀▀ ▀▀▀ ▀░░▀ ▀▀▀\n')
    textFormat('▒▀░░▀▀▀▒▀░░▒▀▀▀▀▒▓▒░▀░▀▀░▀▒▓▀░▒▓░▀▒░▒░▒░▀▒▀░▀▀▀▒▒▀▀▀▓▒█░▀▒░▀▀▀▒▀▀░▒▓░▓▀░▀▒░▀▀▀▒▀▒░░▀▒░▀░')
    textFormat('  ░    ▒ ░▒░    ░▒ ░      ░▒ ░ ▒░ ░ ▒ ▒░ ░      ▒   ▒▒ ░ ░░   ░  ░ ▒░▒ ░ ░░   ░ ▒░░ ░  ░')
    textFormat('          ░░    ░░        ░░   ░░ ░ ░ ▒  ░      ░   ▒     ░   ░    ░ ▒ ░  ░   ░ ░   ░   ')
    textFormat('          ░                ░        ░ ░             ░                ░          ░   ░   ') 
    print('\n'*6)                                                                                            
def title_thePaleThrone():
    title_zoneDicovery()
    textFormat('▀▀█▀▀ █░░█ █▀▀   ▒█▀▀█ █▀▀█ █░░ █▀▀   ▀▀█▀▀ █░░█ █▀▀█ █▀▀█ █▀▀▄ █▀▀')
    textFormat('░▒█░░ █▀▀█ █▀▀   ▒█▄▄█ █▄▄█ █░░ █▀▀   ░▒█░░ █▀▀█ █▄▄▀ █░░█ █░░█ █▀▀')
    textFormat('░▒█░░ ▀░░▀ ▀▀▀   ▒█░░░ ▀░░▀ ▀▀▀ ▀▀▀   ░▒█░░ ▀░░▀ ▀░▀▀ ▀▀▀▀ ▀░░▀ ▀▀▀\n')
    textFormat('▀▒▀░░▀▀▀▒▀░░▒▀▀▀▀▀▀▀▒▓▒▀▀░▒▒▀▀▀▓▒█░▀░░▒░░▀▒▓▀░▒▓░▀▒░▒░▒░░▀▒░▀▀▀▒▀▒░░▀▒░▀░')
    textFormat('   ░    ▒ ░▒░       ░▒     ▒   ▒▒ ░ ░▒░ ░ ░▒ ░ ▒░ ░ ▒ ▒░░ ░░   ░ ▒░░ ░  ░')
    textFormat('        ░  ░░       ░░     ░   ▒     ░░ ░ ░░   ░░ ░ ░ ▒    ░   ░ ░   ░   ')
    textFormat('           ░                   ░     ░  ░  ░        ░ ░          ░   ░   ')
    print('\n'*6)
def title_theTerrace():
    title_zoneDicovery()
    textFormat('▀▀█▀▀ █░░█ █▀▀   ▀▀█▀▀ █▀▀ █▀▀█ █▀▀█ █▀▀█ █▀▀ █▀▀')
    textFormat('░▒█░░ █▀▀█ █▀▀   ░▒█░░ █▀▀ █▄▄▀ █▄▄▀ █▄▄█ █░░ █▀▀')
    textFormat('░▒█░░ ▀░░▀ ▀▀▀   ░▒█░░ ▀▀▀ ▀░▀▀ ▀░▀▀ ▀░░▀ ▀▀▀ ▀▀▀\n')
    textFormat('▀░░▒▀░░▒▀▒░▀▒░▀▀▀▀▀░▀▒▓▀░▒▓░▀▒▓▀░▒▓░▒▒▀▀▀▓▒█░▀░▒▀▒▒░▀░')
    textFormat(' ░ ▒ ░▒░ ░  ░      ░ ░▒ ░ ▒░ ░▒ ░ ▒░ ▒   ▒▒ ░ ░  ▒░  ░')
    textFormat('   ░  ░░    ░        ░░   ░  ░░   ░  ░   ▒  ░     ░   ')
    textFormat('      ░               ░       ░          ░            ')
    print('\n'*6)
def title_theKerberosGate():
    n = 0.2
    title_zoneDicovery()
    os.system('cls' if os.name == 'nt' else 'clear')    
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                              ,,⌐▄▄▄▄▄▄████▄▄▄▄▄▄⌐,,                                                    ")
    textFormat("                                          ▀████████████▀▀▀▀▀▀▀▀▀▀▀▀███████████                                          ")
    textFormat("                                     ▄▄██▀▀▀                               ▀▀▀██▄▄                                      ")
    textFormat("                   ╓▄█           ▄██▀   ,¬▄▄█████████████████████████▄▄╖,`        ▀██▄ ═         ██▄                    ")
    textFormat("               ,▄█████         /` ,▄██████████████▀▀▀▀░░░░▐▌░░░░▀▀▀▀██████████████▄, `\          █████▄,                ")
    textFormat("             ^██████████▀∞═ ^═▀███████╖        ███░░░░░░░░▐▌░░░░░░░▓███         ╖██████*  ⁿ═∞▀████████████              ")
    textFormat("                ^█████           ^██████████▄, ▀███░░░░░░░░▌░░░░░░▓████  ,▄██████████^  ,╔▄████ ▀████▀                  ")
    textFormat("                   `▀█                      ▀▀████████████████████████████▀▀                    ██^                     ")
    textFormat("                                      ,▄██^               ▐███              ^▀██,                                       ")
    textFormat("                                       ╟█                 ╟██P                                                          ")
    textFormat("                                    ╓██▀                                       ^██▄    ,                                ")
    textFormat("                             ▐██,▄██▀                                           '███▄,▄██                               ")
    textFormat("                             ███████`                                             ███████                               ") 
    textFormat("                            ▐███████▄                      █╓                     ╓████████                             ")
    textFormat("                            █████▀▀^^                     ╟██                     ^^▀▀█████                             ")
    textFormat("                                                           █                                                            ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ") 
    time.sleep(n)
    sys.stdout.write("\033[F"*28)
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                              ,,⌐▄▄▄▄▄▄████▄▄▄▄▄▄⌐,,                                                    ")
    textFormat("                                          ▀████████████▀▀▀▀▀▀▀▀▀▀▀▀███████████                                          ")
    textFormat("                                     ▄▄██▀▀▀                               ▀▀▀██▄▄                                      ")
    textFormat("                ╓▄█              ▄██▀   ,¬▄▄█████████████████████████▄▄╖,`        ▀██▄ ═             ██▄                ")
    textFormat("            ,▄█████            /` ,▄██████████████▀▀▀▀░░░░▐▌░░░░▀▀▀▀██████████████▄, `\              █████▄,            ")
    textFormat("          ^██████████▀∞═    ^═▀███████╖        ███░░░░░░░░▐▌░░░░░░░▓███         ╖██████*      ⁿ═∞▀████████████          ")
    textFormat("             ^█████              ^██████████▄, ▀███░░░░░░░░▌░░░░░░▓████  ,▄██████████^      ,╔▄████ ▀████▀              ")
    textFormat("                `▀█                         ▀▀████████████████████████████▀▀                        ██^                 ")
    textFormat("                                      ,▄██^               ▐███              ^▀██,                                       ")
    textFormat("                                       ╟█                 ╟██P                                                          ")
    textFormat("                                       ▀                                                                                ")
    textFormat("                                                                                                                        ")
    textFormat("                                 ╓██                                              ^██▄    ,                             ") 
    textFormat("                          ▐██,▄██▀                         █╓                      '███▄,▄██                            ")
    textFormat("                          ███████`                        ╟██                        ███████                            ")
    textFormat("                         ▐███████▄                         █                         ╓████████                          ")
    textFormat("                         █████▀▀^^                                                   ^^▀▀█████                          ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ") 
    time.sleep(n)
    sys.stdout.write("\033[F"*28)
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                              ,,⌐▄▄▄▄▄▄████▄▄▄▄▄▄⌐,,                                                    ")
    textFormat("                                          ▀████████████▀▀▀▀▀▀▀▀▀▀▀▀███████████                                          ")
    textFormat("                                     ▄▄██▀▀▀                               ▀▀▀██▄▄                                      ")
    textFormat("             ╓▄█                 ▄██▀   ,¬▄▄█████████████████████████▄▄╖,`        ▀██▄ ═                 ██▄            ")
    textFormat("         ,▄█████               /` ,▄██████████████▀▀▀▀░░░░▐▌░░░░▀▀▀▀██████████████▄, `\                  █████▄,        ")
    textFormat("       ^██████████▀∞═       ^═▀███████╖        ███░░░░░░░░▐▌░░░░░░░▓███         ╖██████*          ⁿ═∞▀████████████      ")
    textFormat("          ^█████                 ^██████████▄, ▀███░░░░░░░░▌░░░░░░▓████  ,▄██████████^          ,╔▄████ ▀████▀          ")
    textFormat("             `▀█                            ▀▀████████████████████████████▀▀                            ██^             ")
    textFormat("                                      ,▄██^               ▐███              ^▀██,                                       ")
    textFormat("                                       ╟█                 ╟██P                                                          ")
    textFormat("                                       ▀                                                                                ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ") 
    textFormat("                                                           █╓                                                           ")
    textFormat("                              ╓██                         ╟██                        ^██▄    ,                          ")
    textFormat("                       ▐██,▄██▀                            █                          '███▄,▄██                         ")
    textFormat("                       ███████`                                                         ███████                         ")
    textFormat("                      ▐███████▄                                                         ╓████████                       ")
    textFormat("                      █████▀▀^^                                                         ^^▀▀█████                       ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ") 
    time.sleep(n)
    sys.stdout.write("\033[F"*28)
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ")
    textFormat("                                              ,,⌐▄▄▄▄▄▄████▄▄▄▄▄▄⌐,,                                                    ")
    textFormat("                                          ▀████████████▀▀▀▀▀▀▀▀▀▀▀▀███████████                                          ")
    textFormat("                                     ▄▄██▀▀▀                               ▀▀▀██▄▄                                      ")
    textFormat("          ╓▄█                    ▄██▀   ,¬▄▄█████████████████████████▄▄╖,`        ▀██▄ ═                     ██▄        ")
    textFormat("      ,▄█████                  /` ,▄██████████████▀▀▀▀░░░░▐▌░░░░▀▀▀▀██████████████▄, `\                      █████▄,    ")
    textFormat("    ^██████████▀∞═          ^═▀███████╖        ███░░░░░░░░▐▌░░░░░░░▓███         ╖██████*              ⁿ═∞▀████████████  ")
    textFormat("       ^█████                    ^██████████▄, ▀███░░░░░░░░▌░░░░░░▓████  ,▄██████████^              ,╔▄████ ▀████▀      ")
    textFormat("          `▀█                               ▀▀████████████████████████████▀▀                                ██^         ")
    textFormat("                                      ,▄██^               ▐███              ^▀██,                                       ")
    textFormat("                                       ╟█                 ╟██P                                                          ")
    textFormat("                                       ▀                                                                                ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ") 
    textFormat("                                                           █╓                                                           ")
    textFormat("                                                          ╟██                                                           ")
    textFormat("                                                           █                                                            ")
    textFormat("                           ╓██                                                          ^██▄    ,                       ")
    textFormat("                    ▐██,▄██▀                                                             '███▄,▄██                      ")
    textFormat("                    ███████`                                                               ███████                      ")
    textFormat("                   ▐███████▄                                                               ╓████████                    ")
    textFormat("                   █████▀▀^^                                                               ^^▀▀█████                    ")
    textFormat("                                                                                                                        ")
    textFormat("                                                                                                                        ") 
    time.sleep(n)
    sys.stdout.write("\033[F"*28)
    textFormat("                                    █████                 ████                 ▄████`                                   ")
    textFormat("                                      ▀████,              ████              ,▄████                                      ")
    textFormat("                                        ▀████,   ,,⌐▄▄▄▄▄▄████▄▄▄▄▄▄⌐,,   ,█████                                        ")
    textFormat("                                          ▀████████████▀▀▀▀▀▀▀▀▀▀▀▀███████████                                          ")
    textFormat("                                       ▄████▀^`           ````           `^▀████▄                                       ")
    textFormat("                                    ▄██▀       ,¬▄▄██████████████████▄▄╖,       ▀██▄                                    ")
    textFormat("                                  ▄▀      ,▄███████▀▀▀▀░░░░▐▌░░░░▀▀▀▀███████▄,      ▀█                                  ")
    textFormat("      ╓▄█                       /`    ,▄█████▀` ███░░░░░░░░▐▌░░░░░░░▓███ `▀█████▄,     ═                       ██▄      ")
    textFormat("  ,▄█████                         ,▄████▀'      ▀███░░░░░░░░▌░░░░░░▓████      '▀████▄,                         █████▄,  ")
    textFormat("^███████████████▀∞═ⁿ        ^═▀███████,          ▀███▄▄░░░▒▒░░░░▒░█████          ,█░▒▓░███▀P*        ⁿ═∞▀███████████████")
    textFormat("   ^█████▓▒█░▒                   ^█████▄,        ▀████▄▄▄░▄▄▄▄█████        ,╔▄████▀░ ▒░                     ▓▒▀████▀    ")
    textFormat("      `▀█▒▒ ░                        ▀█████▄╖,     '▀██████████▀'     ,╓▄█████▀`     ░░                     ▒▒██^       ")
    textFormat("         ▒   ░                          █████████▄▄╖,,       ,,,╓▄▄▄████████                                ▒           ")
    textFormat("         ░  ░                          ▄████`  `▀▀█████████████████▀▀▀`   █████                             ░           ")
    textFormat("                                     ,▄████               ▐███               ▀████,                                     ")
    textFormat("                                   ,█████                 ╟███                 ▀████▄                                   ")
    textFormat("                   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀                  ")
    textFormat("                      ▀▀█▀▀ █░░█ █▀▀   ▒█░▄▀ █▀▀ █▀▀█ █▀▀▄ █▀▀ █▀▀█ █▀▀█ █▀▀   ▒█▀▀█ █▀▀█ ▀▀█▀▀ █▀▀                     ")
    textFormat("                      ░▒█░░ █▀▀█ █▀▀   ▒█▀▄░ █▀▀ █▄▄▀ █▀▀▄ █▀▀ █▄▄▀ █░░█ ▀▀█   ▒█░▄▄ █▄▄█ ░░█░░ █▀▀                     ")
    textFormat("                      ░▒█░░ ▀░░▀ ▀▀▀   ▒█░▒█ ▀▀▀ ▀░▀▀ ▀▀▀░ ▀▀▀ ▀░▀▀ ▀▀▀▀ ▀▀▀   ▒█▄▄█ ▀░░▀ ░░▀░░ ▀▀▀                     ")
    textFormat("                  ▀▒▓░▒▓▀▀█████░▒▓░▀▀▒░▒░▒░▀▀▀▀▀░▒▓░▒▓▀▀▀▒████▒▓▀░▒▓░▀▒░▒░▒░▒▀▒▓▒▀▒▀░▀▀▀▀█████▀▀▀▀▀▀▀▀                  ")
    textFormat("                   ░  ▒░ ╓████▀ ░ ▒░ ░ ▒ ▒░     ░ ▒▒░▒   ░████░▒ ░ ▒░ ░ ▒ ▒░░ ░▒  ░ ░    ^████▄    ,                    ")
    textFormat("                   ▐██,▄████▀     ░░ ░ ░ ▒        ░ ░    ░████░░   ░░ ░ ░ ▒ ░  ░  ░        '████▄,▄██                   ")
    textFormat("                   ███████`            ░            ░     ████ ░        ░ ░       ░           ███████                   ")
    textFormat("                  ▐███████▄                               ████                               ╓████████                  ")
    textFormat("                  █████▀▀^^                               ████                               ^^▀▀█████                  ")
    textFormat("                                                          ████                                                          ")                                                              
def boundingScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    textFormat("▓███████████████    ▓██████████████████████████████████████████████████████████████████████████████▌    ▓███████████████")
    textFormat("▓███         ▓██    ▓████                 ▓██▌                            ▓███                 ▓███▌    ▓██▌        ▓███")
    textFormat("▓████████████████████████████████████████████▌                            ▓█████████████████████████████████████████████")
    textFormat("             ▓██    ▓███▌                                                                      ▓███▌    ▓██▌            ")
    textFormat("▓███████████████████████▌                                                                      ▓████████████████████████")
    textFormat("▓█                                                                                                                    ▓█")
    textFormat("▓█                                                                                                                    ▓█")
    textFormat("▓█                                                                                                                    ▓█")
    textFormat("▓█                                                                                                                    ▓█")
    textFormat("▓█                                                                                                                    ▓█")
    textFormat("▓█                                                                                                                    ▓█")
    textFormat("▓█                                                                                                                    ▓█")
    textFormat("▓█                                                                                                                    ▓█")
    textFormat("▓█                                                                                                                    ▓█")
    textFormat("▓█                     for a better experience, scale your terminal to include the bounding box...                   ╟▓█")
    textFormat("▓█                                                                                                                   ▒▓▒")
    textFormat("╟█,                                                                                                                  ░▒░")
    textFormat("▓▒╟                                                                                                                  ░░░")
    textFormat("▓█▓                                                                                                                    ░")
    textFormat("▒▓▒                                                                                                                     ")
    textFormat("░▒░                                                                                                                     ")
    textFormat("░░                                                                                                                      ")
    textFormat(" ░                                                                                                                      \n")
    time.sleep(5)    
def menuInventory(mainItem):
    os.system('cls' if os.name == 'nt' else 'clear')
    mainitemParse(mainItem)
    textFormat(f"▓███████████████    ▓█████████████████████████████████████████████████████████████████████▌    ▓████████████████████████")
    textFormat(f"▓███         ▓██    ▓████                 ▓██▓▒▒▒▒▒▒▒▒▒╢╢╢╣╣╢╣▒▒▒▒▒▒▒╢╣╫╣▓███          ███▌    ▓██▌                 ▓███")
    textFormat(f"▓████████████████████████████████████████████▓╣▓█████████▀▀▀▀▀▀▀▀▀▀██▌╢▓▓▓██████████████████████████████████████████████")
    textFormat(f"             ▓██    ▓████╣╢╢╣▒▒▒▒╢▒╢▒▒▒▒▒▒▒╢▓▓╣▓█                  ▓█▌╣╫╣╢▒▒▒▒▒▒▒▒▒▒▒▒▒███▌    ▓██▌                     ")
    textFormat(f"▓████████████████████████╣╣╣╢╣╣▒╫╣╣╣╢▒▒▒▒╢╣╣▓▓╣▓█                  ▓█▌╣╫╣╢▒▒▒▒▒▒▒▒▒▒▒╢▒█████████████████████████████████")
    textFormat(f"▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬▓╣╬╬▓▓╣╣▓▓▓▓▓╬╬▓╣╣╫╬╬▓▓▓▒▓█                  ▓█▌╣╢▓▓╣╣╣╣╣╣╣╣╣╣╬╬╬█                              ▓█")
    textFormat(f"▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╣▓▓▓▓╢╢▓▓▒╫▓╣╢╣╢╢╣╣╣▒╢╣╣▒╢▓█                  ▓█▌╫▓╣▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                              ▓█")
    textFormat(f"▓█▓▓▓██▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀██▓╣╢╣╢╣╣╢╣╢╣╢╣╢╣▓█                  ▓█▓╣╣▒╢╢╢╢╢╢╢╣╣╣╣╣▒▒█                              ▓█")
    textFormat(f"▓█▓▓███                       ▓█▓╬╢╣╢▒▒▒▒▒▒╢╣╫╣▓█                  ▓█▓╣╫▒▒▒▒▒╢╢╢╣╢╢╣╢╣╣█                              ▓█")
    textFormat(f"▓█▓╫▓██                       ▓█▓╣▒▒▒▒▒╢╣╢╣╢╣╢╢▓█                  ▓█╣╣╣▒▒▒╣╢╣▒╢╢╢╢╢╢╢╢█                              ▓█")
    textFormat(f"▓█▓▓▓██                       ▓█▓▓▓╣╢╢╣╣╢▒╢╢╣╣╢▓█████████████████████╣╣▓▓▄▒╢╢╣╣╢╣╣╢╢╢╢╢█                              ▓█")
    textFormat(f"▓█▓▓▓██{line01:12s}▓█▓▓╢╢╣╣╣╣╢╣╢╢▓██████████████████████████████▓▓╣╢╢╢╢╢╢╢╣╢█                              ▓█")
    textFormat(f"▓█▓▓▓██{line02:12s}▓█▌▓╣╣╢╢╣╢╣▒╢╢██                         ▓█▓▓▓█▓▓╢╣╢╢╣╢╢╢█                              ▓█")
    textFormat(f"▓█▓╫▓██{line03:12s}▓█▓▓╣▓▓▓╣╣╣╬╣╣█▌                         ▓█▓▓▓▓▓█▓╣╣╣╢╢╢╢█                              ▓█")
    textFormat(f"▓█▓▓▓██{line04:12s}▓█▌▓╣▓╣╢╣╣╣╣╫▓█▌                         ▓██▓▓▓▓▓██▓╣╣╢╢╣█                              ▓█")
    textFormat(f"▓█▓▓▓██{line05:12s}▓█▌╣╣▓╣╣╣╣╣▓█▓█▌                         ▓█▓▓▓▓▓▓▓█▓╣╢╣╢╢█                              ▓█")
    textFormat(f"▓█▓▓▓██{line06:12s}▓█▌▓╣╢╣╣╣╣▓██▓█▌                         ▓█▓▓▓▓▓▓▓██▓╣╢╣╢█                              ▓█")
    textFormat(f"▓█▓╫▓██{line07:12s}▓█▌▓▓╣╣╢╣▒▓████▌                         ▓█▓▓▓▓▓▓▓▓█▓╣╣╢╣█                              ▓█")
    textFormat(f"▓█▓▓▓██{line08:12s}▓█▌▓╣▓▓▓╣▒██▓██▌                         ▓█▓▓▓▓█▓▓▓██▓╣╢╢█                              ▓█")
    textFormat(f"▓█▓▓▓██{line09:12s}▓█▌╣▓▓▓▓▓▒██▓██▌                         ▓█▓▓▓▓▓▓▓▓▓██▓╣╢█                              ▓█")
    textFormat(f"▓█▓▓▓██{line10:12s}▓█▌╣╣╣╢╢╢╫█▓▓██▌                         ▓█▓▓▓▓▓▓▓▓▓▓█▓╣╣█                              ▓█")
    textFormat(f"▓█▓▓▓██{line10:12s}▓█▌▓▓╣╣╣╫██▓▓██▌                         ▓███▓▓█▓▓▓▓▓▓█▓╣█                              ▓█")
    textFormat(f"▓█▓▓▓██{line11:12s}▓█▌▓▓╣╢╢██▓▓▓▓█▌                         ▓█▓███▓▓▓▓▓▓███▓█                              ▓█")
    textFormat(f"▓█▓▓▓██⌐                      ▓█▌▓▓▓╣▓█▓▓▓▓▓█▌                         ▓█▓▓▓██▓▓▓▓▓█████                              ▓█")
    textFormat(f"▓█▓▓▓██L                      ▓█▌▓▓▓██▓█▓▓▓▓█▌                         ▓█▓▓▓▓▓█▓▓▓▓▓▓▓▓█                              ▓█")
    textFormat(f"▓█▓▓▓▓█L                      ▓█▌▓████▓▓██▓██▌                         ▓█╣▓╣╢╫██▓▓▓▓▓▓▓█                              ▓█")
    textFormat(f"▓█▓▓█▓██████████████████████████▓▓████████▓██████████████████████████████╣╫▓▓╣▓███▓▓▓▓██                              ▓█")
    textFormat(f"▓███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████\n")
    
 
#                                                     ▓██████████████                                                     
# ▓█                                                  ▓█▓▓▓▓▓▓▓▓▓▓▓▓█                                                   ▓█
# ▓█▓▓█▓███╣╣╣████████████████████▓▓████████▓███████████▓▓▓▓▓▓▓▓▓▓▓▓███████╣╫▓▓╣▓███▓▓▓▓█████████████████████████╣████████
    
    
####             ##### 
#####   Items    #####
#####            #####
def mainitemParse(x):
    global line01, line02, line03, line04, line05, line06, line07, line08, line09, line10, line11, line12
    if x == "bow":
        line01 = "w                      "
        line02 = " ╙▒MNMN@@▄,,.          "
        line03 = "   └╖``└╙╨▓▓██▒        "
        line04 = "     '«,   └▒C     r   "
        line05 = "        \,  '▒Φ,,╓█▓   "
        line06 = "         `²┐   ^╙▒▓█▓  "
        line07 = "            ²┐    ▒▓█  "
        line08 = "              └┐  '▒█W "
        line09 = "                '\,└╠▌ "
        line10 = "                  `²▒▓ "
        line11 = "                     ╙▒"
        line12 = "                       "
    elif x == "sword":
        line01 = "██▌                    "
        line02 = "▀████                  "
        line03 = "  ▀████▄               "
        line04 = "    ╙████▌             "
        line05 = "      ╙█████,          "
        line06 = "        └▓▓█▓█▄        "
        line07 = "          '╫▓▓▓▓@,  ,▄▀"
        line08 = "            '╫▒░░░▀▌▀` "
        line09 = "              ╙▒░░░[   "
        line10 = "              ╓▒```▀Ñ, "
        line11 = "            .ê╙      ╙▒"
        line12 = "                      └"
    elif x == "shield":
        line01 = "                       "
        line02 = "   ▄▓▓▓▓▓╣▀▓╣▓▓▓φ      "
        line03 = "  ╟██▒▓╣▒▒▒░░░░░▓▓┐    "
        line04 = " ▐██▒█▓██▓▓░░░░░░╟▓▄   "
        line05 = " ██▒███▓▀█▓▓@g▓Ñ░▒▒▓▌  "
        line06 = "███▒███▓▒▒▀▓▓▒▒░░▒▒░▓▌ "
        line07 = "░▀███▀▓▓▒▒▒╣╙Ñ▒▒╢▒▒▒╠▓╦"
        line08 = "`╝▒▀███▒╣▒╣▒▒▒╢▒░║▒▒▒╟▒"
        line09 = "   ╨╣▒██▓▒╫╣▒╫▓▓▓╣▒▒░╣╣"
        line10 = "     ╙║░▀▓▓▌@▒▒▒▓▒▄▒▓▓▌"
        line11 = "        ╙@░▀╨▀▀▀▀▀▀▀▀▀ "
        line12 = "          ` ``````     "
    return line01, line02, line03, line04, line05, line06, line07, line08, line09, line10, line11, line12
def mainInventoryParse():
    print('Todo!')

if __name__ == "__main__":
    print('Check!')
    # sys.stdout.write("\033[F"*28)
    mainItem = "shield"
    menuInventory(mainItem)
    input("> ")
    # boundingScreen()
    time.sleep(5)
    
    