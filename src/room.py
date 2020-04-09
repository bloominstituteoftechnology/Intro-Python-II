
from inventory import Inventory


class Room(Inventory):
	direction_inverses = {
		'n': 's',
		's': 'n',
		'w': 'e',
		'e': 'w',
	}

	def __init__(self, name, description):
		super().__init__()
		self.name = name
		self.description = description

		self.n_to = None
		self.e_to = None
		self.w_to = None
		self.s_to = None

		self.directionals = {
			'n': self.n_to,
			's': self.s_to,
			'e': self.e_to,
			'w': self.w_to,
		}

	def get_direction(self, direction):
		return self.directionals[direction]

	def connect_to(self, other, outgoing_direction, incoming_direction=None):
		if incoming_direction is None:
			incoming_direction = self.direction_inverses[outgoing_direction]
		self.directionals[outgoing_direction] = other
		other.directionals[incoming_direction] = self

	def print_items(self):
		items_str = 'On the ground, there is:'
		if len(self.items):
			for item in self.items.values():
				items_str += f'\n- {str(item)}'
		else:
			items_str += '\n- Nothing but dust bunnies.'
		return items_str



