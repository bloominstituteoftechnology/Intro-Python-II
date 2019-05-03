# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.current_room = current_room
        self.name = name
        self.inventory = []
    def __str__(self):
        return f'{self.name} is in {self.current_room}.'
    def add_item(self, item):
        self.inventory.append(item)
    def get_name(self):
        return str(self.name)
    def get_current_room(self):
        return str(self.current_room)

        
# class Player(NameStorage):
#     def __init__(self, name, current_room, storage=[]):
#         super().init__(name, storage = storage)
#         self.current_room = current_room

