from room import Room
from player import Player
from item import Item
#make the room and player class DONE
#set up the REPL to move in the 4 directions look at this to accomplish:
##setup of rooms:
#             'outside'
# 'narrow'    'foyer'
# 'treasure'  'overlook'

#REPL steps

#make player object
#set loop
#set conditionals for all situations s, n, e, w





# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('sword', 'to cut'), Item('map', 'to find your way silly')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('lantern', 'to light up the rooms')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('token', 'get a free cone of ice cream at Cold Stone Creamery')]),
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
player = Player('outside')
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.


# input('where do you want to move? Press q to quit at any time')

# if u_i == 'q':
#     print('Game over.  See you next time...')
#loop through rooms
while True:
    
    for i in room:
    #initial print and input command
    
        if player.room == i:
            print(room[i].name)
            print(room[i].description)
            ###if it has items do this
            if room[i].items:
                for j in room[i].items:
                    print(f'{i} has the following item: {j}\n\n')
                
                cmd = input('Would you like to move? If so press n for north s for south e for east or w for west.  Would you like to pick up or drop an item?  If so type get (or drop) Item, where item is the name of the item you would like to pick up. Press q to quit at any time: \n\n')
                cmd_determiner = cmd.split()
                #break at any time user enters q for quit
                if cmd == 'q':
                    print('Goodbye!')
                    exit(0)
                ##############################################3333correct for get and leave cases
                #handle improper input
                if cmd != 'q' and cmd != 'n' and cmd != 'e' and cmd != 's' and cmd != 'w' and len(cmd_determiner) == 1 :
                    print('improper command, please read instructions CAREFULLY!!  BOOLEAN THUNDER ERROR 55-2234cD\n\n')
                #so long as they don't quit and proper commands: 

                da_length = len(cmd_determiner)
            
                if da_length == 2 and cmd_determiner[0] == 'get':
                    for item in room[i].items:
                        if item.name not in room[i].items and not cmd_determiner:
                            print('You must pick up an item that is ACTUALLY IN THE ROOM!!!\n\n')
                                    
                        if item.name == cmd_determiner[1]:
                                    #make a method to call here to pick up the item:
                                    #method will remove the item from the room, and add it to the players inventory and print that they picked it up
                            player.get_item(item)
                            item.on_take()
                            room[i].remove_item(cmd_determiner[1])
                            ##onTake
                            
                            print(f'You have just picked up the {cmd_determiner[1]}\n\n')
######################################################################################################33333
                if da_length == 2 and cmd_determiner[0] == 'drop':

                    for item in player.items:
                        print(player.items)
                        if not getattr(item, cmd_determiner[1]):
                            print("do not try to drop what you don't have")

                                    
                        if item.name == cmd_determiner[1]:
                                    #make a method to call here to pick up the item:
                                    #method will remove the item from the room, and add it to the players inventory and print that they picked it up
                            player.drop_item(item)####################3make this!!!!!!!!!!!!!!!!!!!!
                            item.on_drop()
                            room[i].add_item(item)#######################make this
                            ##onTake
                            
                            print(f'You have just picked up the {cmd_determiner[1]}\n\n')
