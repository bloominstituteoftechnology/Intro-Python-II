# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
	"""docstring for Player"""
	def __init__(self, name, room):
		self.name = name
		self.current_room = room
		self.items = []

	def moveTo(self, direction):
		if direction == 'n':
			if self.current_room.n_to != None:
				self.current_room = self.current_room.n_to
			else:
				print("Can't go to the North...")
		elif direction == 's':
			if self.current_room.s_to != None:
				self.current_room = self.current_room.s_to
			else:
				print("Can't go to the North...")
		elif direction == 'e':
			if self.current_room.e_to != None:
				self.current_room = self.current_room.e_to
			else:
				print("Can't go to the North...")
		else:
			if self.current_room.w_to != None:
				self.current_room = self.current_room.w_to
			else:
				print("Can't go to the North...")
		
	def addItem(item):
		# BUG: have to pass in an item not string value
		if item in self.current_room.items:
			self.items.append(item)
			item.onTake()
			self.current_room.removeItem(item)
		else:
			print(f"{item} does not exist in the room.")

	def dropItem(item):
		if item in self.items:
			self.items.remove(item)
			self.current_room.addItems(item)
		else:
			print(f"{self.name} do not hold {item}.")