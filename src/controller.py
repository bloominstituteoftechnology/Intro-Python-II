
from manager import AdventureManager
from commands import CommandManager


class Controller:
	'''
	Controls the whole adventure game.
	'''

	prompt = '> '

	def __init__(self):
		self.adventureManager = AdventureManager()
		self.commandManager = CommandManager(self.adventureManager)

	def run_game_loop(self):
		try:
			while True:
				command_string = input(self.prompt)
				self.commandManager.execute(command_string)
		except (Exception, KeyboardInterrupt):
			self.adventureManager.print('\nExiting the game...')



