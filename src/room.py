# Implement a class to hold room information. This should have name and
# description attributes.

import item
class Room(object):
    def __init__(self, name, description, is_light = False, items = []):
        self.name = name
        self.description = description
        self.items = items
        self.is_light = is_light