##################################################################################################3333


                elif cmd == 's' and player.room == 'outside':
                    player = Player('foyer')
                    print("you have now moved to the foyer")
                elif cmd == 'w' and player.room == 'outside':
                    print('You cannot move west from outside dummy')
                elif cmd == 'e' and player.room == 'outside':
                    print('You cannot move east from outside dummy')
                elif cmd == 'n' and player.room == 'outside':
                    print('You cannot move north from outside dummy')

                elif cmd == 's' and player.room == 'foyer':
                    player = Player('overlook')
                    print("you have now moved to the overlook")
                elif cmd == 'w' and player.room == 'foyer':
                    player = Player('narrow')
                    print('You have now moved to the narrow')
                elif cmd == 'e' and player.room == 'foyer':
                    print('you cannot move east from the foyer dummy')
                elif cmd == 'n' and player.room == 'foyer':
                    player = Player('outside')
                    print('You have now moved outside')


                elif cmd == 's' and player.room == 'overlook':
                    print('You cannot move south from overlook dummy')
                elif cmd == 'w' and player.room == 'overlook':
                    player = Player('treasure')
                    print('You have now moved to the treasure room!')
                elif cmd == 'e' and player.room == 'overlook':
                    print('you cannot move east from the overlook dummy')
                elif cmd == 'n' and player.room == 'overlook':
                    player = Player('foyer')
                    print('You have now moved to the foyer')

                elif cmd == 's' and player.room == 'narrow':
                    player = Player('treasure')
                    print('You have now moved to the teasure room!')
                elif cmd == 'w' and player.room == 'narrow':
                    print('You cannot move west from the narrow dummy')
                elif cmd == 'e' and player.room == 'narrow':
                    player = Player('foyer')
                    print('You have now moved to the foyer.')
                elif cmd == 'n' and player.room == 'narrow':
                    print('You cannot move north from the narrow dummy')

                elif cmd != 's' and player.room == 'treasure':
                    print('We just told you the only exit is south dummy.  Game over!')
                    break
                elif cmd == 's' and player.room == 'treasure':
                    print('Good job finding the treasure that is not there.  Game over!')
                    break



            #if it doesn't have items do this
            elif len(room[i].items) == 0:
                cmd = input('Would you like to move? If so press n for north s for south e for east or w for west. Press q to quit at any time\n\n')
                
                
                if cmd == 'q':###########3
                    print('Goodbye!')##########
                    exit(0)
                if cmd != 'q' and cmd != 'n' and cmd != 'e' and cmd != 's' and cmd != 'w':
                    print('improper command, please read instructions CAREFULLY!!  BOOLEAN THUNDER ERROR 55-2234cD')
                #so long as they don't quit and proper commands: 
                elif cmd == 's' and player.room == 'outside':
                    player = Player('foyer')
                    print("you have now moved to the foyer")
                elif cmd == 'w' and player.room == 'outside':
                    print('You cannot move west from outside dummy')
                elif cmd == 'e' and player.room == 'outside':
                    print('You cannot move east from outside dummy')
                elif cmd == 'n' and player.room == 'outside':
                    print('You cannot move north from outside dummy')

                elif cmd == 's' and player.room == 'foyer':
                    player = Player('overlook')
                    print("you have now moved to the overlook")
                elif cmd == 'w' and player.room == 'foyer':
                    player = Player('narrow')
                    print('You have now moved to the narrow')
                elif cmd == 'e' and player.room == 'foyer':
                    print('you cannot move east from the foyer dummy')
                elif cmd == 'n' and player.room == 'foyer':
                    player = Player('outside')
                    print('You have now moved outside')


                elif cmd == 's' and player.room == 'overlook':
                    print('You cannot move south from overlook dummy')
                elif cmd == 'w' and player.room == 'overlook':
                    player = Player('treasure')
                    print('You have now moved to the treasure room!')
                elif cmd == 'e' and player.room == 'overlook':
                    print('you cannot move east from the overlook dummy')
                elif cmd == 'n' and player.room == 'overlook':
                    player = Player('foyer')
                    print('You have now moved to the foyer')

                elif cmd == 's' and player.room == 'narrow':
                    player = Player('treasure')
                    print('You have now moved to the teasure room!')
                elif cmd == 'w' and player.room == 'narrow':
                    print('You cannot move west from the narrow dummy')
                elif cmd == 'e' and player.room == 'narrow':
                    player = Player('foyer')
                    print('You have now moved to the foyer.')
                elif cmd == 'n' and player.room == 'narrow':
                    print('You cannot move north from the narrow dummy')

                elif cmd != 's' and player.room == 'treasure':
                    print('We just told you the only exit is south dummy.  Game over!')
                    break
                elif cmd == 's' and player.room == 'treasure':
                    print('Good job finding the treasure that is not there.  Game over!')
                    break
  

    
  

#             'outside'
# 'narrow'    'foyer'
# 'treasure'  'overlook'


#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.



#REFLECTION Do the following refactors after MVP is met before stretch
#maybe use a helper function to handle all the move commands by checking the room and printing then can do just 4 elifs n e s w and call the function within  