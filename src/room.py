# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, room_name, room_description, room_items=[]):
        self.room_name = room_name
        self.room_description = room_description
        self.room_items = room_items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.basement_to = None

    def __str__(self):
        output = f"{self.room_name} \n {self.room_description}  "
        for i in self.room_items:
            output += f"\n - {i}"
        return output
