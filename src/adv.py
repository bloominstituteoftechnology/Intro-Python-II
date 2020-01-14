from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     'nothing',
                     'nothing',
                     'nothing',
                     'nothing'
                     ),


    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     'nothing',
                     'nothing',
                     'nothing',
                     'nothing'
                     ),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     'nothing',
                     'nothing',
                     'nothing',
                     'nothing'
                     ),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", 'nothing',
                     'nothing',
                     'nothing',
                     'nothing'
                     ),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", 'nothing',
                     'nothing',
                     'nothing',
                     'nothing'
                     ),
}
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Main
current_player = Player("Brandon", "outside")
current_room_in = current_player.current_room

print("Welcome to your adventure!")
print(room[current_room_in].name)
print(room[current_room_in].description)
msg = str(input(
    "what direction will you go? Please press n for north s for south w for west or e for east or q for quit.\n"))

current_player = Player("Brandon", "outside")
current_room_in = ""
# Write a loop that:
current_player.current_room_in = current_player.current_room


while not msg == "q":
    # * Prints the current description
    if msg == "n":
        current_room_in = room[current_player.current_room].n_to.name
        current_player.current_room = room[current_player.current_room].n_to.name.lower(
        )
        print(current_room_in)
    # Print an error message if the movement isn't allowed
    msg = str(input(
        "what direction will you go? Please press n for north s for south w for west or e for east or q for quit.\n"))
