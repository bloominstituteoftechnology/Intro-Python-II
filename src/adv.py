from room import Room
from player import Player
from monster import Monster
# from fight import fight
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Ramiro',room['outside'])
monster  = Monster(room['treasure'])

possible_moves = ['n','s','e','w']
def fight():
    global player
    global monster
    while True:
        action = input('A monster has appeared!! Fight or flee? \n ')

        if action == 'fight':
            monster.attack(player)
            print(f'the monstter has attacked you! your hp: {player.max_hp}')
            player.attack(monster)
            print(f' YOUR ATTACK ITS EFFECTIVE MONSTER HP: {monster.hp}')

        if action == 'flee':
            break

        if monster.hp <= 0:
            print('you killed the monster! \n')
            player.exp +=10
            print(f'{player.name} has gained 10 exp!\n')
            break

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

# print(f'''
#         Welcome to The Game!!!! o.o
#     Player Name: {player.name}
#     Current Room: {player.current_room.name}
#         press 'q' to quit at any time

# ''')
# move = input(f'{player.current_room.description}')
print(f'''
        Welcome to The Game!!!! o.o
    Player Name: {player.name}
    Current Room: {player.current_room.name}
        press 'q' to quit at any time
        press 'i' to get the stats of the player
''')
    
while True:

    player.lvl_up()
    
    move = input(f'{player.current_room.description} >> \n').strip().lower().split()[0]
    move = move[0]

    if move == 'q':
        break

    if move in possible_moves:
        player.try_movement(move)

    if move == 'i':
      print(player.stats())

    if player.current_room.name == 'Treasure Chamber':
        print('A MONSTER IS IN HERE!!')
        fight()
    
    
      
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    # elif move == 'move north':
    #     player.current_room = room['outside'].n_to
    #     print(f'{player.current_room.description} >>')


    # # else:
    # #     continue 


    # if move == 'move south':
    #     player.current_room = room['foyer'].s_to
    #     print(f'{player.current_room.description} >>')

    # elif move == 'move east':
    #     player.current_room = room['foyer'].e_to
    #     print(f'{player.current_room.description} >>')

    # elif move == 'move north' and player.current_room.name == 'foyer':
    #     player.current_room = room['foyer'].n_to
    #     print(f'{player.current_room.description} >>')

    # if move == 'move west':
    #     player.current_room = room['narrow'].w_to
    #     print(f'{player.current_room.description} >>')
    
    # elif move == 'move north' and player.current_room.name == 'narrow':
    #     player.current_room = room['narrow'].n_to
    #     print(f'{player.current_room.description} >>') 




    # else:
    #     print('invalid move')    




