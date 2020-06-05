# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        output_str = "{pname}. {proom}"
        return output_str.format(pname = self.name, proom = self.current_room)

    def get_items(self):
        output_str = "You currently have the following items: \n"
        for each in self.items:
            output_str += each.name + "\n"
        return output_str

    def take_item(self, item):
        print("input is:" + item)

        if item in self.current_room.get_items():
            self.items.append(self.current_room.get_item(item))
            self.current_room.remove_item(item)
            print("You picked up: " + item)
            return self.items
        else:
            print("Whoops, that doesn't seem to be in this room.")

    def drop_item(self, item):
        for each in self.items:
            if each.name == item:
                self.items.pop(self.items.index(each))
                self.current_room.add_item(each)
                print(item + " has now been dropped.")
