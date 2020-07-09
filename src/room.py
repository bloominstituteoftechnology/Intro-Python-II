# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
	"""docstring for Room"""
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.n_to = None
		self.s_to = None
		self.e_to = None
		self.w_to = None
		self.items = []

	def addItems(self, *newItems):
		for item in newItems:
			self.items.append(item)
			
	def removeItem(self, item):
		if item in self.items:
			self.items.remove(item)
		else:
			print(f"{item} does not exist in this room.")

	def displayItems(self):
		for item in self.items:
			print(item)