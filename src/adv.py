from room import Room

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


def show_welcome_message():
    welcome_message = "Welcome to the Cave of Despair!"
    print(welcome_message)

# Prints the current room name
# Prints the current description (the textwrap module might be useful here).


def current_room(player, room):
    print(f"{player.name} has entered the {room.name}. {room.description}")


# Waits for user input and decides what to do.
def get_user_input():
    choice = input(
        "Pick a direction: [n] North  [e] East  [s] South  [w] West  [q] Give up now!\n")
    return choice_options[choice]

# If the user enters a cardinal direction, attempt to move to the room there.


def switch_rooms():
    pass

# If the user enters "q", quit the game.


def quit_game():
    print("Lost? Many have tried and failed!  Better luck next time.")

# Print an error message if the movement isn't allowed.


def error():
    pass


# Make a new player object that is currently in the 'outside' room.
new_player = {
    "name": "Bilbo",
    "current_room": 'outside'
}

choice_options = {
    "n": "North",
    "e": "East",
    "s": "South",
    "w": "West",
    "q": "Give up now!"
}

# Start of Game
show_welcome_message()

# Starting choice
user_input = get_user_input()

while user_input != "q":
    current_room(new_player, current_room)
    user_input = get_user_input()

# Quit game if user exits game loop
quit_game()
