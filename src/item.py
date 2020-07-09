class Item:
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def __str__(self):
		return f"{self.name}: {self.description}"

	def onTake(self):
		print(f"You have picked up {self.name}.")

	def onDrop(self):
		print(f"You have dropped {self.name}.")


class Food(Item):
	def __init__(self, name, description, calory):
		super().__init__(name, description)
		self.calory = calory

class Weapon(Item):
	def __init__(self, name, description, damage):
		super().__init__(name, description)
		self.damage = damage