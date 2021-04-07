from player import Player
from room import Room
from item import Item, Trinket, VitaminPack, Container

#Items List
necklace = Trinket(
    -1,
    "a priceless necklace is in one of these rooms somewhere",
    1
)

notebook = Trinket(
    -1,
    "no one knows how old this notebook is or who even wrote it... there appears to be strange characters on several pages...and is that.. blood?!?",
    1
)

backpack = Container(
    1,
    "backpack",
    "this backpack can hold everything except maybe your sanity",
    [necklace]
)

items = [necklace.name, notebook.name, backpack.name]

# Declare all the rooms
rooms = {
    'outside':  Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons. The path is steep and treacherous, but the mystery draws you in."),

    'foyer':    Room(
        "Foyer", 
        """
        Dim light filters in from the south. Dusty
        passages run north and east. There is an aging yellow velvet couch on the corner and it that... a backpack?!?""",
        [backpack]

),

    'overlook': Room(
        "Grand Overlook", 
        """
        A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.
        """,
        [notebook]
),

    'narrow':   Room(
        "Narrow Passage", 
        """
        The narrow passage bends here from west
to north. The smell of gold permeates the air. Or is that just the mold in the corners...? Through cobwebs and patch of dirt in the corner of the floor a small flash catches your eyes. Is that...no it can't be. It is a priceless antinque necklace that you quickly stash into your backpack."
        """,
        [necklace]
),

    'treasure': Room(
        "Treasure Chamber", 
        """
        You've found the long-lost rumored treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. There are scribblings on the wall. It looks like nothing at first, but then you realize that it is a map of another complex entirely. You quickly sketch down the map in your notebook. The eery stillness of the chamber creeps you out majorly. Happy with the necklace and the mystery of the notebook's characters, as well as the enigma of the new map, you set off as fast as you can to figure out what it all means. You exit to find out what the next level brings.
        """),
}

# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']
#initiate the room sequence
room = rooms['outside']

#
# Main

player = Player(room['outside'], "player one has arrived outside the room.")

i = input("Welcome to Mystery Volumes I: what should we call you?\n")
player = Player(i, room, 100, 0, 0)

print(f"Goodnight and goodluck, {player.name}")

def instructions():
    return """
        Welcome to the labyrinth dear wanderer...

        * use [L] to look around
        * [N,S,E,W] [North, South, East, West] [Up, Down, Right, Left] to travel in those directions
        * [q] to quit
    """

def current_dirs():
    currentDirs = directions()

    if currentDirs.__contains__("n"):
        currentDirs.extend(["north", "up", "forward", "forwards"])
    if currentDirs.__contains__("s"):
        currentDirs.extend(["south", "down", "backward", "backwards"])
    if currentDirs.__contains__("e"):
        currentDirs.extend(["east", "right"])
    if currentDirs.__contains__("w"):
        currentDirs.extend(["west", "left"])

    return currentDirs

def directions():
    directions = []

    if hasattr(player.current_room, "n_to"):
        directions.append("n")
    if hasattr(player.current_room, "s_to"):
        directions.append("s")
    if hasattr(player.current_room, "e_to"):
        directions.append("e")
    if hasattr(player.current_room, "w_to"):
        directions.append("w")

    return directions

def travel(input):

    input = input.lower()
    if input in current_dirs():
        if input == "n" or input == "north" or input == "up" or input == "forward" or input == "forwards":
            player.current_room = player.current_room.n_to
        elif input == "s" or input == "south" or input == "down" or input == "backward" or input == "backwards":
            player.current_room = player.current_room.s_to
        elif input == "e" or input == "east" or input == "right":
            player.current_room = player.current_room.e_to
        elif input == "w" or input == "west" or input == "left":
            player.current_room = player.current_room.w_to
    else:
        print("Wrong Way! There's nothing over there.")

def look():
    if player.current_room == rooms['outside']:
    
        print("Looking around the room you spot an object:")

        item_instructions = "take the object"

        #when there isn't anything in the room anyhow

        if len(player.current_room.items) == 0:
            print(f"Nothing is there...try another room to {item_instructions}")
            item_instructions = ""

        #displaying the descriptions of each room
        item_desc = [x.room_description for x in player.current_room.items]
        for i, _ in enumerate(item_desc):
            print(f"{player.current_room.items[i].name}: {item_desc[i]}")
        #empty line
        print()

    
def prompt(s):
    # print a quicklist of commands
    commands = f"(L to look around | {' | '.join(directions())} to travel | Q to quit | [Help|?] for common commands): "
    prompt = f"\nWhat would you like to do, {player.name}?\n{commands}"

    return input(s + prompt)

def parse(inpt):
    commands = [
        "travel", "walk", "run",
        "take", "drop", 
        "look"
    ]
    commands.extend(current_dirs())

    #add items available in this room to the command list
    commands.extend([item.name for item in player.current_room.items])

    #add the player's items
    commands.extend([item.name for item in player.inventory])
    commands.append(player.leftHandItem.name)
    commands.append(player.rightHandItem.name)

    inpt = inpt.lower()
    # list of the available command separated by space
    inputList = inpt.split()

    #only allow commands to be parsed
    commands = []
    for cmd in inputList:
        if cmd in commands or cmd in items:
            commands.append(cmd)
    
    if len(commands) >= 1:
        cmd1 = commands[0]
    
    if len(commands) > 1:
        cmd2 = commands[1]
        if len(commands) >2:
            print("only two commands can be used at a time separated by a space")
        #win the game and exit
        if cmd1 == "take" and cmd2 == "drop":
            if player.current_room != rooms['treasure']:
                print("Can you decipher anything in here?")
            else:
                print("""
                Do you see the writing's on the wall somewhere over here? 

                "No treasure, but some scratches on the wall...typical. Wait, is that a ... map?"

                You appoach the wall in the dimly lit room and realize that you are in fact staring at a map in front of you. You quickly get out the old notebook and sketch a copy of the map as quickly as you can.
                """)

        #parse verb commands
        if cmd1 == "travel" or cmd1 == "run" or cmd1 == "walk":
            travel(cmd2)
            return 

        if cmd1 == "take" or cmd1 == "drop":
            player.take(cmd2)
            return
        
        elif cmd1 == "drop":
            player.dropItem(cmd2)
            return

        #singular commands
        else:
            dirs = ["n", "north", "up", "e", "east", "right", "s", "south", "down", "w", "west", "left"]

            if inpt == "q":
                exit(0)
            elif inpt == "instructions" or inpt == "?" or inpt == "h":
                print(instructions())
                return
            elif inpt in dirs:
                travel(inpt)
                return
            elif inpt == "l":
                look()
                return
            elif inpt == "inventory" or inpt == "i":
                player.list_inventory()
                return
        print("invalid command")

    


