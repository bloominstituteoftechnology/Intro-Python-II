from room import Room
from player import Player
from item import Item

item = {
    "SWORD": Item("SWORD", "Old and rusted, but it'll get the job done if you have to use it."),

    "SHIELD": Item("SHIELD", """Makeshift shield someone made from flimsy wood. Might withstand a 
couple strikes before breaking apart"""),
}
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

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

room["outside"].items = [item["SWORD"], item["SHIELD"]]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

name = input("What's your name, adventurer?\n")
player = Player(name, room["outside"])
game_over = False

def describe_room(char):
    print(f"\n{char.name}, {char.room}\n")
    if char.room.items == []:
        print("This room holds no items.\n")
    elif len(char.room.items) == 2:
        print(f"This room holds a {char.room.items[0].name} and a {char.room.items[1].name}.\n")
    else:
        print(f"This room holds a {char.room.items[0].name}.\n")

def room_item_check(thing):
    global game_over
    if thing == "SHIELD":
        if player.inventory == []:
            print("""\nA hand of rotten flesh springs out of the ground and grabs your hand. You attempt
to defend yourself, but punches and kicks do nothing. Slowly, you're dragged down into the mud to join the zombies...""")
            game_over = True
            return False
        else:
            print("""\nA hand of rotten flesh springs out of the ground and grabs your hand. You struggle to no avail,
the zombie's grip is incredibly tough. You retrieve your sword and hack at the zombie's wrist until it finally
lets you loose and retreats back into the mud.""")
            return True
    for item in player.room.items:
        if thing == item.name:
            return True
    return False

def player_item_check(thing):
    for item in player.inventory:
        if thing == item:
            return True
    return False


playerAction = ""

while playerAction != "Q":
    describe_room(player)
    # print(player.room.revealItems())

    playerAction = input("[N] North [S] South [E] East [W] West [Q] Quit\n").upper()

    # testing result of code
    # print("s/b get", playerAction.split()[0])
    # print("s/b sword", playerAction.split()[1])
    # print("s/b sword", player.room.items[0].name)
    # print(str(playerAction.split()[1]) in player.room.items)
    

    if playerAction == "N" or playerAction == "S" or playerAction == "E" or playerAction == "W":
        if playerAction == "N" and player.room.n_to != None:
            player.room = player.room.n_to
        elif playerAction == "E" and player.room.e_to != None:
            player.room = player.room.e_to
        elif playerAction == "S" and player.room.s_to != None:
            player.room = player.room.s_to
        elif playerAction == "W" and player.room.w_to != None:
            player.room = player.room.w_to
        else:
            print("\nYou can't go in that direction, it's far too dangerous!")
    elif playerAction == "Q":
        print("\nCome back soon!")
        break
    
    # elif playerAction.split()[1] == "SWORD":
    #     print("sword works")
    elif playerAction.split()[0] == "GET" and room_item_check(playerAction.split()[1]):
        player.inventory.append(playerAction.split()[1])
        player.room.items.remove(item[playerAction.split()[1]])
        print(f"{player.name} examines the {item[playerAction.split()[1]]}.")
        print(f"{item[playerAction.split()[1]].description}")
    elif playerAction.split()[0] == "DROP" and player_item_check(playerAction.split()[1]):
        player.inventory.remove(playerAction.split()[1])
        player.room.items.append(item[playerAction.split()[1]])
        print(f"\nYou drop the {playerAction.split()[1]}. Remember that it's in {player.room.name}, it could be useful later.")
    elif game_over == True:
        print("\nTry Again?")
        break
    else:
        print("\nThat's not a direction! Please use N, S, E, or W")

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
