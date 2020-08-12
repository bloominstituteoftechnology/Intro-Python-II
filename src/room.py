# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.w_to = None
        self.s_to = None
        self.d_to = None
        self.a_to = None
    
    def __str__(self):
        return f"{self.name}\n {self.description}"
