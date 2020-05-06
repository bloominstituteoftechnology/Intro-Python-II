# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def get_next_room_for_direction(self, direction):
        if hasattr(self, f'{direction}_to'):
            return getattr(self, f'{direction}_to')
        return None

