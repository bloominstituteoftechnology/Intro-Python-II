from room import Room
from player import Player
from item import Item, ItemHandler

# Declare all the rooms

outside = Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons")
foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""")
overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")
narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""")
treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")


# Link rooms together

outside.connect(room=foyer, direction='n')
foyer.connect(room=outside, direction='s')
foyer.connect(room=overlook, direction='n')
foyer.connect(room=narrow, direction='e')
overlook.connect(room=foyer, direction='s')
narrow.connect(room=foyer, direction='w')
narrow.connect(room=treasure, direction='n')
treasure.connect(room=narrow, direction='s')

# Make some items

chalice = Item(id=100, name='Golden Chalice', desccription='Actually an adult toy.')

# Create Item Handler

item_handler = ItemHandler()

# Have item_handler place chalice

item_handler.place_item(chalice, outside)


### Helper Functions ###
def select_item(command, inventory):
    item_name = command.split(' ')
    item_name = ' '.join(item_name[1:])
    for item_id in inventory.keys():
        if inventory[item_id].name.lower() == item_name.lower():
            return inventory[item_id]

if __name__ == "__main__":
    # Make a new player object that is currently in the 'outside' room.

    player_1 = Player()
    player_1.current_room = outside

    # Write a loop that:

    run = True

    while run:
        player_1.look()
        command = input('Where do you go? (Move: n-e-s-w, \nInteract: "grab", "drop" \nor quit with "q") ')
        if command == 'q':
            print('Bye!')
            break

        elif command in ['n', 'e', 's', 'w']:
            player_1.move(direction=command)

        elif command == 'i':
            print('Your Inventory: ', player_1.scan_items())


        elif 'grab' in command:
            item = select_item(command=command, inventory=player_1.current_room.items)
            item_handler.move_item(
                player_1.current_room, 
                player_1,
                item,
                )
        
        elif 'drop' in command:
            item = select_item(command=command, inventory=player_1.items)
            item_handler.move_item(
                player_1,
                player_1.current_room,
                item,
                )

        print('\n')


