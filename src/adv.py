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

# key = Item('key', "Old Key")
# old_latern = Item(
#     'old latern', "A latern sits on an old table in the foyer, cobb webs hang off it. Doesn't seem like some one has been in here in a while")

item = {
    'key': Item('key', "Old Key"),
    'latern': Item('latern', 'An old latern covered in dust & cob webs. The room illuminates as the item is picked up!'),
    'random': Item('random', 'iuhklciuyaghdsukfh')
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


# PLAYER DECLARATION
new_player = input('Give your player a name: ')
player = Player(new_player, room['outside'])


# Room Item Declarations
room['outside'].add_room_item(item['key'])
room['outside'].add_room_item(item['random'])
room['foyer'].add_room_item(item['latern'])

command = ''


while True:
    print(player)
    command = input(
        ' \n \n Insert q to quit, \n Use n, s, e, w to move through out the map \n To pick up an item type: grab, followed by the item name in sight! \n \n To drop an item type: drop, followed by the item in your inventory. \n Make a move: ').split(" ")

    new_room = getattr(player.current_room, command[0].lower() + "_to", None)
    player_inventory = [item for item in player.items]

    if(len(command) == 1):
        if new_room:
            player.current_room = new_room
        elif (command[0] == 'q'):
            break
        else:
            print(' \n \n !!!INVALID COMMAND, PLEASE TRY AGAIN!!!')

    elif(len(command) == 2 and command[0].lower() == 'grab'):
        item_choice = command[1].lower()
        item_name = [item.name
                     for item in player.current_room.items_in_room]

        if item_choice in item_name:
            player.pick_up_item(item[item_choice].name)
            player.current_room.remove_room_item(item[item_choice])
            print(f'\n \n You have picked up a {item_choice}!')
            # print('ITEMS:', str(command[1].lower()))
        else:
            print(
                f' \n \n Sorry but {item_choice} does not exist in {player.current_room}')

    elif(len(command) == 2 and command[0].lower() == 'drop'):
        item_choice = command[1].lower()
        if item_choice in player_inventory:
            player.drop_item(item[item_choice].name)
            player.current_room.add_room_item(item[item_choice])
        else:
            print(
                f' \n \n SORRY, BUT {item_choice} DOES NOT EXIST IN YOUR INVENTORY \n \n')
