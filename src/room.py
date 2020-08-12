# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, roomName, description):
        self.roomName = roomName
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"{self.roomName}\n\n{self.description}"
