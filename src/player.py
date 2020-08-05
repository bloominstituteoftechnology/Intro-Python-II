# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, location):
        self.location = location
    def __str__(self):
        return (f'Your location is {self.location}.')

    # def dict_from_class(cls):
    #     return dict((key, value) for (key, value) in cls.__dict__.items()
    #     if key not in _excluded_keys)
