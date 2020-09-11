# Write a class to hold player information, e.g. what room they are in
# currently.

def lookup_item(string, items):
    #returns item with matching name
    for item in items:
        if item.name == string:
            return item
        else:
            return None
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def move(self, direction):
        new_room = getattr(self.current_room, f"{direction}_to")
        if (new_room) is not None:
            self.current_room = new_room
        else:
            print("Sorry you can't move in that direction")

    def show_items(self):
        if self.items.__len__() == 0:
            return "you have no items"
        else:
            return ", ".join(list(map(lambda it: it.name, self.items)))

    def do(self, command):
        action, item_name = command.split(" ")
        if action == 'get':
            item = lookup_item(item_name, self.current_room.items)
            if item is not None:
                self.current_room.items.remove(item)
                self.items.append(item)
                item.get()
            else:
                print(f'{item.name} is not in this room')
        elif action == 'drop':
            item = lookup_item(item_name, self.items)
            if item is not None:
                self.items.remove(item)
                self.current_room.items.append(item)
                item.drop()
            else:
                print(f'You do not have {item.name}')
        else:
            print('that is not a valid command')
        


    def __str__(self):
        return '{self.name} {self.room}'.format(self=self)

    

