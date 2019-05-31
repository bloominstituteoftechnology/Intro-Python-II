# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room, items=[]):
        self.name = name
        self.room = room
        self.items = items

    def __str__(self):
        return f"{self.name} reporting in and I'm lugging around {self.items}."
