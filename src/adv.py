from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     'nothing',
                     'nothing',
                     'nothing',
                     'nothing',
                     'nothing'
                     ),


    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     'nothing',
                     'nothing',
                     'nothing',
                     'nothing',
                     'nothing'
                     ),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     'nothing',
                     'nothing',
                     'nothing',
                     'nothing',
                     'nothing'
                     ),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", 'nothing',
                     'nothing',
                     'nothing',
                     'nothing',
                     'nothing'
                     ),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", 'nothing',
                     'nothing',
                     'nothing',
                     'nothing',
                     'nothing'
                     ),
}
room['outside'].n = room['foyer']
room['foyer'].s = room['outside']
room['foyer'].n = room['overlook']
room['foyer'].e = room['narrow']
room['overlook'].s = room['foyer']
room['overlook'].e = room['narrow']
room['narrow'].w = room['foyer']
room['narrow'].n = room['treasure']
room['treasure'].s = room['narrow']
room['treasure'].loot = ["gold"]

# Main
current_player = Player("Brandon", "outside", ["sword", "belt"])
current_room_in = current_player.current_room
# welcome adventurers
print("Welcome to your adventure!")
print(room[current_room_in].name)
print(room[current_room_in].description)
# set initial direction
msg = str(input(
    "what direction will you go? Please press n for north s for south w for west or e for east or q for quit.\n"))
# set initial settings

current_room_in = ""
current_player.current_room_in = current_player.current_room


def adventure(msg):
    while not msg == "q":
        if hasattr(room[current_player.current_room], msg):
            if getattr(room[current_player.current_room], msg) != 'nothing':
                # two things that we need to print, name and description
                current_room_in = getattr(
                    room[current_player.current_room], msg).name
                current_room_description = getattr(
                    room[current_player.current_room], msg).description
                current_rooms_items = getattr(
                    room[current_player.current_room], msg).loot
                # check to see if el item exists. if it does offer to take it yes or no... then add conditional to drop item???
                # splitting each word into array of lowercase
                current_player.current_room = getattr(room[current_player.current_room], msg).name.lower(
                ).split(" ")
                # checking to see if one of those words exists in the dictionary of rooms
                for key in room:
                    if key in current_player.current_room:
                        # if it does use that word as the new room
                        current_player.current_room = key
                        # print where we are
                print(current_room_in, current_room_description)
                # check for an item in the room
                if isinstance(current_rooms_items, list) and len(current_rooms_items) > 0:
                    item = str(input(
                        f"you see {current_rooms_items[0]} would you like to pick it up? press y or n\n"))
                    if item == "y":
                        current_player.items.append(current_rooms_items[0])
                        print(f"you have picked up {current_rooms_items[0]}")
                        if "gold" in current_rooms_items:
                            current_rooms_items.remove("gold")

                msg = str(input(
                    "what direction will you go? Please press n for north s for south w for west or e for east or q for quit.\n"))

            else:
                msg = str(input(
                    "That was is blocked. What direction will you go? Please press n for north s for south w for west or e for east or q for quit.\n"))
        else:
            msg = str(input(
                "Please enter a real direaction! what direction will you go? Please press n for north s for south w for west or e for east or q for quit.\n"))


adventure(msg)
