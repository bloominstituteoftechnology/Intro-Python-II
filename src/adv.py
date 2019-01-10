from room import Room
from player import Player

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
#
def adv_game():
    # Make a new player object that is currently in the 'outside' room.
    player = Player("Bob", "outside")
    roomKey = player.location
    roomName = room[player.location].name
    roomDesc = room[player.location].description
    # Write a loop that:
    #
    while True:
        # * Prints the current room name
        print(roomName)
        # * Prints the current description (the textwrap module might be useful here).
        print(roomDesc)
        # * Waits for user input and decides what to do.
        userInput = input("Pick a direction to move: n, s, e, or w: ")
        # If the user enters "q", quit the game.
        if userInput == "q":
            print("You quit")
            break
        # If the user enters a cardinal direction, attempt to move to the room there.
        elif roomKey == 'outside':
            if userInput == 'n':
                roomName = room[roomKey].n_to.name
                roomDesc = room[roomKey].n_to.description
                roomKey = [key for key in room.keys() if key == 'foyer'][0]
        elif roomKey == 'foyer':
            if userInput == 's':
                roomName = room[roomKey].s_to.name
                roomDesc = room[roomKey].s_to.description
                roomKey = [key for key in room.keys() if key == 'outside'][0]
            elif userInput == 'n':
                roomName = room[roomKey].n_to.name
                roomDesc = room[roomKey].n_to.description
                roomKey = [key for key in room.keys() if key == 'overlook'][0]
            elif userInput == 'e':
                roomName = room[roomKey].e_to.name
                roomDesc = room[roomKey].e_to.description
                roomKey = [key for key in room.keys() if key == 'narrow'][0]
        elif roomKey == 'overlook':
            if userInput == 's':
                roomName = room[roomKey].s_to.name
                roomDesc = room[roomKey].s_to.description
                roomKey = [key for key in room.keys() if key == 'foyer'][0]
        elif roomKey == 'narrow':
            if userInput == 'w':
                roomName = room[roomKey].w_to.name
                roomDesc = room[roomKey].w_to.description
                roomKey = [key for key in room.keys() if key == 'foyer'][0]
            elif userInput == 'n':
                roomName = room[roomKey].n_to.name
                roomDesc = room[roomKey].n_to.description
                roomKey = [key for key in room.keys() if key == 'treasure'][0]
        elif roomKey == 'treasure':
            if userInput == 's':
                roomName = room[roomKey].s_to.name
                roomDesc = room[roomKey].s_to.description
                roomKey = [key for key in room.keys() if key == 'narrow'][0]
        else:
            # Print an error message if the movement isn't allowed.
            print("Cannot move that direction, try another: ")
            continue

if __name__ == '__main__':
    adv_game()
