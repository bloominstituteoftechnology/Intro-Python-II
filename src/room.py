# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
	def __init__(self, name, description, items = [], needed_items = [], n_to = None, s_to = None, e_to = None, w_to = None):
		self.name = name
		self.description = description
		self.items = items
		self.needed_items = needed_items
		self.n_to = n_to
		self.s_to = s_to
		self.e_to = e_to
		self.w_to = w_to