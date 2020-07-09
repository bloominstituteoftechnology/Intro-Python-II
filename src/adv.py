# Execute this file to play adventure game!

import textwrap
from room import Room
from player import Player
from item import Item

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("sword", "long sharp sword crafted by orcs"), Item("potion", "potion granting the ability to become invisible")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("talisman", "magical artifact granting the owner psychic abilities"), Item("spear", "10 foot long spear")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("relic", "magical artifact granting the owner 10 ruppees per day"), Item("potion", "heals 100 percent of all maladies")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("turkey leg", "food that grants 100 percent healing"), Item("rope", "use this to climb down cliff")]),
    
    'dungeon':  Room("Dark Dungeon", """The cold dang air smells of sweat and evil! You might want to get out of here quick.""", [Item("vampire", "this vampire wants to be your friend")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("rubies", "treasure!"), Item("gold", "treasure!"), Item("emeralds", "treasure!")]),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['narrow'].s_to = room['dungeon']
room['dungeon'].n_to = room['narrow']
room['treasure'].s_to = room['narrow']

def adventure_awaits():

    new_name = input("\nEnter Your NAME! Adventure Awaits...\n-->  ")
    current_player = Player(new_name, room["outside"], [])
    playing = True
    print(
        f"\nHello {current_player.name}!\nExplore rooms and obtain treasure! \nAdventure Awaits!\n")

    while (playing):
        wrapper = textwrap.TextWrapper(width=70)
        room_description = wrapper.wrap(
            text=current_player.room.description)

        # show heros current room and room description
        input("Enter Anything to Continue...\n -->  ")
        print("\n----------------------------")
        print("----------------------------")
        print(f"\nCurrent Room: \n{current_player.room.name}\n")
        print("Room Description: ")
        for every_line in room_description:
            print(every_line)
        print(" ")
        print("Items Available:")
        for count, item in enumerate(current_player.room.items):
            print(f"{item.name} --- {item.description}")
        print("\n----------------------------")
        print("----------------------------")

        # waits for user input to decide what to do next
        action = input(
            "\n\nWhat shall the hero do next??? \ntype 'help' for a hint! \n-->  ")
        num_args = action.split()

        # loop logic here
        if (len(num_args) == 1):
            if (action == "n"):
                if (current_player.room.n_to == None):
                    print("That's not possible.")
                else:
                    current_player.room = current_player.room.n_to
            elif (action == "s"):
                if (current_player.room.s_to == None):
                    print("That's not possible.")
                else:
                    current_player.room = current_player.room.s_to
            elif (action == "e"):
                if (current_player.room.e_to == None):
                    print("That's not possible.")
                else:
                    current_player.room = current_player.room.e_to
            elif (action == "w"):
                if (current_player.room.w_to == None):
                    print("That's not possible.")
                else:
                    current_player.room = current_player.room.w_to
            elif (action == "q"):
                playing = False
            elif (action == "i"):
                print(f"{current_player.name} items:")
                for each_item in current_player.inventory:
                    print(f"{each_item.name} --- {each_item.description}")
            else:
                wrapper = textwrap.TextWrapper(width=70)
                error = wrapper.wrap(text="The game takes a one letter command, or a two word command. For a one letter command, possible commands include: n = north, s = south, w = west, e = east, i = display player inventory, q = quit game. For two letter commands you can do the following: take 'item-name', get 'item-name' or drop 'item-name' to add or remove items from player inventory and rooms.")
                for each_line in error:
                    print(each_line)

        if (len(num_args) == 2):
            if (num_args[0] == "take" or num_args[0] == "get"):
                item_present = False
                for count, item in enumerate(current_player.room.items):
                    if (num_args[1] == item.name):
                        item_present = True
                        current_player.inventory.append(
                            current_player.room.items[count])
                        current_player.room.items[count].on_take()
                        current_player.room.items.remove(
                            current_player.room.items[count])
                    else:
                        pass
                if (item_present):
                    pass
                else:
                    print("that item is not in the room!")
            elif (num_args[0] == "drop"):
                item_present = False
                for count, item in enumerate(current_player.inventory):
                    if (num_args[1] == item.name):
                        item_present = True
                        current_player.room.items.append(
                            current_player.inventory[count])
                        current_player.inventory[count].on_drop()
                        current_player.inventory.remove(
                            current_player.inventory[count])
                    else:
                        pass
                if (item_present):
                    pass
                else:
                    print("that item is not in the room!")
            else:
                wrapper = textwrap.TextWrapper(width=70)
                error = wrapper.wrap(text="When entering more then one character, two words are expected. The only admissable first words are 'take', 'get', and 'drop' and the only admissiable second words are 'item-name' in order to remove or add items to player inventory For example: 'take sword', 'drop gold', or 'get potion'. When entering one character please enter a direction: n, s, e, w. etc. Type 'q' to quit. Type 'i' for player inventory. Type 'take item-name' or 'drop item-name' to add or remove ITEM from player inventory.")
                for each_line in error:
                    print(each_line)


adventure_awaits()
