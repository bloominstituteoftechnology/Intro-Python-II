# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
    def __str__(self):
        return f"My name is {self.name}. I'm currently holding {self.inventory}."
