
from typing import Tuple

from room import Room


class Player:
	def __init__(self, current_room: Room):
		self.current_room = current_room

	def move(self, direction: str) -> Tuple[bool, Room]:
		'''
		Move in a direction.

		Args:
			direction (str): A direction to move.
				One of n, s, e, w.

		Returns:
			Tuple[bool, Room]: A boolean representing if you successfully moved,
				and the current room of the player.
		'''

		new_room = self.current_room.get_direction(direction)
		if new_room is not None:
			self.current_room = new_room
			return (True, self.current_room)
		else:
			return (False, self.current_room)
