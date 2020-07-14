# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__ (self, name, room):
        self.name = name
        self.room = room
        self.score = []
        self.path = []
        self.inventory = []

    def move (self, room):
         self.room = room
         self.score.append(1)
         self.path.append(room)  

    def take_item (self, item):
        self.inventory.append(item)
    
    def drop_item (self, item):
        self.inventory.remove(item)  



    






