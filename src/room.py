# Implement a class to hold room information. This should have name and
# description attributes.

from drop import Drop
from typing import List


class Room:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

        self.drops: List[Drop] = []

        self.north: Room = None
        self.west: Room = None
        self.east: Room = None
        self.south: Room = None
        