# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, room_name, room_description):
        self.room_name = room_name
        self.room_description = room_description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.basement_to = None

    def __str__(self):
        return f'you are {self.room_name} \n {self.room_description}'
