
from __future__ import annotations

from items import Item, ItemStack
from errors import NotEnoughItemsError, IllegalCountError


class Inventory:
	def __init__(self):
		self.items = {}

	def get_item_by_name(self, name: str) -> Item:
		return self.items[name].item

	def get_item_count_by_name(self, name: str) -> str:
		item_stack = self.items.get(name, None)
		if item_stack is None:
			return f'no {name}.'
		else:
			return str(item_stack)

	def add_items(self, item: Item, count: int = 1) -> None:
		if count < 1:
			raise IllegalCountError
		if item.name not in self.items:
			self.items[item.name] = ItemStack(item, count=count)
		else:
			self.items[item.name].count += count

	def remove_items(self, item: Item, count: int = 1) -> None:
		if count < 1:
			raise IllegalCountError
		if self.items[item.name].count > count:
			self.items[item.name].count -= count
		elif self.items[item.name].count == count:
			del self.items[item.name]
		else:
			raise NotEnoughItemsError

	def transfer_items_from(self, other: Inventory, item: Item, count: int = 1) -> None:
		try:
			other.remove_items(item, count=count)
			self.add_items(item, count=count)
		except NotEnoughItemsError:
			raise

	def transfer_items_to(self, other: Inventory, item: Item, count: int = 1) -> None:
		other.transfer_items_from(self, item, count=count)

	def __str__(self):
		return 'an unknown inventory'

	def print_inventory(self):
		inventory_str = f'The inventory of {str(self)} currently contains:'
		if len(self.items):
			for item in self.items.values():
				inventory_str += f'\n- {str(item)}'
		else:
			inventory_str += '\n- Nothing but dust bunnies.'
		return inventory_str
