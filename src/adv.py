from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", Item('sword', 'cuts through anything')),

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

print(type(room))

#
# Main
#
name = input("\nPlayer Name:")

# Make a new player object that is currently in the 'outside' room.
new_player = Player(name, room['outside'])

print(room['outside'].__dict__)
print(room['outside'].items)
# print()
# Write a loop that:
user_is_playing = True     

directions = ['n', 's', 'e', 'w']

while user_is_playing:

    # * Prints the current room name
    print(f'\n{new_player.location.name}\n')
  
    # * Prints the current description (the textwrap module might be useful here).
    print(f'{new_player.location.description}\n')

    # * Waits for user input and decides what to do.
    direction = input(f"Which direction do you want to go {new_player.name}?")

    # quit the game if direction is q
    if direction == 'q':
        break

    # if direction has ['n', 'w', 'e', 's'] then only update the location 
    # move to that location
    elif direction in directions:
        
        # call move method from player to update the location
        new_player.move(direction)
        if new_player.location is None:
            print('Try again')

        # breakpoint()
        # print(new_player.location)
        # print(direction)
    elif direction != directions:
        print("Try Again")

    # a = input("which direction do you want to go?")
    # if a == "n" and new_player.location is not None:
    #     new_player.location = new_player.location.n_to
    # elif a == "s":
    #     new_player.location = new_player.location.s_to
    # elif a == "e":
    #     new_player.location = new_player.location.e_to
    # elif a == "w":
    #     new_player.location = new_player.location.w_to
  
    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
    # elif a == 'q' or 'Q':
    #     break
    # elif a != ['n', 's', 'e', 'w', 'q', 'Q']:
    #     print("This direction is not valid, please enter the right direction.")
