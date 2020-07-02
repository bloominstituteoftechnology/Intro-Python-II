# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
	def __init__(self, name, description, items = []):
		self.name = name
		self.description = description
		self.items = items

		self.n_to = False
		self.s_to = False
		self.e_to = False
		self.w_to = False

	def __str__(self):
		output = ""
		output += f"Room: {self.name}\n"
		output += f"Description: {self.description}"

		if len(self.items) > 0:
			for index, item in enumerate(self.items):
				output += "\nRoom Item: "+str(item)

		return output
