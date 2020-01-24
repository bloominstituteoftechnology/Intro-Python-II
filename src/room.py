# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
       

    def __str__(self):
        return f"{self.name} : {self.description}"
        
    def get_roomname(self):
        return self.name

    def set_roomname(self, new_name):
        return self.name = new_name

    def get_description(self):
        return self.description

    def set_description(self, new_description):
        return self.description = new_description
    
   