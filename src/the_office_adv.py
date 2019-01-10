from room import Room
from player import Player
from item import Item

# Declare all the rooms
room = {
    'outside':  Room("Outside Scranton Business Park",
                     """Welcome to Scranton Business Park. \n
    1725 Slouh Ave. \n
    Scranton, PA 45342 \n
    North of you, is the main enterance"""),
    'fun_run':  Room("""Michael Scott's Dunder Mifflin Scranton Meredith Palmer
    Memorial Celebrity Rabies Awareness Pro-Am Fun Run Race For The Cure""",
                     "A race to cure rabbies."),

    'lobby':    Room("Lobby", """To the west is Hank's cafe. To the north is a
    hallway that leads to the 100 level suite buildings.
    To the east is the stairs that lead to
    The Second Floor Hallway."""),

    'cafe': Room("Hank's Cafe", """A steep cliff appears before you, falling
    into the darkness. Back to the east is the lobby"""),

    'hallway_one':   Room("First Floor Hallway", """To the west is Suite 100,
    To the east is Suite 110, to the north is Suite 120,
    and the lobby is to the south"""),

    'hallway_two':   Room("Second Floor Hallway", """To the west is Suite 200,
    To the east is Suite 210,
    To the north is the stairway to Hallway Three
    and the stairs to the First Floor Hallway to the south"""),

    'hallway_three':   Room("Third Floor Hallway", """To the west is Suite 300,
    To the east is Suite 302, the hallway continues to the north,
    and the stairs to the Second Floor Hallway lie to the south"""),

    'hallway_three_cont':   Room("Third Floor Hallway Continued", """To the west is Suite 320,
    To the east is Suite 344, to the norht is Suite 345,
    and the beginning of the hallway lies to the south"""),

    '100':   Room("Suite 100 - Ruben's Elec. Cont.", """There's not much
    going on here."""),

    '110':   Room("Suite 110 - W.B. Jones Heating & Air", """There's not much
    going on here."""),

    '120':   Room("Suite 120 - Available 1400", """This room is deserted"""),

    '200':   Room("Suite 200 - Dunder Mifflin Paper", """There's not much
    going on here."""),

    '210':   Room("Suite 210 - Vance Refrigeration", """There's not much
    going on here."""),

    '300':   Room("Suite 300 - Woods & Grammercy", """There's not much
    going on here."""),

    '302':   Room("Suite 302 - Cress Tool & Die", """There's not much
    going on here."""),

    '320':   Room("Suite 320 - E.G. Phylloxy", """There's not much
    going on here."""),

    '344':   Room("Suite 344 - Kavala Data Filters", """There's not much
    going on here."""),

    '345':   Room("Suite 345 - Dwight Schrute", """There's not much
    going on here.""")
}

items = {
    'key': Item('Key', 'It\'s a key to something'),
    'sword': Item('Sword', 'It\'s a weapon'),
    'mouse': Item('Mouse', 'It could be a pet'),
    'map': Item('Map', 'Helps you get around'),
    'backpack': Item('Backpack', 'Holds more items'),
    'yo-yo': Item('Yo-Yo', 'A fun toy'),
    'water': Item('Water', 'Stay hydrated'),
}


# Link rooms together
room['outside'].n_to = room['lobby']
room['outside'].s_to = room['fun_run']
room['fun_run'].n_to = room['outside']
room['lobby'].n_to = room['hallway_one']
room['lobby'].w_to = room['cafe']
room['lobby'].s_to = room['outside']
room['lobby'].e_to = room['hallway_two']
room['cafe'].e_to = room['lobby']
room['hallway_one'].n_to = room['120']
room['120'].s_to = room['hallway_one']
room['hallway_one'].w_to = room['100']
room['100'].e_to = room['hallway_one']
room['hallway_one'].s_to = room['lobby']
room['hallway_one'].e_to = room['110']
room['110'].w_to = room['hallway_one']
room['hallway_two'].n_to = room['hallway_three']
room['hallway_two'].w_to = room['200']
room['200'].e_to = room['hallway_two']
room['hallway_two'].s_to = room['lobby']
room['hallway_two'].e_to = room['210']
room['210'].w_to = room['hallway_two']
room['hallway_three'].n_to = room['hallway_three_cont']
room['hallway_three'].w_to = room['300']
room['300'].e_to = room['hallway_three']
room['hallway_three'].s_to = room['hallway_two']
room['hallway_three'].e_to = room['302']
room['302'].w_to = room['hallway_three']
room['hallway_three_cont'].n_to = room['345']
room['345'].s_to = room['hallway_three_cont']
room['hallway_three_cont'].w_to = room['320']
room['320'].e_to = room['hallway_three_cont']
room['hallway_three_cont'].s_to = room['hallway_three']
room['hallway_three_cont'].e_to = room['344']
room['344'].w_to = room['hallway_three_cont']


# Place items in rooms
room['fun-run'].items = [items['shirt']]
room['overlook'].items = [items['mouse'].name, items['yo-yo'].name]
room['narrow'].items = [items['backpack'].name]
room['treasure'].items = [items['water'].name]

#
# Main
#


def try_direction(direction, current_room):
    attribute = direction + '_to'
    # see if inputted direction is one we can move to
    if hasattr(current_room, attribute):
        # fetch the new room
        return getattr(current_room, attribute)
    else:
        print('You can\'t go that way. Try a different direction.')
        return current_room

# Make a new player object that is currently in the 'outside' room.


# Init a new player to play the game
# set current room to outside
player = Player(room['outside'])

# game loop
while True:
    # Display current room, desc, items
    print(player.current_room)

    # User enters a command
    user_input = input('> ').lower().split(' ')

    # If Item command
    if len(user_input) == 2:
        if user_input[0] == 'get' or user_input[0] == 'take':
            item_count = len(player.current_room.items)
            for i, item in enumerate(player.current_room.items):
                if item.lower() == user_input[1]:
                    player.items.append(player.current_room.items.pop(i))
                    print(f"Updated inventory: {player.items}")
        elif user_input[0] == 'drop':
            item_count = len(player.items)
            for i, item in enumerate(player.items):
                if item.lower() == user_input[1]:
                    player.current_room.items.append(player.items.pop(i))
                    print(f"Updated inventory: {player.items}")
    elif len(user_input) == 1:
        if user_input[0] == 'q':
            print('You left the game, game over!')
            break
        if user_input[0] == 'i' or user_input[0] == 'inventory':
            print(f"inventory: {player.items}")

        player.current_room = try_direction(user_input[0], player.current_room)
