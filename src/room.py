# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f"room name: {self.name}, room description: {self.description}. \n"

    # def print_room(self, name, description):
    #     self.name = name
    #     self.description = description
    #     print(f'Room name: {name}, room description: {description}')


# room = Room("hello", "something")
# room.print_room("hello", "something")
