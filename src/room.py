# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def _init_(self, room_name = "", room_description = ""):
        self.room_name = room_name
        self.room_description = room_description

    def _str_(self):
        return "{} \nRoom Description: {}".format(self.room_name, self.room_description)