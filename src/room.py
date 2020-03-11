
from inventory import Inventory


class Room(Inventory):
	def __init__(self, name, description):
		super().__init__()
		self.name = name
		self.description = description

		self.n_to = None
		self.e_to = None
		self.w_to = None
		self.s_to = None

		self.directionals = {
			'n': self.get_n,
			's': self.get_s,
			'e': self.get_e,
			'w': self.get_w,
		}

	def get_direction(self, direction):
		return self.directionals[direction]()

	def get_n(self):
		return self.n_to

	def get_s(self):
		return self.s_to

	def get_w(self):
		return self.w_to

	def get_e(self):
		return self.e_to

	def print_items(self):
		items_str = 'On the ground, there is:'
		if len(self.items):
			for item in self.items.values():
				items_str += f'\n- {str(item)}'
		else:
			items_str += '\n- Nothing but dust bunnies.'
		return items_str



