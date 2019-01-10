from room import Room
from player import Player
from item import Item
from monster import Monster

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('wand', 'Does not really work well, in really rough shape')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('sword', 'Looks as if it were just sharpened. Too bad its merely a training sword')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('potion', 'This can heal your health 25 points')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


monster = {
    'gorgon': Monster('Gorgon', """ With a head full of serpents, the creature flys above..stalking her prey.""", 150),

    'giant': Monster('Giant', """ A massive human-like beast with immense strenth""", 300),

    'tiger': Monster('Large Tiger', """ A very large tiger seems to be lurking around here..""", 100)
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

# Links monsters to a room
room['overlook'].monster = monster['gorgon']
room['narrow'].monster = monster['tiger']
room['treasure'].monster = monster['giant']

inits = 'Start of Game' # input variable used

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Austin')
current_room = room['outside']
print(current_room)
#============== FUNCTIONS ====================#


# moves player to user given direction
def command(p_inpt):
    """
    The command function handles all the input for the user
    directions are n s e or w.
    verbs are q or quit for quit
    drop for dropping item followed by item you want to drop separated by space
    take or get for getting item followed by item you want to get seperated by space

    """
    global current_room
    if p_inpt[0] == 'n':      # if the player input equals n for north
        new_room = current_room.n_to # set the current room to the room 
        current_room = new_room      # linked to the north by attr
        print(f"You are now at the {current_room.name}. {current_room.description}.")
        if len(current_room.items) > 0: # if there are any items in the current room 
            print(f"You see a {current_room.items[0]}.")
        if hasattr(current_room, 'monster') == True:
            print(f"You can also see a {current_room.monster.name}. {current_room.monster.description}")
            
    elif p_inpt[0] == 's': 
        new_room = current_room.s_to
        current_room = new_room
        print(f"You are now at the {current_room.name}. {current_room.description}")
        if len(current_room.items) > 0:
            print(f"You see a {current_room.items[0]}.")
        if hasattr(current_room, 'monster') == True:
            print(f"You can also see a {current_room.monster.name}. {current_room.monster.description}")
    elif p_inpt[0] == 'e':
        new_room = current_room.e_to
        current_room = new_room
        print(f"You are now at the {current_room.name}. {current_room.description}")
        if len(current_room.items) > 0:
            print(f"You see a {current_room.items[0]}.")
        if hasattr(current_room, 'monster') == True:
            print(f"You can also see a {current_room.monster.name}. {current_room.monster.description}")
    elif p_inpt[0] == 'w':
        new_room = current_room.w_to
        current_room = new_room
        print(f"You are now at the {current_room.name}. {current_room.description}\n")
        if len(current_room.items) > 0:
            print(f"You see a {current_room.items[0]}.\n")   
        if hasattr(current_room, 'monster') == True:
            print(f"You can also see a {current_room.monster.name}. {current_room.monster.description}")
    

    if p_inpt[0] == 'get' or p_inpt[0] == 'take':
        if len(current_room.items) > 0:
            for i in current_room.items:
                if p_inpt[1] == i.name:
                    player.items.append(i)
                    current_room.items.remove(i)
                    print(f"You have picked up the {i.name}\n")
                else:
                    print('There is no item with that name here\n')

    if p_inpt[0] == 'drop' or p_inpt[0] == 'd':
        if len(player.items) > 0:
            for i in player.items:
                if p_inpt[1] == i.name:
                    current_room.items.append(i)
                    player.items.remove(i)
                    print(f"You don't need {i.name} any longer, so you drop it\n")
        else: 
            print("You don't have any items to drop\n")

    if p_inpt[0] == 'inventory' or p_inpt[0] == 'i':
        if len(player.items) > 0:
            for i in player.items:
                print(i.name)
        else:
            print("Inventory is empty\n")
    
    if p_inpt[0] == 'q' or p_inpt[0] == 'quit':
        print("Ending game....Goodbye! \n")


# ================ Game Loop ===========================#

print(f"\n Welcome to your first adventure, {player.name}! \n Use 'n' to go North \n Use 's' to go South \n Use 'w' to go West \n Use 'e' to go East \n Press 'q' to quit game \n Type 'get' followed by the item name, separated by a space" )

while not inits[0] == 'q':
    if current_room == room['outside']:
        print(f'You are currently {current_room}\n')
    else:
        print('\n<=========================================> \n')
    
    try:
        inits = input('Enter a command: \n').split(' ')
        command(inits)
    except AttributeError:
      print("Can't go this way\n")
      continue

    # if len(current_room.items) > 0:
    #     inits = input('Would you like to pick up an Item?: \n').split(' ')
    #     if inits[0] == 'get' or inits[0] == 'take':
    #         for i in current_room.items:
    #             if inits[1] == i.name:
    #                 player.items.append(i)
    #                 print(f"You have picked up the {i.name}")
    #             else:
    #                 print('There is no item with that name here')

    