from room import Room
from player import Player
#
# # Declare all the rooms
#
room = {
    'outside':  Room('outside', "Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["rock", "stick"]),

    'foyer':    Room('foyer', "Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room('overlook', "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room('narrow', "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room('treasure', "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [])
}
#
#
# # Link rooms together
#
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

# Make a new player object that is currently in the 'outside' room.
name = input("Please enter your character name: ")
player = Player(name, room["outside"], [])
print("\n")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
q = ""
while q != "q":
    if q != "You can't go that way!":
        print(player.room)
    q=input("Where would you like to move? ")
    print("\n")
    try:
        if q == "N" or q == "n" or q == "north" or q == "North":
            player.room = player.room.n_to
        elif q == "S" or q == "s" or q == "south" or q == "South":
            player.room = player.room.s_to
        elif q == "E" or q == "e" or q == "east" or q == "East":
            player.room = player.room.e_to
        elif q == "W" or q == "w" or q == "west" or q == "West":
            player.room = player.room.w_to
        elif q == "items" or q == "Items" or q == "i" or q == "I":
            if len(player.items) > 0:
                print("Your Items:")
                for i in range(0, len(player.items)):
                    print(str(i+1) + ". " + player.items[i])
                print("\n")
            else:
                print("You have no items!")
        else:
            q = q.split()
            if q[0] == "get" or q[0] == "Get":
                if player.room.items.index(q[1]) >= 0:
                    player.items.append(q[1])
                    room[player.room.title].items.remove(q[1])
                    player.room = room[player.room.title]
            elif q[0] == "drop" or q[0] == "Drop":
                if player.items.index(q[1]) >= 0:
                    player.items.remove(q[1])
                    room[player.room.title].items.append(q[1])
                    player.room = room[player.room.title]
    except:
        if q[0] == "drop" or q[0] == "Drop":
            print("You don't have a " + q[1] + "!\n")
        elif q[0] == "get" or q[0] == "Get":
            print("There is no " + q[1] + " here!\n")
        else:
            q = "You can't go that way!"
            print(q)

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
