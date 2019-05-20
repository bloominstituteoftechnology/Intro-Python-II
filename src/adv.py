from room import Room
from player import Player
import items
import winsound

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", """==============================================
North of you, the cave mount beckons
=============================================="""),

    'foyer':    Room("Foyer", """==============================================
Dim light filters in from the south. Dusty
passages run north, east and west. You are
greeted by a pile of gold on the ground.
==============================================""", ['gold']),

    'overlook': Room("Grand Overlook", """==============================================
A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.
On the edge lies a forgotten axe
==============================================""", ['axe']),

    'narrow':   Room("Narrow Passage", """==============================================
The narrow passage bends here from west
to north. The smell of mold permeates the air.
In all the decay you discover a sword.
==============================================""", ['sword']),

    'treasure': Room("Treasure Chamber", """==============================================
You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.
=============================================="""),

'corridor':  Room("The Corridor", """==============================================
Ancient Passage to the Unknown. It is up to you
to decide to venture on.
=============================================="""),

    'pass':    Room("The Deserted Pass", """==============================================
A barely visible trail runs from the north and south.
You can see what appears to be a forest to the south.
You also spot a diamond on the ground.
==============================================""", ['diamond']),

    'trail': Room("Forest Trail", """==============================================
You are surrounded by trees and creatures of the night.
You spot something shiny and identify it as a dagger.
Trail runs north, south and east.
==============================================""", ['dagger']),

    'cave':   Room("Dead Mans Cave", """==============================================
You just passed throught the mouth of a large cave.
It is too dark to continue. You do find a shield 
leaning against a stone. 
==============================================""", ['Shield']),

    'watch': Room("Fiery Watch", """==============================================
Out of the trees and into the fire. It is much too
risky to go on this way. Go back...
=============================================="""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].w_to = room['corridor']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['corridor'].e_to = room['foyer']
room['corridor'].s_to = room['pass']
room['pass'].s_to = room['trail']
room['pass'].n_to = room['corridor']
room['trail'].n_to = room['pass']
room['trail'].s_to = room['cave']
room['trail'].e_to = room['watch']
room['cave'].n_to = room['trail']
room['watch'].w_to = room['trail']
#
# Main
#
# Make a new player object that is currently in the 'outside' room.
player_one = Player('willie', room['outside'])    
# Write a loop that:
#
# * Prints the current room name
import os
os.system('cls')
print("\033[1;36;40m")
print(player_one.room.name)
# * Prints the current description (the textwrap module might be useful here).
print(player_one.room.description)
# * Waits for user input and decides what to do.
print("\033[1;33;40m")
player_one.play_audio("music5.wav")
print("Enter: get item_name or: drop item_name...")
direction = input("Select the direction to go: n,s,e,w or q to quit: ").strip()

while direction != 'q':
  try:
    
    commands = direction.split()
    if len(commands) == 1: 
        if direction == 'n':
            player_one.play_audio("scorpwalk1.wav") 
            player_one.room = player_one.room.n_to 
            print("\033[1;36;40m")  
            print(player_one.room)
        elif direction == 's':
            player_one.play_audio("scorpwalk2.wav") 
            player_one.room = player_one.room.s_to 
            print("\033[1;36;40m")  
            print(player_one.room)    
        elif direction == 'e':
            player_one.play_audio("scorpwalk1.wav")
            player_one.room = player_one.room.e_to 
            print("\033[1;36;40m")  
            print(player_one.room)
        elif direction == 'w':
            player_one.play_audio("scorpwalk2.wav")
            player_one.room = player_one.room.w_to      
            print("\033[1;36;40m")  
            print(player_one.room)
        elif direction == 'i':
            print("\033[1;31;40m")
            player_one.print_inventory()   
            player_one.play_audio("01_opentreasure.wav")
        else:
            print("\033[1;35;40m Not a valid entry, please select n,s,e,w, i for inventory or q to quit:\n ")
    elif len(commands) == 2:
        #parse out words
        if commands[0] == "get":
            #check if anything is in room inventory
            for i in player_one.room.inventory:
                if i == commands[1]:
                    player_one.inventory.append(i)   
                    player_one.room.inventory.pop()
                    print("\033[1;31;40m")
                    print("You picked up " + i)
                    print("Inventory is:")
                    player_one.print_inventory() 
                    player_one.play_audio("01_Coin.wav")
                else:
                    print("Please select a valid item")
            
        elif commands[0] == "drop":
            for i in player_one.inventory:
                if i == commands[1]:
                    player_one.room.inventory.append(i)   
                    print("\033[1;31;40m")
                    print("You dropped " + i)
                    player_one.inventory.pop()
                    print("Inventory is now: ")
                    player_one.print_inventory() 
                    player_one.play_audio("02_Coin.wav")
                else:
                    print("item not found")    
        else:
            print("Please only enter valid commands")
    else:
      print("Please use only two word commands, 'get item_name' or 'drop item_name' ")

      
  except:
    player_one.play_audio("mismatch.wav")
    print("\033[1;35;40m Cant go in that direction\n")  
  
  print("\033[1;33;40m")
  direction = input("Select the direction to go: n,s,e,w i for inventory or q to quit: ")
  print("\n")


os.system('cls')
print("\033[1;31;44m \n\n\nThanks for playing...\n")  
print("\033[0;37;40m")
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
