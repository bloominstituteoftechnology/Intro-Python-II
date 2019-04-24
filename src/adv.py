from room import Room
from player import Player
from item import Item
from parser import Parser

# Declare all the rooms

room = {
    'outside':  Room("Parking Lot",
                     "You see the office entrance to the north"),

    'lobby':    Room("Lobby", """Not much to see here. The elevator lies to the north, stairs to the east."""),

    'elevator': Room("Elevator", """Not much room in here, but you can choose any of the three floors: '1', '2', '3'"""),

    'second_floor_hallway':   Room("Second Floor Hallway", """"""),
}


# Link rooms together
room['outside'].add_addjacent_room(room['lobby'], "north")
room['lobby'].add_addjacent_room(room['elevator'], "north", False)
room['elevator'].add_addjacent_room(room['lobby'], "first", False)

# Add items to rooms
room['lobby'].add_items(Item("mug", """It is empty, but you can fill it up with some of that life-giving liquid."""), Item("apple", "Looks tasty."))
#
# Main
#
player = Player(room['outside'])
previous_room = None

parser = Parser(player)

while True:
    if player.current_room is not previous_room:
        print(f'\nYou are now in the {player.current_room.name}')
        print(player.current_room.description)
    
    previous_room = player.current_room
    command = input("\nWhat would you like to do? ")

    if not parser.parse_command(command):
        break

print("\nSee you later!\n")