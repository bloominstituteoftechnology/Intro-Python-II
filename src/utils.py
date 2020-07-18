import os
import sys

def clear():
    os.system('cls')

    
def delete_last_line():
    "Use this function to delete the last line in the STDOUT"

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')

def space_word(word, n_spaces):
    spaces = (n_spaces - len(str(word))) * " "
    return str(word) + spaces