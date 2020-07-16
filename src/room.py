# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def print_current_location(self):
        print(f'\nCurrently in room: {self.current_room.name}\n')
        print(f"{self.current_room.description}\n")