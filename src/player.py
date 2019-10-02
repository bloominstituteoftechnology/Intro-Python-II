# Write a class to hold player information, e.g. what room they are in
# currently.
from typing import Optional
from room import Room
from dataclasses import dataclass

@dataclass
class Player:
    name: str
    current_room: Room
