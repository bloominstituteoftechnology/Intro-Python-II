
class Player:
    # initial values set for Player class
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __repr__(self):
        if self.items == []:
            return f"Name: {self.name}"
        else:
            return f"Name: {self.name}\nItems: {self.items} "

    def look(self):
        if self.current_room.items == []:
            return f"{self.current_room.description}"
        else:
            return f"{self.current_room.description}\n {self.current_room.items}"
