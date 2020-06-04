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

#
# Main
# Make a new player object that is currently in the 'outside' room.
player_name = input('\nwhat is your name?>')
player1 = Player(player_name, room['outside'])
print(f'\nwelcome {player1.name}!\n')

# create items and add these items to rooms.
bat = Item("Bat", "Barry Bonds home run bat")
bow = Item('Bow', "Robin Hoods bow!")
skateboard = Item('Skateboard', "Could be nice for transportation!")
yoyo = Item('YoYo', "Looks like a toy...")
guitar = Item('Guitar', 'Good for a Jam Session!')

room['outside'].items.append(bat)
room['foyer'].items.append(yoyo)
room['overlook'].items.append(bow)
room['narrow'].items.append(skateboard)
room['treasure'].items.append(guitar)


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
quiting = False

while not quiting:

    
    print(f'You are standing inside the {player1.current_room.name}. You look around and see {player1.current_room.description}\n')
    if len(player1.current_room.items) != 0:
        print('It looks like there is some item in the room! \n')
        for i in player1.current_room.items:
            print(f'{i.name}, {i.description}')
    
    if len(player1.inventory) != 0:
        print(f'You are currently holding: ')
        for i in player1.inventory:
            print(f'{i.name}')

    # what are the accepted commands for movement of quitting? If the user doesnt enter then we will
    # prompt for an accepted command. 

    accepted_commands = ['q', 'n', 'e', 's', 'w']
    
    # get the user command for the direction that they want to move, or if they want to quit. 
    command = input('\nWhat do you want to do? You can move n, s, e, or w. or you can quit, q?')
    command_split = command.split() # add the strip() in case the user accidently puts a space after their choice.
    command_verb = command_split[0].lower()
    command_item = command_split[-1].lower()

    if len(command_split) == 1 and command in accepted_commands:
        if command == 'n':
            if player1.current_room.n_to == None:
                print("\nThat way is blocked! Pick another direction!\n")
                player1.current_room
            else:
                player1.current_room = player1.current_room.n_to
        elif command == 's':
            if player1.current_room.s_to == None:
                print("\nThat way is blocked! Pick another direction!\n")
                player1.current_room
            else:
                player1.current_room = player1.current_room.s_to
        elif command == 'e':
            if player1.current_room.e_to == None:
                print("\nThat way is blocked! Pick another direction!\n")
                player1.current_room
            else:
                player1.current_room = player1.current_room.e_to
        elif command == 'w':
            if player1.current_room.w_to == None:
                print("\nThat way is blocked! Pick another direction!\n")
                player1.current_room
            else:
                player1.current_room = player1.current_room.w_to
        elif command == 'q':
            quiting = True
            print('\nThanks for playing!')

    elif len(command_split) == 2:
        if command_verb == 'get' or command_verb == 'take':
            # get the names of the list of items in the current room. 
            room_items = [i.name.lower() for i in player1.current_room.items]

            if command_item in room_items:
                for i in player1.current_room.items:
                    if i.name.lower() == command_item:
                        player1.current_room.items.remove(i)
                        player1.inventory.append(i)
                        i.get_item()
            else:
                print(f'{command_item} is not in this room.')

        elif command_verb == 'drop':
            inventory_items = [i.name.lower() for i in player1.inventory]

            if command_item in inventory_items:
                for i in player1.inventory:
                    if i.name.lower() == command_item:
                        player1.inventory.remove(i)
                        player1.current_room.items.append(i)
                        i.drop_item()
            else:
                print(f'you arent carrying {command_item}, nothing to drop.')
    
    else:
        print('\nThat isnt a valid command! Please input a valid command.')

# TODO 
# Make it so when command is pick up the item list will remove that item from the Item list in room
# WHen command is to pick up item the inventory will be updated with the item in Player class. 
# add logic to show what a player is carrying. 
# When the command is to Drop and item, it will be the opposite logic of the Pickup item logic. 
# i.e. item list will be appended in the Room Class, and the player inventory will be appended. 
