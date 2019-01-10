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
    player = Player("Bob", room['outside'])
    print(player)
    #player = Player("Bob", "outside")
    #roomKey = player.location
    #roomName = room[player.location].name
    #roomDesc = room[player.location].description

    def try_direction(direction, location):
        attribute = direction + '_to'

        # see if the inputted direction is one we can move to
        if hasattr(location, attribute):
            return getattr(location, attribute)
        else:
            print("You can't go that way")
            return location
    # Write a loop that:
    #
    while True:
        # * Prints the current room name
        print(player.location.name)
        # * Prints the current description (the textwrap module might be useful here).
        print(player.location.description)
        # * Waits for user input and decides what to do.
        s = input("\n").lower()[0]

        # s = input("\n> ").lower().split()
        #check to see if one  or two word command
        # if len(s) == 1:
            #the user passed us a direction
            # grab the first character of the first word
            # s = s[0][0]
            #if s == 'q':
            #print("You quit")
            #break

            #player.location = try_direction(s, player.location)
        # elif len(s) ==2:
            #user passed us a two-word command
            # first_word = s[0]
            # second_word = s[1]

            # if first_word in ['get', 'drop']:

        # else:
            #print("I don't understand that")
            #continue

        # If the user enters "q", quit the game.
        if s == 'q':
            print("You quit")
            break

        player.location = try_direction(s, player.location)

        """
        North, South, East, West, north, south, east, west
        N, S, E, W, n, s, e, w
        """
            
        # If the user enters a cardinal direction, attempt to move to the room there.
        

if __name__ == '__main__':
    adv_game()
