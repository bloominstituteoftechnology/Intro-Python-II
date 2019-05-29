from item import Food, LightSource
import random
from room import Room
from player import Player
from textwrap import wrap

# Create some items
item = {
    'bread': Food("Bread", "Four slices of bread", 300), 'cheese': Food("Cheese", "A cheddar wheel", 1000),
    'chicken': Food("Chicken", "Grilled chicken breast", 300), 'apples': Food("Apples", "Three green apples", 150),
    'lamp': LightSource("Lamp", "An oil-burning lamp")
}

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


for rm in room:
    if rm != 'outside':
        if random() > 0.5:
            room[rm].items = [random.choice(item.keys())]

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
#
def room_is(current_room):
    print("\nCurrent room is", current_room.name)

def room_description(current_room):
    print(wrap(current_room.description, width=70))

def room_item(current_room):
    if room.items == []:
        print("Room has no items in it")
    else:
        print("Room has", items[0].description, "in it")

# Make a new player object that is currently in the 'outside' room.
player_one = Player('player_one', 'outside', 0)


def create_game():
    moves = 0
    while True:
        if moves == 0:
            current_room = room[player_one.current_room]
            room_is(current_room)
            room_description(current_room)
            room_item(current_room)
        elif moves > 0:
            current_room = player_one.current_room
                
        instruction_text = """\nEnter 'n' to go north, 's' to go south, 'e' to go east, 'w' to go west, or 'q' to quit- """
        user_choice = input(instruction_text)
        
        if user_choice != 'q':
            next_move = current_room.move_further(user_choice)
            # if user_choice is in the directions instruction text, and if from the current room there is a room
            # in that direction, this returns that room and increments the moves counter
            if isinstance(next_move, Room):
                player_one.current_room = next_move
                moves += 1
                room_is(player_one.current_room)
                room_description(player_one.current_room)
                room_item(player_one.current_room)
            # if either of those conditions fail, then instead of a room returning from the Room class method move_further,
            # an error message returns saying no way forward by user_choice from current room
            else:
                print(next_move)
        
        elif user_choice == 'q':
            break
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

if __name__ == '__main__':
    create_game()