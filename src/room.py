# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, roomname, description):
        self.roomname = roomname
        self.description = description
       

    def __str__(self):
        return f"{self.roomname} : {self.description}"
        
    def get_roomname(self):
        return self.roomname

    def set_roomname(self, new_name):
        self.roomname = new_name

    def get_description(self):
        return self.description

    def set_description(self, new_description):
        self.description = new_description
    
   