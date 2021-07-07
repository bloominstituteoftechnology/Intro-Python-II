# Write a class to store item information

class Item:
    """Consumable trinkets to scatter around the dungeon"""
    def __init__(self, name, description, usage):
        self.name = name
        self.description = description
        self.usage = usage