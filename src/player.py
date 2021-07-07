# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player(Room):
    def __init__(self, name, roomname, description):
        super().__init__(roomname, description)
        self.name = name
    
    def __str__(self):
        room_string = self.name
        i = 1
        for r in self.roomname:
            room_string += f"\n{i}.{r.get_roomname}"
            i+=1
        # return f"{self.name} is in Room {super().__str__()}"
        return room_string

    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name