# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, cur_room, lvl=0, char_class=None):
        self.name = name
        self.char_class = char_class
        self.cur_room = cur_room
        self.lvl = lvl