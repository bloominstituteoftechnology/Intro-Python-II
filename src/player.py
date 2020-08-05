# Write a class to hold player information, e.g. what room they are in
# currently.

# 1. create class and give the minimum that player must have
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location