class Room:
    def __init__(self, room_name, room_description):
        self.room_name = room_name
        self.room_description = room_description
        self.room_items = []
        self.n_to = ""
        self.s_to = ""
        self.e_to = ""
        self.w_to = ""

    def __repr__(self):
        return f'{ self.room_name }'

    def add_item(self, item):
        self.room_items.append(item)
