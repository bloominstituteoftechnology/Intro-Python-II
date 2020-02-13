from src.directions import Direction
import typing
from typing import Any, List, Dict, Union, Optional, Type


# Implement a class to hold room information. This should have name and
# description attributes.


class Room:

    def __init__(
            self,
            room_name,
            description,
            nearby_rooms: Optional[Dict[Direction, Any]] = None
    ):
        self.room_name = room_name
        self.description = description
        self.nearby_rooms = nearby_rooms

    def set_nearby_room(self, room_position: Direction, nearby_room):
        self.nearby_rooms[room_position] = nearby_room

    def get_nearby_room(self, direction: Direction):
        return self.nearby_rooms.get(direction, None)
