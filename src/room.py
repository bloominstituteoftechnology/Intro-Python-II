# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, n, s, w, e):
        self.description = description
        self.name = name
        self.n = n
        self.s = s
        self.w = w
        self.e = e
