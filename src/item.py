# Write a class to hold item information

class Item:
	"""
	Class for items. Items may be placed in rooms or placed in a players' inventory.
	"""
	def __init__(self,  name, description):
		self.name = name
		self.description = description
	
	def __str__(self):
		return f"name: {self.name}, description: {self.description}"

