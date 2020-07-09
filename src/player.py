# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def getItem(self, item):
        return self.items.append(item)

    def dropItem(self, item):
        return self.items.remove(item)      

    def __repr__(self):
        return(f"You are {self.current_room}")

        

