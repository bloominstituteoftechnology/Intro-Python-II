# from room import Room

from room import Room
from player import Player
from item import Utility
from item import Weapon


# Declare items in rooms
flashlight = Utility(
    "Flashlight", "This item can illuminate your surroundings", 2)
death_note = Weapon(
    "Death Note", "this item can kill anyone whose name is writting in the book", 100,
)
# Declare all the rooms

room = {
    "outside": Room(
        "Outside the Cave Entrance",
        "North of you, the cave mount beckons"

    ),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""", [flashlight, death_note]
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
    "basement": Room(
        "Basement Entry Way",
        """You've found the secret maze, and have entered the labyrinth
untold riches await you if you can find your way through. Light gleams from
the West, North, and East.""",
    ),
    "basement_dead_end_one": Room(
        "Dead End",
        """You've hit a dead end, 
        hope you remember where you came from""",
    ),
    "basement_room_one": Room("Room One", """Only a million more to go"""),
    "basement_room_two": Room(
        "Room Two", """Are you sure you're going the right way?"""
    ),
    "basement_dead_end_two": Room(
        "Dead End",
        """You hit a dead end,
        hope you remember where you came from""",
    ),
    "basement_room_three": Room(
        "Room Three",
        """Wellllll my weary traveller, the rooms get tougher from here
        let hope you can make it through""",
    ),
    "basement_dead_end_three": Room(
        "Dead End",
        """You hit a dead end,
        hope you remember where you came from""",
    ),
    "basement_room_four": Room(
        "Room Four",
        """well you are over half way to your treasure,
        think you will actually make it?""",
    ),
    "basement_room_five": Room(
        "Room Five",
        """Is that treasure that i smell?,
        no its only you!""",
    ),
    "basement_room_six": Room(
        "Room Six",
        """well you are almost there, this has been a fun game so far,
        once you finish, i have a surprise for you""",
    ),
    "basement_dead_end_five": Room(
        "Dead End",
        """You have reached yet another dead end,
        maybe a lied when i said you were almost done""",
    ),
    "basement_dead_end_six": Room(
        "Dead End",
        """You have reached yet another dead end,
        maybe a lied when i said you were almost done""",
    ),
    "basement_dead_end_seven": Room(
        "Dead End",
        """You have reached yet another dead end,
        maybe a lied when i said you were almost done""",
    ),
    "basement_room_seven": Room(
        "Room Seven",
        """well you finally got on the right path,
        but this is where things get tricky,
        dont get so caught up on room numbers""",
    ),
    "basement_room_eight": Room(
        "Room Eight",
        """it should would be nice if you could Teleport,
        from one room or dead end, to another room""",
    ),
    "basement_room_nine": Room("Room Nine", """T"""),
    "basement_room_ten": Room("Room Ten", """Z"""),
    "basement_room_eleven": Room("Room Eleven", """P"""),
    "basement_dead_end_eight": Room(
        "Dead End",
        """You hit a dead end,
        hope you remember where you came from""",
    ),
    "basement_dead_end_nine": Room(
        "Dead End",
        """You hit a dead end,
        hope you remember where you came from""",
    ),
    "basement_dead_end_ten": Room("Dead End", """E"""),
    "basement_room_twelve": Room("Room Twelve", """Welcome to room twelve"""),
    "basement_room_fifteen": Room("Room Fifteen", """lets finish this shall we"""),
    "basement_room_thirteen": Room("Room Thirteen", """almost done"""),
    "basement_room_fourteen": Room("Room Fourteen", """Done!"""),
}

# print(room['foyer'].room_items[0])
# # Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]
room["treasure"].basement_to = room["basement"]

# basement
room["basement"].w_to = room["basement_dead_end_one"]
room["basement_dead_end_one"].e_to = room["basement"]
room["basement"].n_to = room["basement_room_one"]
room["basement"].e_to = room["basement_room_two"]

# basement room one
room["basement_room_one"].n_to = room["basement_dead_end_two"]
room["basement_room_one"].w_to = room["basement_room_three"]
room["basement_room_one"].s_to = room["basement"]
room["basement_dead_end_two"].s_to = room["basement_room_one"]

