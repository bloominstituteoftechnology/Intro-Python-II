from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance","North of you, the the doors becon", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",[Item("torch","the faint glow from this torch can light up a room")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
    'library': Room("#       Library          #", """you have found a place for reading. Unfortunately in your adventures you never learned the Dewey Decimal System so finding books is very difficult""", []),

    'breakfastnook': Room("#        Breakfast Nook       #", """Just off the kitchen a breakfast nook ending in a large curved window setting overlooking a large yard. Looks pretty nice. I wonder what...Wait WHY AM I HERE?""", []),

    'livingroom': Room("#       Living Room       #", """You find a lavish 30 by 20 foot living room. an ornate table sits in front of the fireplace flanked by two sofas. The fire still crackling. The room looks dustless and well kept""", []),

    'kitchen': Room("#        Kitchen        #", """In front of you, a modern kitchen. outfitted with all the trappings a hom of this size should have with one exception you notice, "where is the fridge?""", [] ),

    'staircase': Room("#        Staircase         #", """You walk up an iron railing staircase. to your right are assorted pictures of a family. You dont recognize any of them. but they look happy """, []),

    'secretroom': Room("#        An unplaned room has no Name       #", """you find a secret room of someones design. outfitted with a cmall collection of books and a desk. you wonder if anything here is worth keeping a secret? you see a dimmly lit staircase going down""", []),

    'sprialstaircase': Room("#       ~Sprial Staircase~        #", """a large sprial staircase decends into darkness lit only by the light of a single torch on the wall""", []),

    'landing': Room("#        Staircase Landing       #", """the staircase ends on a landing to the west a large room. to the east you see streaks of light from a window at the end, rooms on both sides of the hallway""", []),

    'longhallway1': Room("#      Hallway      #", """a room door on to the north, a room door to the south. East the hallway continues""", []),

    'longhallway2': Room("#     Hallway     #", """a room door on the north, a room door to the south, the hallway continues to a door to what looks like a balcony""", []),

    'bedroom1': Room("#      Bedroom       #", """Its a bedroom what do you expect..... you find a piece of paper missing 3 letters which reads a--- """, []),

    'bedroom2': Room("#      Bedroom       #",  """Its a bedroom what do you expect -b-- """, []),

    'bedroom3': Room("#       Bedroom      #", """Its a bedroom what do you expect --c- """, []),

    'bedroom4': Room("#       Bedroom       #", """Its a bedroom what do you expect ---d """,[]),

    'bedroom5': Room("#       Master Bedroom      #", """Its a bedroom what do you ex.....you find a mirror. you see yourself for seeminly the first time. a shiver runds down your spint """, []),

    'largecolumedexpanse': Room("#       ~Large columned expanse~      #", """ columns 4 feet wide are spaced evenly across this large 50 foot tall 40 foot wide expanse. darkness is before you. westward into the darkness or east to cowardice """, []),

    'largecolumedexpanse2': Room("#       ~Large columned expanse~      #", """ you see as you press forward a large fire pit within a wide opening copper pot. the smell of gasoline is strong. its pretty dark in here, might be easier to see with light you think. westward further into the hall or east toward cowardice """, []),

    'largecolumedexpanse3': Room("#       ~Large columned expanse~      #", """ you find a wall. empty of defects like the other room. a dead end.... East toward cowardice???, """, []),

    'balcony': Room("Balcony", """you find a door to a balcony, stepping out fresh air greets you. West to go back inside""", [])




}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['staircase']
room['foyer'].w_to = room['livingroom']
room['livingroom'].n_to = room['kitchen']

