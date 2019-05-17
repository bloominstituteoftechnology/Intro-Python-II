# Write a class to hold player information, e.g. what room they are in
# currently.
class player:
    def __init__(self, name, desc, satchel, location):
        self.name = name
        self.desc = desc
        self.satchel = satchel
        self.location = location


    def __repr__(self):
        return 