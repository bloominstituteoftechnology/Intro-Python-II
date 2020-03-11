
class GameError(Exception):
	pass


class GameExitedException(GameError):
	'''
	Exception for when the game is exited.
	'''
	pass


class EmptyStackException(GameError):
	'''
	Exception for if there is an empty stack of items.
	'''


class ControlError(GameError):
	'''
	Exception for expected illegal events.
	'''
	pass


class IllegalMoveError(ControlError):
	'''
	Exception for if the player tries to move in an illegal way.
	'''
	pass


class NotEnoughItemsError(ControlError):
	'''
	Exception for if a player tries to do something with more items than are available.
	'''
	pass


class IllegalCountError(ControlError):
	'''
	Exception for if a player tries to do something with an illegal count (< 1) items.
	'''
	pass
