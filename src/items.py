
from errors import EmptyStackException


class Item:
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def examine(self):
		return self.description

	def __str__(self):
		return self.name


class ItemStack:
	def __init__(self, item: Item, count: int = 1):
		self.item = item
		self.count = count

	def __str__(self):
		if self.count < 1:
			raise EmptyStackException
		elif self.count == 1:
			return f'a single {self.item}.'
		else:
			return f'{self.count} of {self.item}.'

