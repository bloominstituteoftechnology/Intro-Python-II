from room import Room
from player import Player
from basic_room import basic_room
from cave import cave
from narrow import narrow
from treasure import treasure
from overlook import overlook
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
chamber! The only exit is to the south.""", 'nothing',
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
room['treasure'].loot = ["gold", "silver"]

# Main
current_player = Player("Brandon", "outside", ["sword", "belt"])
current_room_in = current_player.current_room
# welcome adventurers
print("Welcome to your adventure!")
print(room[current_room_in].name)
print(room[current_room_in].description)
print(cave())
# set initial direction
msg = str(input(
    "what direction will you go? Please press n s w e or q for quit.\n"))
# set initial settings

current_room_in = ""
current_player.current_room_in = current_player.current_room


def adventure(msg):
    while not msg == "q":

        item_drop = msg.split(" ")

        if "drop" in item_drop:
            if item_drop[1] in current_player.items:
                print(f"you have dropped {item_drop[1]}")
                current_player.items.remove(item_drop[1])
            else:
                print("you don't have that *^&%")
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
                # refactor to be conditional here
                if current_room_in == "Foyer":
                    print(basic_room())
                if current_room_in == "Narrow Passage":
                    print(narrow())
                if current_room_in == "Treasure Chamber":
                    print(treasure())
                if current_room_in == "Grand Overlook":
                    print(overlook())
                if isinstance(current_rooms_items, list) and len(current_rooms_items) > 0:
                    items_string = " ".join(current_rooms_items)
                    item = str(input(
                        f"you see {items_string}. type get and the name the item you would like to get!"))
                    item = item.split(" ")
                    if len(item) > 1:
                        if item[1] in current_rooms_items and item[0] == "get":
                            index = current_rooms_items.index(item[1])
                            current_player.items.append(
                                current_rooms_items[index])
                            print(
                                f"you have picked up {current_rooms_items[index]}")
                            current_rooms_items.remove(
                                current_rooms_items[index])
                        else:
                            print("this does not exist")
                    else:
                        print("did you type get?")

                msg = str(input(
                    "what direction will you go? Please press n s w e or q for quit.\n"))

            else:
                msg = str(input(
                    "That was is blocked. What direction will you go? Please press n s w e or q for quit.\n"))
        else:
            msg = str(input(
                "Please enter a DIRECTION! what direction will you go? Please press n for s w e or q for quit.\n"))


adventure(msg)
