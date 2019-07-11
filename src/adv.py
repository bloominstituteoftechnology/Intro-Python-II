from room import Room
from player import Player
from item import Item
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
# print(f'Room: {room}')
#
# Main
#

item = Item('health', 'get extra health')
room['outside'].inventory.append(item)

item = Item('coins', '10 silver coins')
room['foyer'].inventory.append(item)

item = Item('sword', 'weapon to get creepers with')
room['foyer'].inventory.append(item)

item = Item('grass sword', 'the legendary grass sword of Oo is cursed and binds to a users soul who appears too weak.')
room['narrow'].inventory.append(item)

item = Item('coins', '250 silver coins')
room['narrow'].inventory.append(item)

item = Item('The Enchiridion', 'Ancient book with codes of conduct, guidelines, and other helpful information for heroes.')
room['narrow'].inventory.append(item)

item = Item('potion of healing', 'increases health by ')
room['narrow'].inventory.append(item)

def find_item(name, current_room):
    for item in current_room.inventory:
        if item.name == name:
            return item
    return None


#The hasattr() method returns true if an object has the given named attribute and false if it does not
def move_to(direction, current_room):
    attribute = direction + '_to'

    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)
    
    else:
        print("Not a valid room")
        return current_room


# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

# Write a loop that:
#
while True:
    # * Prints the current room name
    print(f"current room: {player.current_room.name}, {player.current_room.description}")
    # * Prints the current description (the textwrap module might be useful here).
    print(f"Room Items: {player.current_room.inventory}")
    
    # * Waits for user input and decides what to do.
    user = input("\n>").lower().split()
    # print(f"user input: {user}")
    
    if len(user) == 1:
        user = user[0]
        
        if user == "q":
            print("Come back again soon")
            break
        player.current_room = move_to(user[0], player.current_room)
        print(f"Current room: {player.current_room}, user0 from current room:  {user[0]}")
    elif len(user) == 2:
        
        #to get an item type get <item name>
        if user[0] == 'get':
            print(f"user[0]{user[0]}")
            item = find_item(user[1], player.current_room)
            if item == None:
                print('That item cannot be found')
            else:
                player.current_room.inventory.remove(item)
                player.inventory.append(item)
                print(f"{item.name} taken")
                
        if user[0] == 'drop':
            #to drop an item type drop <item name>
            item = find_item(user[1], player)
            if item == None:
                print('You are not carrying any items')
            else:
                player.inventory.remove(item)
                player.current_room.inventory.append(item)
                print(f"{item.name} dropped")
        if user[0] == "player":
            #type player inventory to see your inventory
            print(f"Your inventory contains: {player.inventory}")
  

    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.




