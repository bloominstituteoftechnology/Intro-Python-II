# from room import Room

# Declare all the rooms
#
# room = {
#     'outside':  Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons"),
#
#     'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east."""),
#
#     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm."""),
#
#     'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air."""),
#
#     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south."""),
# }


# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

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

from player import Player
from room import Room
from item import Item

# DECLARE ITEMS
item_hat = Item("Hat", "A very very fancy hat")
item_bat = Item("Bat", "An unusually swole bat")
item_rat = Item("Rate", "This is NOT a bat, there are probably others.")
item_rope = Item("Rope", "For adventuring")
item_pole = Item("Pole", "You cannot adventure without a 10 foot pole")

# DECLARE ROOMS
room_outside = Room(
    "Outside Cave Entrance",
    "North of you, the cave mount beckons",
    {item_hat: 1},
)
room_foyer = Room(
    "Foyer",
    """Dim light filters in from the south. Dusty passages run north and east.""",
    {item_rat: 1},
)
room_overlook = Room(
    "Grand Overlook",
    """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    {item_rope: 1},
)
room_narrow = Room(
    "Narrow Passage",
    """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
    {item_bat: 1}
)
room_treasure = Room(
    "Treasure Chamber",
    """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    {item_pole: 1}
)

# Link rooms together
room_outside.branches.update({
    "north": room_foyer,
})
room_foyer.branches.update({
    "north": room_overlook,
    "east": room_narrow,
    "south": room_outside
})
room_overlook.branches.update({
    "south": room_foyer
})
room_narrow.branches.update({
    "south": room_foyer
})
room_treasure.branches.update({
    "south": room_narrow,
})

# Main
if __name__ == '__main__':

    # Make a new player object that is currently in the 'outside' rooms_dict.
    name = input("Please input name: ")
    player = Player(name, room_outside)

    # Write a loop that:
    #
    direction = None
    cur_room = None
    print("You must go find the treasure because of reasons!")
    input("Press any key to begin: ")

    # While game is playing
    while direction != "q":
        # If player has moved
        if cur_room != player.current_room:
            # Current rooms_dict updates to players new location
            cur_room = player.current_room

        # Print player name & location
        print(f"{player.name} is in {player.current_room.name}")

        # * Prints the current rooms_dict name
        print(f"{player.current_room}")

        # * Waits for user input and decides what to do.
        direction = input("What do you do? \nOPTIONS: [n, s, e, w, (a)ction] ").lower()

        # If the user enters a cardinal direction, attempt to move to the rooms_dict there.
        if direction in ["n", "s", "e", "w", "q", "a"]:
            if direction == "n":
                # Update current rooms_dict to northern rooms_dict
                cur_room = cur_room.branches["north"]
            elif direction == "s":
                # Update current rooms_dict to southern rooms_dict
                cur_room = cur_room.branches["south"]
            elif direction == "e":
                # Update current rooms_dict to eastern rooms_dict
                cur_room = cur_room.branches["east"]
            elif direction == "w":
                # Update current rooms_dict to western rooms_dict
                cur_room = cur_room.branches["west"]

            elif direction == "a":
                action = input("What would you like to do? (s)earch (i)nventory (b)ack")
                if action.lower() == "s" and player.current_room.items:
                    items = cur_room.items
                    grabbed = []

                    for item in items:
                        print(f"{player.name} sees {item}")

                        decide = input(f"Do you want {item.name}? (y)/(n)? ").lower()

                        if decide == "y":
                            grabbed.append(item)

                        elif decide == "n":
                            print("You don't want that.")

                    for item in grabbed:
                        player.grab_item(item)
                        player.current_room.remove_item(item)

                # elif action == "s" and player.current_room.items in player.inventory:
                #     print("There is nothing to see here")

                if action.lower() == "i":
                    print(f"{player.inventory}")

            elif direction == "q":
                quit()

            # If current rooms_dict has None, print a message
            if cur_room is None:
                print(f"There is nowhere for {player.name} to go.")
            elif cur_room == player.current_room:
                # If current rooms_dict has not updated, print a message
                print("Think about your next move...")
            else:
                # If current rooms_dict available to update, update rooms_dict and move on
                print(f"{player.name} moves with vigor to {cur_room.name}")
                player.current_room = cur_room

        # Print an error message if the movement isn't allowed.
        else:
            print("Direction Not Valid")

    # If the user enters "q", quit the game.
