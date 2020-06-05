from room import Room
from player import Player
from item import Item

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

# Declare items
items = {
    'knife' : Item("knife", "Use the knife to stab your enemy."),
    'sword' : Item("sword", "If a knife is not enough, use a sword."),
    'hammer' : Item("hammer", "Impress you ennemy with your force"),
    'katana' : Item("katana", "Impress you enemy with your martial arts and this katana."),
    'rifle' : Item("rifle", "Use this long-barrelled firearm for accurate shooting.")
}

# Add items in the rooms
room['outside'].items = [items['knife']]
room['foyer'].items = [items['hammer']]
room['overlook'].items = [items['katana'], items['rifle']]
room['narrow'].items = [items['sword'], items['hammer']]
room['treasure'].items = [items['sword']]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_1 = Player("Player_1", room["outside"])

# Write a loop that:
while player_1.current_room:
    # * Prints the current room name
    print("\nYou are now in the room:\n",player_1.current_room.name)
    # * Prints the current description (the textwrap module might be useful here).
    print("\nDescription:\n",player_1.current_room.description)
    available_items = []
    for item in player_1.current_room.items:
        available_items.append(item.name)
    if len(available_items)==0:
        print("\nThere are no items in this room!")
        user_input = input("\nPress n/s/e/w to move to another room.\n \
Write 'Get <object>' or 'Take <object>' to select a weapon.\n \
Press 'q' to exit the game.\n").lower()
    else:
        print("\nItems in this room:")
        for item in available_items:
            print(item)
        # * Waits for user input and decides what to do.
        user_input = input("\nPress n/s/e/w to move to another room.\n \
Write 'Get <object>' or 'Take <object>' to select a weapon.\n \
Press 'q' to exit the game.\n").lower()
    if len(user_input.split())==1:
        # If the user enters a cardinal direction, attempt to move to the room there.
        if user_input == 'n':
            player_1.current_room = player_1.current_room.n_to
        elif user_input == 's':
            player_1.current_room = player_1.current_room.s_to
        elif user_input == 'e':
            player_1.current_room = player_1.current_room.e_to
        elif user_input == 'w':
            player_1.current_room = player_1.current_room.w_to
        # If the user enters "q", quit the game
        elif user_input == 'q':
            print("Have a nice day!")
            break
        if (user_input == 'i') | (user_input == "inventory"):
            print("Your inventory:")
            for item in player_1.inventory:
                print (item.name)
        # Print an error message if the movement isn't allowed.
        else:
            user_input = input("\nPress n/s/e/w to move to another room.\n \
Write 'Get <object>' or 'Take <object>' to select a weapon.\n \
Press 'q' to exit the game.\n").lower()
    elif len(user_input.split())==2:
        verb = user_input.split()[0]
        selected_item = user_input.split()[1]
        actions = ["get", "take", "drop"]
        if verb in actions:
            if (verb == "get") | (verb == "take"):
                if selected_item in available_items:
                    player_1.add_item(items[selected_item])                    
                    items[selected_item].on_take()
                    available_items = player_1.current_room.remove_item(items[selected_item])
                else:
                    print("The item selected is not in this room")
            elif verb == "drop":
                inventory_items = []
                for item in player_1.inventory:
                    inventory_items.append(item.name)
                if selected_item in inventory_items:
                    player_1.current_room.add_item(items[selected_item])
                    player_1.remove_item(items[selected_item])
                    items[selected_item].on_drop()
                else:
                    print("The item is not in your inventory")
            else:
                user_input = input("\nPress n/s/e/w to move to another room.\n \
Write 'Get <object>' or 'Take <object>' to select a weapon.\n \
Press 'q' to exit the game.\n").lower()
        else:
            user_input= input("Actions allowed: GET, TAKE, or DROP\n")
    else:
        user_input = input("\nPress n/s/e/w to move to another room.\n \
Write 'Get <object>' or 'Take <object>' to select a weapon.\n \
Press 'q' to exit the game.\n").lower()

        # Print an error if the player tries to move where there is no room
    if not player_1.current_room:
        user_input = input("\nYou fell out of the board. Game Over!")
