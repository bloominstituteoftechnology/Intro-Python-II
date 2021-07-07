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

#
# Main
#
def adv_game():
    # Make a new player object that is currently in the 'outside' room.
    player = Player("Mari", room["outside"])
    print(player)

    def try_direction(direction, location):
        attribute = direction + "_to"

        if hasattr(location, attribute):
            return getattr(location, attribute)
        else:
            print("Wrong way!")
            return location

    # Write a loop that:
    #
    while True:
        # * Prints the current room name
        print(player.location.name)
        # * Prints the current description (the textwrap module might be useful here).
        print(player.location.description)
        # * Displays Player Items
        if len(player.location.items):
            print(f"The items found in this room are: {player.location.items}")
        else:
            print("There is nothing to be found here.")
        # * Waits for user input and decides what to do.
        s = input("Choose a command: \n> ").lower().split()

        # * Checks to see if one or two word command
        if len(s) == 1:
            # grab the first character of the first word
            s = s[0][0]
            if s == 'q':
                print("You quit")
                break

            if s == 'i' or s[0] == "inventory":
                if player.inventory == []:
                    print("Your inventory is empty.")
                else:
                    print(f"your inventory has: {player.inventory}")

            player.location = try_direction(s, player.location)
        elif len(s) == 2:
            # user passed us a two-word command
            if s[0] == "get":
                item_count = len(player.location.items)
                for i, item in enumerate(player.location.items):
                    if item.lower() == s[1]:
                        player.inventory.append(player.location.items.pop(i))
                        print(player.inventory)
            elif s[0] == "drop":
                item_count = len(player.inventory)
                for i, item in enumerate(player.inventory):
                    if item.lower() == s[1]:
                        player.location.items.append(player.inventory.pop(i))
                        print(f"Your inventory has: {player.inventory}")

        else:
            print("I don't understand that")
            continue

if __name__ == '__main__':
    adv_game()