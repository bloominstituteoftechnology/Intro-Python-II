class Room:
    def __init__(self, room_name, room_description):
        self.room_name = room_name
        self.room_description = room_description
        self.room_items = []

    def add_item(self, item):
        self.room_items.append(item)