room['kitchen'].e_to = room['breakfastnook']
room['breakfastnook'].w_to = room['kitchen']
room['staircase'].n_to = room['landing']
room['foyer'].e_to = room['library']
room['staircase'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['foyer']
room['treasure'].s_to = room['narrow']


#upstairs
room['landing'].w_to = room['bedroom5']
room['bedroom5'].e_to = room['landing']
room['landing'].e_to = room['longhallway1']
room['longhallway1'].e_to = room['longhallway2']
room['longhallway1'].w_to = room['landing']
room['longhallway1'].s_to = room['bedroom2']
room['bedroom2'].n_to = room['longhallway1']
room['longhallway1'].n_to = room['bedroom1']
room['bedroom1'].s_to = room['longhallway1']

room['longhallway2'].e_to = room['balcony']
room['balcony'].w_to = room['longhallway2']
room['longhallway2'].n_to = room['bedroom3']
room['bedroom3'].s_to = room['longhallway2']
room['longhallway2'].s_to = room['bedroom4']
room['bedroom4'].n_to = room['longhallway2']






room['library'].key_to = room['secretroom']
room['secretroom'].s_to = room['sprialstaircase']
room['secretroom'].n_to = room['library']
room['sprialstaircase'].n_to = room['secretroom']
room['sprialstaircase'].s_to = room['largecolumedexpanse']

room['largecolumedexpanse'].e_to = room['largecolumedexpanse2']
room['largecolumedexpanse2'].e_to = room['largecolumedexpanse3']
room['largecolumedexpanse2'].w_to = room['largecolumedexpanse']
room['largecolumedexpanse3'].w_to = room['largecolumedexpanse2']
room['largecolumedexpanse'].s_to = room['sprialstaircase']
room['sprialstaircase'].s_to = room['largecolumedexpanse']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

bob = Player(
    name = "Bob",
    room = room['outside']
)

cmd = input("Enter a direction ")

def print_room_info():
    print(bob.room.name + ":")

    print(bob.room.description)

    bob.room.view_items()


action = cmd    
    # if action == g or action == "grab":
    #     if parsed_cmd[1] in bob.room.item

# if action == g or action =="grab":
# if parsed_cmd[1] in bob.room.items

parsed_cmd = cmd.split()

if action == "g" or action =="grab":
    for i in bob.room.items:
        if cmd[1] == i.item:
            print("grabbing item")
            bob.items.append(i)
            bob.room.items.remove(i)


if len(parsed_cmd) > 1:
    action = parsed_cmd[0]
    # item =''

    for i in range(1, len(parsed_cmd)):
        item += parsed_cmd[i] + " "
    item = item.strip()

    if action == "g" or action == "grab":
        if parsed_cmd[1].name in bob.room.items:
            print("...grabbing item")


dir = ""

while not dir == "q":
    # cmd = input('string')
    # cmd = input("Please enter... \nn, s, e, w, to move or \ng [item] to get item OR \nq to quit the game").lower()
    # parsed_cmd = cmd.split("")
    # "Get" "item name"
    
    print(bob.room.name)
    print(bob.room.description)
    if bob.room.items != None:
        print(bob.room.items)
    

    # if parsed_cmd[1] == i.name:
    #     print('...something')

    #     bob.items.append( i )

    #     bob.room.items.remove( i )

    dir = input('please enter a direction...n, s, e, w, or q to quit the game')
    parsed_cmd = dir.split()
    if len(parsed_cmd) == 2:
        if parsed_cmd[0].lower() == "get":
            print(f"{parsed_cmd[1]} picked up")
            # put item name
            bob.items.append(bob.room.items[0])
            print(bob.items)

    if dir == "n":
        if hasattr(bob.room, "n_to"):
            bob.room = bob.room.n_to

        print('#BAM!~~~~~ a wall finds purchase on your forehead. Try another path')
        
    elif dir =="s":
        if hasattr(bob.room, "s_to"):
            bob.room = bob.room.s_to
        
        print('#BAM!~~~~~ a wall finds purchase on your forehead. Try another path')

    elif dir == "e":
        if hasattr(bob.room, "e_to"):
            bob.room = bob.room.e_to

        print('#BAM!~~~~~ a wall finds purchase on your forehead. Try another path')

    elif dir == "w":
        if hasattr(bob.room, "w_to"):
            bob.room = bob.room.w_to

        print('#BAM!~~~~~ a wall finds purchase on your forehead. Try another path')

    elif dir != "w" and "e" and "s" and "n":
        print('#BAM!~~~~~ a wall finds purchase on your forehead. Try another path')


print("Game Exited .... or did the game exit you?")
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
