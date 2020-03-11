
from manager import AdventureManager
from utils import descendants
from errors import GameExitedException


class CommandManager:
	def __init__(self, adventureManager):
		self.adventureManager = adventureManager
		self.commands_dict = {
			alias: command(self)
			for command in descendants(Command)
			for alias in command.aliases
		}

	def get_command(self, alias: str):
		'''
		Gets a command by its alias and returns an instance of it.
			If an unknown alias is provided, an UnknownCommand instance is returned.

		Args:
			alias (str): Command alias

		Returns:
			Command: A Command instance that has that alias
		'''

		return self.commands_dict.get(alias, UnknownCommand(self))

	def execute(self, text):
		args = text.lower().strip().split()
		if len(args) == 0:
			return

		try:
			command = self.get_command(args[0])
			command.execute(*args)
		except Exception as e:
			if isinstance(e, GameExitedException):
				raise
			elif isinstance(e, KeyboardInterrupt):
				raise GameExitedException
			else:
				FailedCommand(self).execute(*args)


class Command:
	'''
	ABC for input commands.
	'''

	aliases = []

	def __init__(self, commandManager: CommandManager):
		self.commandManager = commandManager
		self.adventureManager = commandManager.adventureManager

	def execute(self, *args) -> None:
		raise NotImplementedError

	def help(self, *args) -> str:
		return f'No help available for command {args[0]}.'


class Help(Command):
	aliases = ['help', 'h', '?']

	def __init__(self, commandManager: CommandManager):
		self.command_list = []
		for command in descendants(Command):
			if len(command.aliases):
				self.command_list.append(command.aliases[0])
		super().__init__(commandManager)

	def execute(self, *args) -> None:
		if len(args) > 1:
			self.adventureManager.print(
				self.commandManager.get_command(args[1]).help(*args[1:])
			)
		else:
			help_list = 'Available commands:'
			for command_name in self.command_list:
				help_list = help_list + f'\n{command_name}'
			self.adventureManager.print(
				help_list
			)

	def help(self, *args) -> str:
		return 'Usage: help [command [arg0] [arg1] ...]\n' + \
			f'Retrieve a list of commands, or detailed help on a command.\n' + \
			f'Aliases: {", ".join(self.aliases)}'


class FailedCommand(Command):
	def execute(self, *args):
		self.adventureManager.print(
			f'Failed to execute command string: {" ".join(args)}'
		)


class UnknownCommand(Command):
	def execute(self, *args) -> None:
		self.adventureManager.print(
			f'Unknown command {args[0]}. Try "help".'
		)

	def help(self, *args) -> str:
		return f'No command with alias `{args[0]}` exists!'


# class StepCommand(Command):
# 	def execute(self, *args) -> None:
# 		self.adventureManager.step()


class Quit(Command):
	aliases = ['quit', 'exit', 'q']

	def execute(self, *args) -> None:
		raise GameExitedException

	def help(self, *args) -> str:
		return 'Usage: exit\n' + \
			f'Exits the game.\n' + \
			f'Aliases: {", ".join(self.aliases)}'


class Wait(Command):
	aliases = ['wait', 'skip']

	def execute(self, *args):
		try:
			if len(args) > 1:
				steps = int(args[1])
			else:
				steps = 1

			for _ in range(steps):
				self.adventureManager.step()

			self.adventureManager.print('You do nothing, for a time.')

		except Exception:
			self.adventureManager.print(
				self.help(*args)
			)

	def help(self, *args) -> str:
		return 'Usage: wait [steps]\n' + \
			f'Waits `steps` turns, or 1 if `steps` omitted.\n' + \
			f'Aliases: {", ".join(self.aliases)}'


class Move(Command):
	aliases = ['move', 'go', 'm']

	def __init__(self, commandManager):
		super().__init__(commandManager)
		self.directions = self.adventureManager.directions
		self.direction_commands = {
			alias: command(self)
			for command in [
				MoveEast,
				MoveNorth,
				MoveSouth,
				MoveWest,
			]
			for alias in command.aliases
		}

	def execute(self, *args) -> None:
		try:
			self.direction_commands[args[1]].execute(*args[1:])
		except Exception:
			self.adventureManager.print(
				self.help(*args)
			)

	def help(self, *args) -> str:
		return f'Usage: move direction\n' + \
			f'Directions: {", ".join(self.directions)}.\n' + \
			f'Aliases: {", ".join(self.aliases)}'


class MoveDirection(Command):
	def __init__(self, commandManager):
		super().__init__(commandManager)
		self.directions = self.adventureManager.directions

	def help(self, *args) -> str:
		return f'{", ".join(self.directions)}: Move in a direction.\n' + \
			f'Aliases: {", ".join(self.aliases)}'


class MoveNorth(MoveDirection):
	aliases = ['north', 'n', 'up']

	def execute(self, *args) -> None:
		self.adventureManager.move_player('n', args[0])


class MoveSouth(MoveDirection):
	aliases = ['south', 's', 'down']

	def execute(self, *args) -> None:
		self.adventureManager.move_player('s', args[0])


class MoveWest(MoveDirection):
	aliases = ['west', 'w', 'left']

	def execute(self, *args) -> None:
		self.adventureManager.move_player('w', args[0])


class MoveEast(MoveDirection):
	aliases = ['east', 'e', 'right']

	def execute(self, *args) -> None:
		self.adventureManager.move_player('e', args[0])


class Look(Command):
	aliases = ['look']

	def execute(self, *args):
		self.adventureManager.describe_current_room()

	def help(self, *args):
		return 'Usage: look\n' + \
			f'Look around at the room.\n' + \
			f'Aliases: {", ".join(self.aliases)}'


class Take(Command):
	aliases = ['take', 'get', 'pickup', 'grab']

	def execute(self, *args):
		try:
			count = int(args[1])
			item_name = ' '.join(args[2:])
		except ValueError:
			count = 1
			item_name = ' '.join(args[1:])
		self.adventureManager.player_take(item_name, count)

	def help(self, *args):
		return 'Usage: take [count] item\n' + \
			f'Take one or more of item.\n' + \
			f'Aliases: {", ".join(self.aliases)}'


class Take(Command):
	aliases = ['drop', ]

	def execute(self, *args):
		try:
			count = int(args[1])
			item_name = ' '.join(args[2:])
		except ValueError:
			count = 1
			item_name = ' '.join(args[1:])
		self.adventureManager.player_drop(item_name, count)

	def help(self, *args):
		return 'Usage: drop [count] item\n' + \
			f'Drop one or more of item.\n' + \
			f'Aliases: {", ".join(self.aliases)}'


class CheckInventory(Command):
	aliases = ['inventory', 'inv', 'i']
	# TODO: Make this accept an item name

	def execute(self, *args):
		self.adventureManager.print_player_inventory()

	def help(self, *args):
		return 'Usage: inventory [item]\n' + \
			f'Check how many of [item] you have, or view your full inventory.\n' + \
			f'Aliases: {", ".join(self.aliases)}'

