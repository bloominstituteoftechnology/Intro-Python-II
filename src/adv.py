from room import Room, valid_directions
from player import Player
from items import Item
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
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#items
item = {
    'coins':  Item("Coins: ~~[Money", "--Just a few lose coins to take to the tavern]~~"),
    'tools':  Item("Tool: ~~[Grappling hook", "--This might come in handy. It is very heavy]~~"),
    'jewel': Item("Jewel: ~~[Gem", "--Next time you ask that stranger for information. He might be willing to help for this type of payment]~~"),
    'torch': Item("Tool: ~~[Torch", "--Let there be light. Is someone sneaking around? Why is this on the floor?!?]~~"),
    'trap': Item("Misc: ~~[Tripped Trap", "--An abandoned trap that has been tripped. If cleaned up it could be useful.]~~"),
    'medallion': Item("Jewel: ~~[Medallion", "--It reflects light and glows slightly orange it may be magical. There is an inscription in an unknown language. Inscription:Hul werud ezes ulud egembelu owog. Kyul buol engumet ullyetuk.]~~ "),
}

room['outside'].items = []
room['foyer'].items = [str(item['coins']), str(item['trap'])]
room['overlook'].items = [str(item['jewel']),str(item['medallion']),str(item['trap'])]
room['narrow'].items = [str(item['jewel']), str(item['coins']), str(item['torch'])]
room['treasure'].items = [str(item['tools'])]
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
players = Player('Dom', room['outside'])

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

def is_direction(str):
    """
        returns true from string if it is a valid
    """
    return str in valid_directions

print(f'Welcome {players.name}, press q at any time to quit')
print(f'You are currently {players.current_room.name}')
print(players.current_room.description)
current_room = players.current_room
items = current_room.items

def item_check(room_items):
    if room_items != []:
        return True
    else:
        return False

while True:
    if current_room != players.current_room:
        print(players.current_room)
        current_room = players.current_room
        items = current_room.items         
    user_input = input('What would you like to do? Choose direction n, e, s or w? Or "view" Room: ')
    if user_input == 'q':
        break
    elif is_direction(user_input):
        players.move(user_input)
    elif user_input.lower().strip() == 'view':
        if item_check(items) == True:
          print('In this room you will find these items: ')
          for item in items:
            print(item)
          choice = str(input('Would you like to pick up these items: y or n '))
          if choice == 'y':
            players.pick_up(items)            
            print('Your inventory now contains ' + str(players.inventory))
            items.clear()
          else:
            user_input = input('What would you like to do? Choose direction n, e, s or w? Or "view" Room: ')                      
        else:
          print('There are no items in this room')
    else:
        print('Sorry that is not a valid command, please try again!')

