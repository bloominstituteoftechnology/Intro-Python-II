from room import Room
from player import Player
from item import Item
import sys
import time


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'den': Room("Strange Den", """You stumble into the den of a tall lanky eldritch creature.
It quickly grabs hold of you with it's fingers, each one matching the length of your arms.
As it draws you closer, everything fades to black."""),
}


# Link rooms together

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

# Make a new player object that is currently in the 'outside' room.
# Declare Player:
player = Player(
    current_room=room["outside"],
    name="David davis"
)
# Declare items
item = {
    'lighter': Item("lighter", "Half empty lighter", 1),
    'survival_knife': Item("survival knife", "Fishing knife", 2),
    'bloody dress': Item("bloody dress", "Bloody dress on the floor",  3),
    'torn note': Item("torn note", "A half of a note", 4),
    'old shoe': Item("old shoe", "Old dress shoe", 5),
}

# Add Items to Rooms:
room['outside'].addItem(item['survival_knife'])
room['foyer'].addItem(item['lighter'])
room['foyer'].addItem(item['bloody dress'])
room['overlook'].addItem(item['torn note'])
room['narrow'].addItem(item['old shoe'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Game Loop:
# Game Loop:
def game_loop():

    # Start The Game:
    game_running = True
    # Intro Text:
    print(f"\nYour name is {player.name}...\n")
    print("The sky thunders as it begins to pour.\nYou see an eerie cave entrance straight ahead of you.\nTo view your controls, enter 'C'.\n")
    # Create Input Variable:
    player_input = ""

    while game_running == True:

        # Quit Function:
        if player_input.lower() == "q":
            print("\nThank you for playing!")
            quit()

        # Boss Room Function:
        if player.current_room.name == "Strange Den":
            if item["survival_knife"] in player.items:
                print("You wake just as the creature is about to take a bite of your abdomen.\nYou take the knife you found earlier and thrust it into the side of its long narrow neck.\nYou quickly make your way back out of the cave as the beast wails in agony.\n\nCongratulations, you win!")
                game_running = False
                break
            else:
                print(f"G     O")
                time.sleep(.4)
                print(f"A     V")
                time.sleep(.4)
                print(f"M     E")
                time.sleep(.4)
                print(f"E     R\n")
                time.sleep(.4)
                print(f"Y     A")
                time.sleep(.4)
                print(f"O     R")
                time.sleep(.4)
                print(f"U     E\n")
                time.sleep(.4)
                print(f"D E A D")
                time.sleep(.4)
                print(f"! ! ! !")
                game_running = False
                break

        # Take Item Function:
        if player.current_room.items != []:
            for i in player.current_room.items:
                if player_input.lower() == f"take {i.name}":
                    player.takeItem(i)
                    player.current_room.removeItem(i)
        else:
            if "take" in player_input.lower(): 
                print("There is nothing to take.")

        # Drop Item Function:
        if player.items != []:
            for i in player.items:
                if player_input.lower() == f"drop {i.name}":
                    player.dropItem(i)
                    player.current_room.addItem(i)
        else:
            if "drop" in player_input:
                print("You don't have any items...")

        # Repeating Message:
        player_input =  str(input("What will you do?: "))

        # Controls Function:
        if player_input.lower() == 'c':
            print("\nControls:\n'W' = Up\n'A' = Left\n'S' = Down\n'D' = Right\n'Q' = Quit.\n'R' = Check Current Room\n'I' = Check Inventory.\n'take (item name)' = Take the specified item.\n'drop (item name)' = Drop the specified item.\n")
        
        # Check Room Function:
        elif player_input.lower() == 'r':
            print(f"\n{player}\n")

        # Check Inventory Function:
        elif player_input.lower() == 'i':
            if player.items != []:
                print("\nInventory:")
                for i in player.items:
                    print(i)
            else:
                print("\n    Your bag is empty...\n")

        # Direction Up Function:
        elif player_input.lower() == 'w':
            if player.current_room.n_to != []:
                player.current_room = player.current_room.n_to
                print(f"\nYou enter the {player.current_room.name}.\n{player.current_room.description}\n")
                if player.current_room.items != []:
                    for i in player.current_room.items:
                        print(f"    You see a ({i.name}) on the ground.\n")
            else:
                print("\nThere's nothing of interest in that direction.\n")

        # Direction Left Function:
        elif player_input.lower() == 'a':
            if player.current_room.w_to != []:
                player.current_room = player.current_room.w_to
                print(f"\nYou enter the {player.current_room.name}.\n{player.current_room.description}\n")
                if player.current_room.items != []:
                    for i in player.current_room.items:
                        print(f"    You see a ({i.name}) on the ground.\n")
            else:
                print("\nThere's nothing of interest in that direction.\n")

        # Direction Down Function:
        elif player_input.lower() == 's':
            if player.current_room.s_to != []:
                player.current_room = player.current_room.s_to
                print(f"\nYou enter the {player.current_room.name}.\n{player.current_room.description}\n")
                if player.current_room.items != []:
                    for i in player.current_room.items:
                        print(f"    You see a ({i.name}) on the ground.\n")
            else:
                print("\nThere's nothing of interest in that direction.\n")

        # Direction Right Function:
        elif player_input == 'd':
            if player.current_room.e_to != []:
                player.current_room = player.current_room.e_to
                print(f"\nYou enter the {player.current_room.name}.\n{player.current_room.description}\n")
                if player.current_room.items != []:
                    for i in player.current_room.items:
                        print(f"    You see a ({i.name}) on the ground.\n")
            else:
                print("\nThere's nothing of interest in that direction.\n")
    
    player_input =  str(input("\nTry again? y/n: "))
    if player_input == "y":
        print("Good Luck!")
        game_running = True
        player.current_room = room['outside']
        player.items = []
        room['outside'].addItem(item['survival_knife'])
        room['foyer'].addItem(item['lighter'])
        room['foyer'].addItem(item['bloody dress'])
        room['overlook'].addItem(item['torn note'])
        room['narrow'].addItem(item['old shoe'])
        game_loop()
    elif player_input == "n":
        print("Goodbye!")
        quit()

game_loop()
