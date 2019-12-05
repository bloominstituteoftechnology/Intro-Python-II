# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_location):
        self.name = name
        self.current_location = current_location

    def __str__(self):
        return f"My Name is '{self.name}', I am currently located  {self.current_location}"
