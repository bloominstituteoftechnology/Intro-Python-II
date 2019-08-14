# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
    def __init__(self, name, current_room):
        # self._name = name
        self.name = name
        self.current_room = current_room
    
    def __self__(self):
        return f'Player {self.name} is currently in room {self.current_room}. Keep going!'
        