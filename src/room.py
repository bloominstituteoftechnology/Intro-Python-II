# Implement a class to hold room information. This should have name and
# description attributes.
from lib import Description

class Room(Description):
	def __init__(self, name, description, storage = []):
	  super().__init__(name, description, storage = storage)
	  self.n_to = None
	  self.e_to = None
	  self.s_to = None
	  self.w_to = None
