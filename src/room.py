import time

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def invalid_room(self):
        print('There is nothing to be gained by going in this direction...')
        time.sleep(1.5)
