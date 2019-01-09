# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
    def __repr__(self):
        return str(f'{self.name}')