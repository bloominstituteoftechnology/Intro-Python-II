# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, current_room, item=[]):
        self.current_room = current_room
        self.item = item

    def __str__(self):
        x = f"Your Current Location: {self.current_room.name}\n Current Inventory: "
        if len(self.item)<1:
            x += f"Nothing"
        else:
            for i in self.item:
                x += f"\n {i}"
        return x

    def take(self, item="na"):
        self.item.append(item)
        return f"You Chose {item}"
