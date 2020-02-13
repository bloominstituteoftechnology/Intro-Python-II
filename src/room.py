from src.directions import Direction
import typing
from typing import Any, List, Dict, Union, Optional, Type
from src.item import Item

# Implement a class to hold room information. This should have name and
# description attributes.


class Room():

    def __init__(
            self,
            room_name: str,
            description: str
    ):
        self.room_name = room_name
        self.description = description
        self.nearby_rooms = {}
        self.items = []

    def get_nearby_room(self, direction: Direction):
        return self.nearby_rooms.get(direction, None)
