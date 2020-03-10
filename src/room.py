
class Room:
	def __init__(self, name, description):
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

		self.items = []

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
