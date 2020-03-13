"""
BeWilder - text adventure game :: Game tests

All tests implemented in Pytest.
"""

# Third-party imports
import pytest

# Local imports
from .room import Room
from .player import Player


narrow_name = "Narrow Passage"

narrow_description = """The narrow passage bends here from west
to north. The smell of gold permeates the air."""


def test_room_instance():
    # Instantiate the room
    room = Room(narrow_name, narrow_description)
    assert isinstance(room, Room)


def test_player_instance():
    # Instantiate the player
    room = Room(narrow_name, narrow_description)
    player = Player("Tobias", room)

    assert isinstance(player, Player)
