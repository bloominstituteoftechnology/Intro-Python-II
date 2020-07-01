class Room():
    def __init__(self, name, description, n_to=None, e_to=None, s_to=None, w_to=None, items=[]):
        self.name = name
        self.description = description
        self.connections = {
            'n': n_to,
            's': s_to,
            'e': e_to,
            'w': w_to
        }

        self.items = items
