# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self._current_room = current_room

    def __str__(self):
        return f"Current Room: {self._current_room}"

    def _set_current_room(self, current_room):
        self._current_room = current_room

    def _get_current_room(self):
        return self._current_room

    current_room = property(_get_current_room, _set_current_room)