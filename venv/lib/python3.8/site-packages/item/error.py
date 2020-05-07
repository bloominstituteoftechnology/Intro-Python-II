class ItemError(Exception):
    pass


class ItemRuntimeError(ItemError):
    pass


class ChoiceFieldError(ItemError):
    pass


class DataNotFound(ItemError):
    pass
