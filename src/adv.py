from room import Room
from player import Player

# Declare all the rooms
room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
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

# Add room items
room['outside'].room_items.append("sword")
room['foyer'].room_items.append('coins')
room['overlook'].room_items.append('ruby')
room['narrow'].room_items.append('key')
room['treasure'].room_items.append('treasure box')

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Conner", room['outside'])

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

print('Welcome to the adventure game!')


def display_current_room_info():
    print('========== ROOM INFO ==========')
    print(f'You\'re character is currently located in the room named "{player.current_room}".')
    print(f'The room description says: "{player.current_room.room_description}"')
    print(f'The items available in this room are: {[item for item in player.current_room.room_items]}')
    print('========== END ROOM INFO ==========')


def user_choose_action(action):
    action = action.lower()
    if action == "move" or action == "1":
        return "1"
    elif action == "take items" or action == "2":
        for item in player.current_room.room_items:
            player.add_item_to_inventory(item)
        player.current_room.room_items = []
        return "2"
    elif action == "show inventory" or action == "3":
        return "3"
    elif action == "show room info" or action == "4":
        return "4"
    elif action == "exit" or action == "5":
        return "5"
    else:
        return "incorrect action"


display_current_room_info()

while True:
    user_action = input("Please choose an action \n 1. Move \n 2. Take Items \n 3. Show Inventory \n 4. Show Room Info "
                        "\n 5. Exit \n Action: ")
    user_chosen_action = user_choose_action(user_action)

    if user_chosen_action == "incorrect action":
        print("Incorrect action, please try again.")
    elif user_chosen_action == "1":
        user_chosen_direction = input("Please enter a direction to move in (n, s, w, e): ")
        if user_chosen_direction == "n" and player.current_room.n_to != "":
            player.current_room = player.current_room.n_to
        elif user_chosen_direction == 's' and player.current_room.s_to != "":
            player.current_room = player.current_room.s_to
        elif user_chosen_direction == 'e' and player.current_room.e_to != "":
            player.current_room = player.current_room.e_to
        elif user_chosen_direction == 'w' and player.current_room.w_to != "":
            player.current_room = player.current_room.w_to
        else:
            print("Incorrect movement, try a different direction")

        display_current_room_info()
        continue
    elif user_chosen_action == "2":
        print("==========")
        print(f'Items have been added to your inventory: {player.inventory}')
        print("==========")
    elif user_chosen_action == "3":
        print("========== USER ITEMS ==========")
        print(f'Items: {[item for item in player.inventory]}')
        print("========== END USER ITEMS ==========")
    elif user_chosen_action == "4":
        display_current_room_info()
    elif user_chosen_action == "5":
        print("Exiting!")
        break
