
def descendants(cls: type) -> list:
	"""
	Return a list of all descendant classes of a class

	Arguments:
		cls (type): Class from which to identify descendants
	Returns:
		subclasses (list): List of all descendant classes
	"""

	subclasses = cls.__subclasses__()
	for subclass in subclasses:
		subclasses.extend(descendants(subclass))

	return(subclasses)
