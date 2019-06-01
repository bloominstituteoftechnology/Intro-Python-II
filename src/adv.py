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

# Add items to rooms
room['foyer'].items.append(Item('Sword', 'A shiny longsword'))
room['foyer'].items.append(Item('Shield', 'A simple shield'))
room['foyer'].items.append(Item('Helmet', 'A sturdy helmet'))

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


def show_help():
    print("**********************************************************************")
    print("    h or help                help menu")
    print("    q or quit                quit game")
    print("    e or east                move east")
    print("    s or south               move south")
    print("    w or west                move west")
    print("    n or north               move north")
    print("    l or look                search room")
    print("    i or inventory           player inventory")
    print("    g or get [item]          get item")
    print("    t or take [item]         take item")
    print("    d or drop [item]         drop item")


def main():
    player = Player("Eric", room['outside'])
    show_help()

    while True:
        print("**********************************************************************")
        print(player.current_room.name)
        print(player.current_room.description)

        tokens = input("? ").strip().split(' ')

        if len(tokens) == 1:
            cmd = tokens[0]
            if cmd == 'q' or cmd == 'quit':
                break
            elif cmd == 'h' or cmd == 'quit':
                show_help()
            elif cmd == 'i' or cmd == 'inventory':
                print('*** Player inventory ***')
                if len(player.items):
                    for item in player.items:
                        print(item.name)
                else:
                    print('None')
            elif cmd == 'l' or cmd == 'look':
                print('*** Items in room ***')
                if len(player.current_room.items):
                    for item in player.current_room.items:
                        print(item.name)
                else:
                    print('None')
            elif cmd == 'e' or cmd == 'east':
                if player.current_room.e_to is not None:
                    player.current_room = player.current_room.e_to
                else:
                    print('!!! Unable to move that direction !!!')
            elif cmd == 's' or cmd == 'south':
                if player.current_room.s_to is not None:
                    player.current_room = player.current_room.s_to
                else:
                    print('!!! Unable to move that direction !!!')
            elif cmd == 'w' or cmd == 'west':
                if player.current_room.w_to is not None:
                    player.current_room = player.current_room.w_to
                else:
                    print('!!! Unable to move that direction !!!')
            elif cmd == 'n' or cmd == 'north':
                if player.current_room.n_to is not None:
                    player.current_room = player.current_room.n_to
                else:
                    print('!!! Unable to move that direction !!!')
            else:
                print('!!! Invalid command !!!')
                show_help()
        elif len(tokens) == 2:
            cmd = tokens[0]
            item = tokens[1]
            if cmd == 't' or cmd == 'take' or cmd == 'g' or cmd == 'get':
                index = None
                for i, val in enumerate(player.current_room.items):
                    if val.name == item:
                        index = i
                        break
                
                if index is not None:
                    i = player.current_room.items.pop(index)
                    player.items.append(i)
                    i.on_take()
                else:
                    print('!!! Item not in room !!!')
            elif cmd == 'd' or cmd == 'drop':
                index = None
                for i, val in enumerate(player.items):
                    if val.name == item:
                        index = i
                        break

                if index is not None:
                    i = player.items.pop(index)
                    player.current_room.items.append(i)
                    i.on_drop()
                else:
                    print('!!! Item not in inventory !!!')
            else:
                print('!!! Invalid command !!!')
                show_help()

    print('*** End Game ***')


if __name__ == "__main__":
    main()
