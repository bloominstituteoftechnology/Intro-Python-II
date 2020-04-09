
from typing import Tuple

from room import Room
from errors import IllegalMoveError
from inventory import Inventory


class Player(Inventory):
	def __init__(self, current_room: Room):
		super().__init__()
		self.current_room = current_room

	def move(self, direction: str) -> Room:
		'''
		Move in a direction.

		Args:
			direction (str): A direction to move.
				One of n, s, e, w.

		Raises:
			IllegalMoveError: If the player can't move that way.

		Returns:
			Room: The new room of the player.
		'''

		new_room = self.current_room.get_direction(direction)
		if new_room is not None:
			self.current_room = new_room
			return self.current_room
		else:
			raise IllegalMoveError

	def print_inventory(self):
		inventory_str = f'Your inventory currently contains:'
		if len(self.items):
			for item in self.items.values():
				inventory_str += f'\n- {str(item)}'
		else:
			inventory_str += '\n- Nothing but dust bunnies.'
		return inventory_str

	def __str__(self):
		return 'you, the player'
