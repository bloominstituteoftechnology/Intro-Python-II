# Class to manage the rooms' title, descriptions, and items
class Room:

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.__items = []

    def __repr__(self):
        print(f"-" * 40)
        return (f"You are at the {self.title}.")
    # Method to add an item to a room

    def add_item(self, item):
        return self.__items.append(item)
    # Method to list items in a room.

    def list_items_in_room(self):
        return self.__items
