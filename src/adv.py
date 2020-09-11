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

    'kitchen': Room("The Kitchen", """You check out some refreshments and grab
a quick bite to eat before moving along. """),
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
room['kitchen'].w_to = room['overlook']

# MVP 2 - Add items to rooms

room['outside'].add_item('bricks')
room['foyer'].add_item('mirror')
room['foyer'].add_item('envelope opener')
room['foyer'].add_item('matches')
room['overlook'].add_item('magic wand')
room['narrow'].add_item('sword')
room['narrow'].add_item('one ring to rule them all')
room['treasure'].add_item('stick')
room['kitchen'].add_item('butcher knife')

# Make a new player object that is currently in the 'outside' room.

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
#
# Thank you for the inspiration Anthony! I added in a place to add your name too!

name = input("Welcome to my castle adventurer! Please, tell me your name. ")

player = Player(name, room['outside'])

print(f" Welcome, {player.name}! Let's explore!")


def display_room_description(room):
    end_game = False
    print(f'You are here: {room.name}.')
    print(room.description)
    print("""Enter a direction (n, s, e, or w) to travel through the castle. 
    Use i to look for items that may be hidden in each room. """)

display_room_description(player.current_room)

end_game = False


def item(player, item):
    end_game = False
    interface = input("There is an item in here. You can 'g' get or 'd' drop it. ")

    if interface == 'g':
        player.inventory.append(item)
        print("This new tool could be useful!")
        player.current_room.item_taken(item)
        game_input(player)
    elif interface == 'd':
        print("Moving on..")
        game_input(player)
    else:
        print("Does not compute, try again. ")


def game_input(command, player):
    end_game = False
    if command == 'n':
        if player.current_room.n_to != None:
            player.current_room = player.current_room.n_to
            display_room_description(player.current_room)
        else:
            print("Sorry, can't go this way!")
    elif command == 's':
        if player.current_room.s_to != None:
            player.current_room = player.current_room.s_to
            display_room_description(player.current_room)
        else:
            print("Nope, try again!")
    elif command == 'e':
        if player.current_room.e_to != None:
            player.current_room = player.current_room.e_to
            display_room_description(player.current_room)
        else:
            print("Are you lost? This isn't the way")
    elif command == 'w':
        if player.current_room.w_to != None:
            player.current_room = player.current_room.w_to
            display_room_description(player.current_room)
        else:
            print("Made a wrong turn, try again!")
    elif command == 'i':
        print(player.hunt_for_items())
        object = player.hunt_for_items()

        if player.hunt_for_items != "Nothing here, better keep looking":
            item(player, object)
        else:
            game_input(player)
    elif command == 'q':
        end_game = True
    else:
        print('Please enter a valid direction')
    return end_game

while end_game == False:
    end_game = game_input(str(input()), player)

print('Thanks for playing!')
