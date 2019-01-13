# Class to manage a players name, current room, and items
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.__items = []

    def __repr__(self):
        if self.__items == []:
            return f"Name: {self.name}"
        else:
            return f"Name: {self.name}\nItems: {self.__items}"
    # Method to look in the player's current room for items

    def look(self):
        return f"{self.current_room.description}\nItems: {self.current_room.list_items_in_room()}"
