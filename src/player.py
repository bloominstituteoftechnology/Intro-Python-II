from room import Room


class Player():
    def __init__(self, name, current_room, inventory = []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def room_info(self):
        name = self.current_room.name
        description = self.current_room.description
        return f'{name} - {description}'

    def investigate(self):
        items = self.current_room.items
        if items != None:
            return f'--- You see a {items}.'
        else:
            return "--- There is nothing here."
