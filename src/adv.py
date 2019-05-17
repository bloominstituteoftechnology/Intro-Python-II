from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """⛰️ A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """💰 You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Declare the items

items = {
    "broom": Item("Magic Broomstick (broom)", "🧹 The Magic Broomstick can fly quickly in any direction and hover."),
    "candlestick": Item("Golden Candlestick (candlestick)", "🕯️ The Casanova of all candelabras. He is suave and a gracious host."),
    "sword": Item("Andúril (sword)", "⚔️ The reforged sword from the shards of Narsil."),
    "map": Item("Treasure Map (map)", "🗺️ Follow the directions to get to the treasure."),
    "diamond": Item("Diamond (diamond)", "💎Beautiful!")
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

# Link items to rooms
room["outside"].items = [items['map']]
room["foyer"].items = [items['broom'], items['candlestick']]
room["overlook"].items = [items['sword']]
room["narrow"].items = [items['diamond']]

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

# Allow the player to quit


class Quit(Exception):
    pass

# Accept inputs from the player


def player_input(player):
    player_input = input("🔮 Enter a command: ").lower()
    command = player_input.split()[0]

    if len(player_input.split()) == 2:
        game_item = player_input.split()[1]

    if command in ("quit", "q"):
        print("Thanks for playing 🙌🏼")
        raise Quit
    elif command in ("n", "s", "e", "w", "north", "south", "east", "west"):
        player.move(command[0] + "_to")
        print(player.current_room)
    elif command in ("take", "drop", "look"):
        try:
            item = items[game_item]

            if command == "take":
                if item in player.current_room.items:
                    player.current_room.drop_item(items[game_item])
                    player.take_item(items[game_item])
                    print(items[game_item].pick_up())
                else:
                    print("\nItem is not in this room.")
            elif command == "drop":
                if item in player.items:
                    player.current_room.take_item(items[game_item])
                    player.drop_item(items[game_item])
                    print(items[game_item].drop_it())
                else:
                    print("\nYou do not have this item.")
            elif command == "look":
                if item in player.items:
                    print(item.look())
                else:
                    print("\nThis item is not in your inventory.")
        except KeyError:
            print("\nThis is not an item in this game.")
    elif command in ("i", "inventory"):
        print(f'\nYour inventory: {player.inventory}')
    else:
        print("💀 Please enter a valid command (n, s, e, w, i, take, drop, look).\n")
        return command

# Main method for the game


def game():
    print("👋🏼 Welcome to The Jungle 🌳 ")

    player_name = input("What would you like your name to be? ")
    player = Player(player_name, room["outside"])
    print("\n")
    print(player.current_room)

    try:
        while True:
            player_input(player)
    except Quit:
        pass


# Start game
game()
