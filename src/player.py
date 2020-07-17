# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
    def __init__(self, name, current_room, items):
        self.name = name
        self.current_room = current_room
        self.items = []
        
    # def get_item(self, item):
    #     # remove item from current room
    #     self.current_room.remove_item(item)
    #     # add item 
    #     self.items.append(item)
    #     return(f'You now have item {item.name}{item.description}')
    # def __str__(self):
    #     return(f'{self.name} now has items {self.items}')
        

        
    
