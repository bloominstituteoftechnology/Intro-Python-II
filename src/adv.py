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

flower = Item("Flower", "A pale pink rose.")
ruby = Item("Ruby", "A sparkling red gem. It seems old.")
dogtags = Item("Dogtags", "Looks like someone dropped their dogtag...who's 'L.J.C'?")


room['outside'].items = [flower, ruby, dogtags]

#
# Main
#

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

def adventure_game():
    name = input("What is your name?").capitalize()
    current_room = room["outside"]
    player = Player(name, current_room)

    while True:
        print("\n")
        print(player, "\n")
        print("You can go north, south, east, or west. \n")
        print("You can see what items are in the room by typing 'items'.\n")
        print("You can see what items you have by typing 'my items'\n")
        move = input("Which way do you go?\n")
        splitMove = move.split(" ");

        if len(splitMove) > 1:
            if move == 'my items':
                print(player.get_items())

            elif splitMove[0] == "get" or splitMove[0] == "take":
                # do blah
                player.take_item(splitMove[1])
            elif splitMove[0] == "drop":
                player.drop_item(splitMove[1])

        else:
            if move == 'items':
                print(player.current_room.get_items())
            elif move == 'n':
                try:
                    player.current_room = player.current_room.n_to
                except:
                    print("Whoops, looks like you can't go in that direction. \n")
            elif move == 'e':
                try:
                    player.current_room = player.current_room.e_to
                except:
                    print("Whoops, looks like you can't go in that direction. \n")
            elif move == 's':
                try:
                    player.current_room = player.current_room.s_to
                except:
                    print("Whoops, looks like you can't go in that direction. \n")
            elif move == 'w':
                try:
                    player.current_room = player.current_room.w_to
                except:
                    print("Whoops, looks like you can't go in that direction. \n")
            elif move == 'q':
                break
            else:
                print("That is not a valid input. Try again.")


if __name__ == '__main__':
    adventure_game()
