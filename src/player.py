# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
    def __init__(self, name, current_room, items):
        self.name = name
        self.current_room = current_room
        self.items = []
        
# get item 
    def getItem(self, item):
        return self.items.append(item)
    
# drop item 
    def dropItem(self, item):
        return self.items.remove(item)

# return item to current_room 
    def __repr__(self):
        return(f'Welcome to {self.current_room}')

        
    
