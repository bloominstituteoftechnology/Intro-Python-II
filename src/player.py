# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:

    def __init__(self, name, room, items):
        self.name = name
        self.room = room
        self.items = items

    def __repr__(self):

        output = ""
        output += "Name: " + self.name + "\n"
        output += "Room: " + self.room + "\n"
        if len(self.items) > 0:
            for i in range(0, len(self.items)):
                output += str(int + 1) + ". " + self.items[i] + "\n"
        return output
