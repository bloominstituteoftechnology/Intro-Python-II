# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # self.light = light
        # self.is_inside = is_inside
        # self.items = items
        # self.enemies = enemies
    def __repr__(self):
        return f"<Room: {self.name} | Description: {self.description}>"