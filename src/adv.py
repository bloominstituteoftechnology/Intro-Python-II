from room import Room
from player import Player

# Declare all the rooms

room = {
    'winterfell':   Room("Winterfell", "Winterfell is the seat and the ancestral home of the royal House Stark. It is a very large castle located at the center of the North, from where the head of House Stark rules over his or her people."),

    'riverrun':    Room("Riverrun", "Riverrun is the seat of House Tully, which was once occupied by House Frey. It is a large castle located in the central-western part of the Riverlands."),

    'kings_landing': Room("Kings Landing", "King's Landing is the capital, and largest city, of the Seven Kingdoms. It enjoys a warm climate and life there is luxurious for those that can afford it."),

    'braavos':   Room("Braavos", "Braavos is one of the Free Cities located to the east of Westeros."),

    'casterly_rock': Room("Casterly Rock", "Casterly Rock is the ancestral stronghold of House Lannister. It is located on the Western coast of Westeros on a rocky promontory overlooking the Sunset Sea."),
}


# Link rooms together

room['winterfell'].n_to = room['riverrun']
room['riverrun'].s_to = room['winterfell']
room['riverrun'].n_to = room['kings_landing']
room['riverrun'].e_to = room['braavos']
room['kings_landing'].s_to = room['riverrun']
room['braavos'].w_to = room['riverrun']
# room['braavos'].n_to = room['casterly_rock']
# room['casterly_rock'].s_to = room['braavos']

#
# Main
#

# Make a new player object that is currently in the 'winterfell' room.
player1 = Player("John", "winterfell")

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
directions = ''

while directions != 'q':
    print(
        f"You, {player1.name} are currently in {room[player1.current_room].name} ")

    directions = input(
        "Where would you like to go? Use north/south/west/east for navigation")

    print(f"You have decided to go {directions} ")
