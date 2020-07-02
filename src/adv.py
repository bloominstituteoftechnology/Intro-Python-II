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

# Creating items
items = {'sword': Item("Sword", "May be used to defend or kill!"),
         'coins': Item("Coins", "Survival has a price..."),
         'lantern': Item("Lantern", "Light up your way")
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

# Adding items to the rooms list.
room['outside'].items.append(items['lantern'])
room['narrow'].items.append(items['coins'])
room['overlook'].items.append(items['sword'])

#
# Main
#
name = input('\nWelcome to Adventure game, what shall we call you...? \n\n')

# Make a new player object that is currently in the 'outside' room.

player = Player(name, room['outside'])

print(f'\nWelcome {player.name} to the mysterious adventure lands... You are currently located {player.current_room} \n')
print(f'To play the game you may select a direction using N, S, E, W, and to quit the game use Q')

# Write a loop that:
while True:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.


    selection = input("\nEnter a direction or q to escape:")

    user_selection = selection.lower().split(" ")
    # print(user_selection)

    if len(user_selection) == 1:
        if selection == "q":
            print("We shall meet again...")
            break
        elif selection == "n" or selection == "s" or selection == "e" or selection == "w":
            player.move(selection)
            print(f'You are now located {player.current_room}\n This room contains: {player.current_room.list_items()}')
        elif selection == "i":
            player.print_items()
        else:
            print(f'{selection} is not a valid command, try using N, S, E, W... or Q to quit.\n')

    elif len(user_selection) == 2:
        if user_selection[0] in ["take", "get", "pickup"]:
            if items[user_selection[1]]:
                player.pickup_item(items[user_selection[1]])
                print('You have added a new item!')
                print(f'You are in {player.current_room} and you have: \n {player.current_room.list_items()}')
            else:
                print("That is not an item.\n")
        elif user_selection[0] == "drop":
            if items[user_selection[1]]:
                player.drop_item(items[user_selection[1]])
                print(f'You dropped an item!\n You have: {player.print_items()} \n You are {player.current_room} \n There are {player.current_room.list_items()} in this room.')
            else:
                print("That is not an item")
        else:
            print("Wrong command, Try again.. ")
    else:
        print("Wrong command, Try Again.")

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
