# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    
    def move(self,direction):
        if self.current_room.connections[direction] is not None:
            self.room = self.room.connections[directions]
        else:
            print("You sense something in a different direction.")

    def take (self, item_name):
        search room inventory for item
        if no item:
            print error message 
        else:
            room.list.remove
            self.inventory.append()
        print("You picked up {item}. {Description}")

    def drop (self, item_name):
        search player inventory for item_name
        if no item:
            print error message
        else:
            self.inventory.remove()
            room.inventory.append()
        print("You dropped {item_name}")
    



#Steps in the Process
'''
Step 1: run the program

Step 2: Put in their name
input() + prompt

Step 3: Show the Outside room dialogue:
Tell the computer the player is in the room, display room dialogue

Step 4: Ask them where they want to go? 
show layout of rooms? 
receive player input()
move player to the room

Step 5: They arrive at the foyer
display the foyer description. 
display list of foyer items
display list of player inventory
display [i] shortcut 
prompt for direction input

Step 6: Items that they need to interact in specs? 
display list of room items
display item name, and description. 
if player uses 2 word command for item:
    check if item is in room
        if yes: take item from room list, add to player list
            print(ontake message "You have picked up blah")
        if not: print an error message telling the user. 
        if player drops item: 
            put item in Room list.
check if player is ready to move on?
prompt for direction?
move player to direction.

Step 7: Next room. What directions they can go?
Any room that isn't the treasure room: 
-display the name, description
-prompt for any item interactions needed
-item interaction mechanics
-directions prompts given
-player move based on input

Step 8: Find the room with the treasure in it. 
-display the name, description
-display the treasure
-interactions w/ treasure
Step 9: You won/You died conditions
-You won! Exit Program/Try Again
Step 10: Exit program
'''