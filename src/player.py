# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
	def __init__(self, name, current_room, has_backpack = False, items = []):
		self.name = name
		self.current_room = current_room
		self.has_backpack = has_backpack
		self.items = items

	def take_item(self, item):

		if item.name == "Backpack":
			self.has_backpack = True

		if len(self.items) <= 2 or self.has_backpack == True:
			self.items += [item]
			return True
		else:
			return False

	def drop_item(self, item):

		if item.name == "Backpack":
			self.has_backpack = False

		for i in self.items:
			if i.name == item.name:
				self.items.remove(item)