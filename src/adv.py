from room import Room
from player import Player
from item import Item

# Declare items available

sword = Item('Sword', 'A short and rusty blade, must of been left here ages ago!')
shield = Item('Shield', 'a small wooden shield')

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

# ##################################################################### #
#                                 Main                                  #
# ##################################################################### #

# Name input
name = input("What is your adventurer's name? ")

# Player object starts 'outside'
player = Player(room['outside'], name)

# Greeting for when you enter the game
print(f"\nGreetings {player.playerName}, you can control your adventure using the keys: N, E, S, W to move around the dungeon and Q to end your time here")

# Add items to foyer room
def add_items_to_foyer():
    if player.currentRoom.name != room['foyer'].name:
        room['foyer'].items.pop()
        room['foyer'].items.pop()
    if player.currentRoom.name == room['foyer'].name:
        room['foyer'].items.append(sword)
        room['foyer'].items.append(shield)


# game loop
game_over = False

while game_over == False:

    player_move = input("\n[N] North, [E] East, [S] South, [W] West, [Q] Quit, [I] Items >> ").upper()

    if player_move == 'I':

        print(*player.playerItem, sep = "\n")

        item_input = input("[Drop] or [Take] [Item] >> ").upper()
        
        if item_input == 'DROP SWORD':
            player.playerItem.remove(sword)
            print(f'\n{sword.itemName} has been dropped')
        
        if item_input == 'TAKE SWORD':
            player.playerItem.append(sword)
            print(f"{sword.itemName} has been picked up")

        if item_input == 'DROP SHIELD':
            player.playerItem.remove(shield)
            print(f'\n{shield.itemName} has been dropped')
        
        if item_input == 'TAKE SHIELD':
            player.playerItem.append(shield)
            print(f"{shield.itemName} has been picked up")
            

    if player_move == 'N' or player_move == 'E' or player_move == 'S' or player_move == 'W' or player_move == 'Q':

        if player_move == 'N' and player.currentRoom.n_to != None:
            player.currentRoom = player.currentRoom.n_to
            add_items_to_foyer()
            print(player.currentRoom)

        elif player_move == 'E' and player.currentRoom.e_to != None:
            player.currentRoom = player.currentRoom.e_to
            add_items_to_foyer()
            print(player.currentRoom)
        
        elif player_move == 'S' and player.currentRoom.s_to != None:
            player.currentRoom = player.currentRoom.s_to
            add_items_to_foyer()
            print(player.currentRoom)

        elif player_move == 'W' and player.currentRoom.w_to != None:
            player.currentRoom = player.currentRoom.w_to
            add_items_to_foyer()
            print(player.currentRoom)

        elif player_move == 'N' and player.currentRoom.n_to == None or player_move == 'E' and player.currentRoom.e_to == None or player_move == 'S' and player.currentRoom.s_to == None or player_move == 'W' and player.currentRoom.w_to == None:
            print('This seems to be the wrong way, please choose a different direction')

        elif player_move == 'Q':
            print("Good bye!")
            game_over = True



    # else:
    #     print('Invalid command, please choose from the given options')
