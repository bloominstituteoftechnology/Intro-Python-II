from room import Room
from item import Item
from player import Player

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
#
# Main
#
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

item = {
    'sword': Item("Katana Sword", "A Japanese sword for samurai"),
    'knife': Item("Knife", "Chinese dagger"),
    'arrow': Item("Bow and Arrow", "Bow and arrow laced with poison"),
    'rope': Item("rope", "rope with claws")
}

room['outside'].items = [
    item['sword'],
    item['rope']
]

room['foyer'].items = [
    item['knife'],
    item['arrow'],
]

room['overlook'].items = [
    item['sword'],
    item['knife'],
]

room['narrow'].items = [
    item['arrow'],
    item['sword'],
]

room['treasure'].items = [
    item['arrow'],
    item['sword'],
    item['rope']
]


class Adv(Player):
    def __init__(self, name, current_room):
        super().__init__(name, current_room)

    def __str__(self):
        return f"Welcome, {self.name} and your are in {self.current_room} "


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.tim
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
# player_input = ''

# while len(player.name) != 0:
# player_input = input("Pick your location, using 'n' for north, 's' for south, 'w' for west, 'e' for east  ")

# current_location = 'outside'
# print(room[current_location])

player = Adv('Tiger', room['outside'])
print(player)
print(player.get_player_instruction())


while True:
    direction = input("\nKindly input your direction or action")

    try:
        if direction == 'n':
            if hasattr(player.get_current_room(), 'n_to'):
                player.set_current_room(player.get_current_room().n_to)
                print(player.get_current_room())
            else:
                print(f"\nSorry there no way there \n")

        if direction == 's':
            if hasattr(player.get_current_room(), 's_to'):
                player.set_current_room(player.get_current_room().s_to)
                print(player.get_current_room())
            else:
                print(f"\nSorry now to the south\n")

        if direction == 'w':
            if hasattr(player.get_current_room(), 'w_to'):
                player.set_current_room(player.get_current_room().s_to)
                print(player.get_current_room())
            else:
                print(f"\n No way to west..\n")

        if direction == 'e':
            if hasattr(player.get_current_room(), 'e_to'):
                player.set_current_room(player.get_current_room().s_to)
                print(player.get_current_room())
            else:
                print(f"\nSorry now to the east..closed\n")
        else:
            print('Wrong direction, bye')
    except ValueError:
        print(f"{super.__get_player_instruction__}")
