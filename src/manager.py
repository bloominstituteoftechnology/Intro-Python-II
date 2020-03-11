
from player import Player
from room import Room
from items import Item
from errors import IllegalMoveError, NotEnoughItemsError, IllegalCountError


def create_rooms():
	# Declare all the rooms

	room = {
		'outside': Room(
			"Outside Cave Entrance",
			"North of you, the cave mount beckons"
		),
		'foyer': Room(
			"Foyer",
			"Dim light filters in from the south. Dusty passages run north and east."
		),
		'overlook': Room(
			"Grand Overlook",
			"A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."
		),
		'narrow': Room(
			"Narrow Passage",
			"The narrow passage bends here from west to north. The smell of gold permeates the air."
		),
		'treasure': Room(
			"Treasure Chamber",
			"You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."
		),
	}

	# Link rooms together

	room['outside'].n_to = room['foyer']
	room['foyer'].s_to = room['outside']
	room['foyer'].n_to = room['overlook']
	room['foyer'].e_to = room['narrow']
	room['overlook'].s_to = room['foyer']
	room['narrow'].w_to = room['foyer']
	room['narrow'].n_to = room['treasure']
	room['treasure'].s_to = room['narrow']
	room['outside'].add_items(
		item=Item('rock', 'A fist-sized rock lies on the path.')
	)

	return room


class AdventureManager:
	directions = ['n', 's', 'e', 'w']

	def __init__(self):
		self.rooms = create_rooms()
		self.player = Player(self.rooms['foyer'])
		self.describe_current_room()

	def print(self, text: str) -> None:
		'''
		Prints something to the screen.
			Later, this might be modified to allow for fancier effects.

		Args:
			text (str): text to print
		'''

		print(text[0].upper() + text[1:])

	def step(self) -> None:
		'''
		Does a step of the game world.
		'''
		pass

	def get_current_room_summary(self):
		return f'You are currently in the {self.player.current_room.name}.'

	def get_current_room_description(self):
		return self.player.current_room.description

	def describe_current_room(self):
		self.print(self.get_current_room_summary())
		self.print(self.get_current_room_description())

	def move_player(self, direction: str, direction_name: str = None) -> None:
		'''
		Moves the player.

		Args:
			direction (str): Direction to move.
			direction_name (str, optional): The name of the direction you moved.
		'''

		if direction_name is None:
			direction_name = direction

		try:
			self.player.move(direction)

			self.print(f'You move {direction_name}...')
			self.describe_current_room()

			self.step()

		except IllegalMoveError:
			self.print(f'You can\'t move {direction_name}.')

	def player_take(self, item_name, count):
		try:
			item = self.player.current_room.get_item_by_name(item_name)
			self.player.transfer_items_from(self.player.current_room, item, count=count)
			self.print(f'Picked up {count} of {item_name}.')
		except KeyError:
			self.print(f'There\'s not a {item_name} here!')
		except NotEnoughItemsError:
			self.print(f'There aren\'t enough of {item_name} here to take {count}.')
		except IllegalCountError:
			self.print(f'Can\'t take {count} of an item!')

	def player_drop(self, item_name, count):
		try:
			item = self.player.get_item_by_name(item_name)
			self.player.transfer_items_to(self.player.current_room, item, count=count)
			self.print(f'Dropped {count} of {item_name}.')
		except KeyError:
			self.print(f'You don\'t have a {item_name}!')
		except NotEnoughItemsError:
			self.print(f'You don\'t have enough of {item_name} to drop {count}.')
		except IllegalCountError:
			self.print(f'Can\'t drop {count} of an item!')

	def print_player_inventory(self):
		self.print(self.player.print_inventory())
