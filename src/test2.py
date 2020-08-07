from room import Room
from player import Player
#from item import Item

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
room['outside'].n_to = room['foyer']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


commands = ["n", "s", "e", "w"]


# class Player():
#     def __init__(self, name = None):
#         self.name = name
#         self.location = None
#         #self.current_room = None

#     # def quit(self):
#     #     self.playing = False

#     def move_player(self, direction):
#         self.location = current_room
#         move = f'{direction}_to'
#         if hasattr(current_room, move):
#             self.location = getattr(current_room, move)
#             return True
#         else:
#             print("There is no way to go that direction.")
#             return False

print("Welcome to the ADVENTURE Game!")

user = input("\nWhat is your name?\n")
player = Player(user, room['outside'])
print(f"\nWelcome {player.name}!\n{player.current_room.name}\n{player.current_room.description}")

items = []

while True:
    press = answer = input("\nWhat's your next move? \n Go North [n] South [s] East [e] West [w] ").lower().strip()

    if(press == "q"):
        print("Quitting Game...")
        break
    elif(press == "n"):
        if(player.current_room.n_to == None):
            print("\nThat direction does not exist\n")
        else:
            player.current_room = player.current_room.n_to
            print(f"\n{player.current_room.name}\n{player.current_room.description}")
    elif(press == "s"):
        if(player.current_room.s_to == None):
            print("\nThat direction does not exist\n")
        else:
            player.current_room = player.current_room.s_to
            print(f"\n{player.current_room.name}\n{player.current_room.description}")
    elif(press == "e"):
        if(player.current_room.e_to == None):
            print("\nThat direction does not exist\n")
        else:
            player.current_room = player.current_room.e_to
            print(f"\n{player.current_room.name}\n{player.current_room.description}")
    elif(press == "w"):
        if(player.current_room.w_to == None):
            print("\nThat direction does not exist\n")
        else:
            player.current_room = player.current_room.w_to
            print(f"\n{player.current_room.name}\n{player.current_room.description}")
    elif(press == "i"):
        if(len(items) == 0):
            print("\nYou have no Items\n")
        else:
            print(items)
    elif(press == "t"):
        items.append(player.current_room.item.name)
    else:
        print("\nWrong Input!\n")