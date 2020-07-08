# class for room attributes
from collections import defaultdict

class Room:
    def __init__(self, name, description, dark_description="It's pitch black! You can't see a thing!", lit=False):
        self.name = name
        self.description = description
        self.dark_description = dark_description
        self.contents = defaultdict(int)
        self.lit = lit
        self.exits = {}

    def __str__(self, player_light=False):
        light_in_room = False
        for item in self.contents.keys():
            light_in_room = light_in_room or item.light
        if not (self.lit or light_in_room or player_light):
            room_string = f"Darkness...\n\n{self.dark_description} \n\nBest turn back for now."
        else:
            room_string = f"{self.name}\n\n{self.description}"
            if len(self.contents) != 0:
                room_string += ("\n\n" + "\n".join([key.description for key in self.contents.keys()]))
            room_string += ("\n\nVisible exits: " + " ".join(list(self.exits.keys())))
        return room_string

    def illuminated(self):
        light_in_room = False
        for item in self.contents.keys():
            light_in_room = light_in_room or item.light
        return self.lit or light_in_room  