# basement room two
room["basement_room_two"].n_to = room["basement_room_eight"]
room["basement_room_two"].w_to = room["basement"]
room["basement_room_two"].e_to = room["basement_room_seven"]

# basement room three
room["basement_room_three"].n_to = room["basement_dead_end_three"]
room["basement_room_three"].e_to = room["basement_room_one"]
room["basement_dead_end_three"].s_to = room["basement_room_three"]
room["basement_room_three"].w_to = room["basement_room_four"]

# basement room four
room["basement_room_four"].n_to = room["basement_room_five"]
room["basement_room_four"].e_to = room["basement_room_three"]

# basement room five
room["basement_room_five"].n_to = room["basement_room_six"]
room["basement_room_five"].s_to = room["basement_room_four"]

# basement room six
room["basement_room_six"].w_to = room["basement_dead_end_seven"]
room["basement_room_six"].n_to = room["basement_dead_end_five"]
room["basement_room_six"].s_to = room["basement_room_five"]
room["basement_dead_end_five"].s_to = room["basement_room_six"]
room["basement_room_six"].e_to = room["basement_dead_end_six"]
room["basement_dead_end_six"].w_to = room["basement_room_six"]
room["basement_dead_end_seven"].e_to = room["basement_room_six"]


# basement room seven
room["basement_room_seven"].n_to = room["basement_room_nine"]
room["basement_room_seven"].w_to = room["basement_room_two"]

# basement room eight
room["basement_room_eight"].s_to = room["basement_room_two"]
room["basement_room_eight"].n_to = room["basement_room_eleven"]
room["basement_room_eight"].w_to = room["basement_room_ten"]
room["basement_room_eight"].e_to = room["basement_room_nine"]

# basement room nine
room["basement_room_nine"].w_to = room["basement_room_eight"]
room["basement_room_nine"].s_to = room["basement_room_seven"]
room["basement_room_nine"].n_to = room["basement_room_twelve"]

# basement room ten
room["basement_room_ten"].e_to = room["basement_room_eight"]
room["basement_room_ten"].n_to = room["basement_dead_end_eight"]
room["basement_dead_end_eight"].s_to = room["basement_room_ten"]
room["basement_room_ten"].w_to = room["basement_dead_end_nine"]
room["basement_dead_end_nine"].e_to = room["basement_room_ten"]
room["basement_room_ten"].s_to = room["basement_dead_end_ten"]
room["basement_dead_end_ten"].n_to = room["basement_room_ten"]

# basement room twelve
room["basement_room_twelve"].s_to = room["basement_room_nine"]
room["basement_room_twelve"].w_to = room["basement_room_fifteen"]

# basement room fifteen
room["basement_room_fifteen"].e_to = room["basement_room_twelve"]
room["basement_room_fifteen"].s_to = room["basement_room_thirteen"]

# basement room thirteen
room["basement_room_thirteen"].n_to = room["basement_room_fifteen"]
room["basement_room_thirteen"].s_to = room["basement_room_eleven"]
room["basement_room_thirteen"].w_to = room["basement_room_fourteen"]

# basement room eleven
room["basement_room_eleven"].n_to = room["basement_room_fifteen"]
room["basement_room_eleven"].s_to = room["basement_room_eight"]

# basement room fourteen
room["basement_room_fourteen"].e_to = room["basement_room_thirteen"]
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input("what is your name? "), room["outside"], [])
# print(f'************************, this is player object {player}')
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


welcome = input(
    f"Welcome {player.player_name}, would you like to play a game? (yes/no): "
)
if welcome.lower().strip() == "yes":
    welcome = input(
        f"{player.player_name},  {player.current_room} please choose a direction: [n] north, [s] south, [e] east, [w] west: "
    )
    while True:
        options = ["n", "s", "e", "w", "basement"]
        choice = input("-> ").lower()
        if choice in options:
            player.movement(choice)
        elif choice == "basement":
            # if player.current_room == "treasure":
            player.take_secret_passage("choice")
        elif choice == "take":
            player.take_items()
        elif choice == 'show':
            player.show_items()
        elif choice == 'drop':
            player.drop_items()
        elif choice == "q":
            print("well that was short lived")
            exit()
        else:
            print("that was an invalid choice, please try again")

# else:
#     print("maybe another time")
