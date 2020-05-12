from room import Room


class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def room_info(self):
        name = self.current_room.name
        description = self.current_room.description
        return f'{name} - {description}'
