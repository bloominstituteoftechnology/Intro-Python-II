# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
	def __init__(self, name, description):
		self.name = name
		self.description = description

		self.n_to = False
		self.s_to = False
		self.e_to = False
		self.w_to = False

	def __str__(self):
		return (f"Room: {self.name}\nDescription: {self.description}")
