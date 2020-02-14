from player import Player
from room import Room 

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     "sword"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", "axe"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "club"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "shield"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "wand"),
}


room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


ri = Room('overlook', 'a room', 'an axe')
print(ri.items)

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

# If the user enters "q", quit the game.




player = Player(input("What is your name? "), room['outside'])

print(f"Hello, {player.name}.")



#### Final version, refactoring code, and follwing "fat models, skinny controllers" - created travel class in 'player.py'

print(player.current_room)
while True:
    cmd = input("-->").lower()
    if cmd in ["n", "s", "e", "w"]:   
        # move to that room
        player.travel(cmd)   
    elif cmd == "q": 
        print('goodbye')
        exit()
    else: 
        print("I did not understand that command")





# player = Player(input("What is your name? "), room['outside'])

# print(f"Hello, {player.name}.")


# while True:
#     print(player.current_room)
#     cmd = input("-->")
#     if cmd in ["n", "s", "e", "w"]: 
#         current_room = player.current_room
#         next_room = getattr(current_room, f"{cmd}_to")
#         if next_room is not None: 
#             player.current_room = next_room
#         else: 
#             print("You cannot move in that direction")         
#     elif cmd == "q": 
#         exit()
#     else: 
#         print("You cannot move there!")

        

#### Naive attempt done in class and then reproduced with recorded lecture, "final" version is above 


# while True:
#     print(player.current_room)
#     cmd = input("-->")
#     if cmd in ["n", "s", "e", "w"]: 
#         print("MOVE " + cmd)
#         if cmd == "n": 
#             if player.current_room.n_to is not None: 
#                 player.current_room = player.current_room.n_to
#             else: 
#                 print('You cannot move in that direction')
#         if cmd == "s": 
#             if player.current_room.s_to is not None: 
#                 player.current_room = player.current_room.s_to
#             else: 
#                 print('You cannot move in that direction')
#         if cmd == "e": 
#             if player.current_room.e_to is not None: 
#                 player.current_room = player.current_room.e_to
#             else: 
#                 print('You cannot move in that direction')
#         if cmd == "w": 
#             if player.current_room.w_to is not None: 
#                 player.current_room = player.current_room.w_to
#             else: 
#                 print('You cannot move in that direction')
         
#     elif cmd == "q": 
#         exit()
#     else: 
#         print("You cannot move there!")







#### My attempt, managed to code the "move" logic but not to link the rooms in a "closed loop" fashion




# move = input("your turn to move:")
# while not move == "q":

#     if move == "n":
#         current_room = room.n_to
#         print(current_room)
        
#     else: 
#         print("You cannot move there")
#     break 

# move = input("your turn to move:")
# while not move == "q":

#     if move == "n":
#         print("You have entered the Overlook")
#         move = input("your turn to move:")
#         while not move == "q":
#             if move == "e":
#                 print("You have reached the Treasure room")
#                 move = input("your turn to move:")
#                 while not move == "q":
#                     if move == "s":
#                         print("You have reached the Narrow room")
#                         break
#                     elif move == "w":
#                         print("You have reached the Overlook room") 
#                     else:
#                         print("You cannot move there")



#             elif move == "s": 
#                 print("You have reached the Foyer room")
#             else: 
#                 print("You cannot move there")
#             break
        
#     elif move == "e":
#         print("You have entered the Narrow room")
#     elif move == "s":
#         print("You have entered the Outside room")
#     else: 
#         print("You cannot move there")
#     break





# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
