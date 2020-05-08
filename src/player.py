# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    def travel(self, direction):  
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(f"Current Room: {self.current_room.name}")
            print(f"{self.current_room.description}")
            if len(self.current_room.items) > 1:
                print("This room contains:")
                for i in self.current_room.items[1:]:
                    print(f"{i.name}, {i.description}")
        else:
            print("There is nothing in that direction")