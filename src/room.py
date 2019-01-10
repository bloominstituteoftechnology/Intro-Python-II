# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, area, description, inventory=[]):
        self.area = area
        self.description = description
        self.inventory = inventory

    def __repr__(self):
        return f'Area: {self.area}, Description: {self.description}, Items: {self.inventory}'