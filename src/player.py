# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room, items):
        self.current_room = current_room
        self.items = items
    
    def move(self, direction):
        next_room = getattr(self.current_room, f'{direction}_to', None)

        if next_room is not None:
            self.current_room = next_room
        else:
            print("\n")
            print("You can't move that way")
    
    def add_item(self, item_name):
        for item in self.current_room.items:
            if item.name == item_name:
                self.current_room.items.remove(item)
                self.items.append(item)
                item.on_take(item.name)
                break
        else:
            print('That item is not here')

    def drop_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                item.on_drop(item.name)
                break        
        else:
            print("You can't drop something you don't have")
