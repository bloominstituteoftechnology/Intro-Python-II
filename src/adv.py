from room import Room
from player import Player
from item import Item

#declare all rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons",
                     [Item('Lantern','Provides light')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
[Item('stick','provides meager defense'), Item('Pile of Rat turds','see if your that type who likes to pick up everything')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
[Item('Coin',' buy items')])
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


# Make a new player object that is currently in the 'outside' room.
player1 = Player('Player 1', room['outside'])


print(f'Hello {player1.name}! Ready to play the game?')

while True:
    print(player1.current_room.name)
    print(player1.current_room.description)
    if len(player1.current_room.items) != 0:
        items_list = player1.current_room.items.copy()
        for item in items_list:
            approved_ans = False
            print(f"You Found:\n{item.name} to {item.description}")
            while approved_ans is False:
                ans = input('Pick up item?(y/n):')
                if ans == 'y':
                    player1.items.append(item)
                    player1.current_room.items.remove(item)
                    approved_ans = True
                elif ans == 'n':
                    approved_ans = True
                else:
                    print('Choose yes or no!') 


        #player's inventory
        items_list = []
        for item in player1.items:
            items_list.append(item.name)
        print(f'Your Inventory:{str(items_list)[1:-1]}')


        #for player to be able to manage
        approved_ans = False
        while approved_ans is False:
            ans = input('Manage Inventory? (y/n):')
            if ans == 'y':
                approved_ans == True
                items_list = player1.items.copy()
                for item in items_list:
                    rem = input(f'Remove {item.name}?(y/n):')
                    if rem == 'y':
                        player1.items.remove(item)
                        player1.current_room.item.append(item)
                        item_list = []
                        for item in player1.items:
                            item_list.append(item.name)
                        print(f'Your Inventory:{str(item_list)[1:-1]}')
                    elif rem == 'n':
                        pass
                    else:
                        pass
            elif ans == 'n':
                approved_ans = True
            else:
                print('Choose yes or no!')




    #if room has no items
    else:
        print('No items to be found in this room...')
    direction = input('Which direction do you move?(n, s, e, w), to quit press q:')
    if direction == 'n':
        try:
            player1.current_room = player1.current_room.n_to
        except:
            print('Ran into a wall silly')    
    if direction == 's':
        try:
            player1.current_room = player1.current_room.s_to
        except:
            print('Ran into a wall silly')
    if direction == 'e':
        try:
            player1.current_room = player1.current_room.e_to
        except:
            print('Ran into a wall silly')    
    if direction == 'w':
        try:
            player1.current_room = player1.current_room.w_to
        except:
            print('Ran into a wall silly')        
    if direction == "inventory":
        item_list = []
        for item in player1.items:
            item_list.append(item.name)
        print(f'Your Inventory:{str(item_list)[1:-1]}')
    if direction == 'q':
        break        
