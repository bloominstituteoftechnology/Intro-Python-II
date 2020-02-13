from src.directions import Direction
import typing
from typing import Any, List, Dict, Union, Optional, Type


# Implement a class to hold room information. This should have name and
# description attributes.


class Room():

    def __init__(
            self,
            room_name: str,
            description: str,
            nearby_rooms: Dict[Direction, Any] = {}
    ):
        self.room_name = room_name
        self.description = description
        self.nearby_rooms = nearby_rooms

    def get_nearby_room(self, direction: Direction):
        if direction in self.nearby_rooms:
            return self.nearby_rooms[direction]
        else:
            return None

