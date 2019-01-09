# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, light, is_inside):
        self.name = name
        self.description = description
        self.light = light
        self.is_inside = is_inside

    def __repr__(self):
        return f"<You Are In {self.name}"