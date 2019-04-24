from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("torch", "Lights your way.")]),

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
room['outside'].add_addjacent_room(room['foyer'], "north")
room['foyer'].add_addjacent_room(room['overlook'], "north")
room['foyer'].add_addjacent_room(room['narrow'], "east")
room['narrow'].add_addjacent_room(room['treasure'], "north")

#
# Main
#
player = Player(room['outside'])
previous_room = None

while True:
    if player.current_room is not previous_room:
        print(f'\nYou are now in the {player.current_room.name}')
        print(player.current_room.description)
    
    previous_room = player.current_room
    command = input("\nWhat would you like to do? ")

    if command == "north" or command == "n":
        player.move("north")
    elif command == "south" or command == "s":
        player.move("south")
    elif command == "east" or command == "e":
        player.move("east")
    elif command == "west" or command == "w":
        player.move("west")
    elif command == "look":
        player.look()

    elif command == "q":
        break
    else:
        print("\nThat isn't a valid command, try again.")

print("\nSee you later!\n")