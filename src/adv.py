from room import Room
from player import Player
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

room['outside'].addItem('sword')
room['outside'].addItem('cape')
room['outside'].addItem('goldpile')

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

player = Player("Aaron", room["outside"])


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

# print(player.room.name)
# print(player.room.description)
# print(player.room.items)

# userInput = input('Input a movement direction (n,w,s,e) press "q" to quit ')

# while userInput != 'q':
    

#     if(userInput not in ['n', 'w', 's', 'e', 'q']):

#         userInput = input('please enter valid input press "q" to quit ')
        
#     elif(not hasattr(player.room, f'{userInput}_to') and userInput != 'q'):

#         print(userInput)
#         userInput = input('you cannot move in that direction: Choose another press "q" to quit ')

#     elif(userInput != 'q'):

#         player.room = getattr(player.room, f'{userInput}_to')
#         print(player.room.name)
#         print(player.room.description)
#         print(player.room.items)

#         userInput = input('Input a movement direction (n,w,s,e) press "q" to quit ')

# print('done')




class Game(): 
   
    def __init__(self):
       self.commandMap = {
           'n': self.move,
           'w': self.move,
           's': self.move,
           'e': self.move,
           'drop': self.dropItem,
           'pickup': self.pickupItem,
           'q': self.quit
       }
    
    def printState(self, player):

        print(player.room.name)
        print(player.room.description)
        print('item', player.room.items)
        print('inventory', player.inventory)

        return input('Input a movement direction (n,w,s,e) press "q" to quit ')


    def move(self, player, userInput):

        print(player, userInput[0])
        
        if(not hasattr(player.room, f'{userInput[0]}_to')):
            return input('you cannot move in that direction: Choose another press "q" to quit ')
        else:

            player.room = getattr(player.room, f'{userInput[0]}_to')

            return self.printState(player)

            
    def dropItem(self, player, commands):

        player.removeItem(commands[1])
        player.room.addItem(commands[1])
        
        return self.printState(player)

        

    def pickupItem(self, player, commands): 

        player.addItem(commands[1])
        player.room.removeItem(commands[1])

        return self.printState(player)

        
    
    def quit(self, *args): 
        return 'q'


    def issueCommand(self, userInput, player):
        
        commands = userInput.split(" ")

        if(commands[0] in self.commandMap.keys()):

            nextCommand = self.commandMap[commands[0]](player, commands)
    
            if nextCommand == 'q': return

            else: self.issueCommand(nextCommand, player)

        else:
            
            userInput = input('please enter valid input press "q" to quit ')
            self.issueCommand(userInput, player)


gameInstance = Game()

print(player.room.name)
print(player.room.description)
print(player.room.items)

userInput = input('Input a movement direction (n,w,s,e) or press "q" to quit ')

gameInstance.issueCommand(userInput, player)

print("done")  




