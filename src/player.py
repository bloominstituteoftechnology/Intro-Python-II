# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items=[]):
        super().__init__
        self.name = name
        self._current_room = current_room
        self.items = items

    def take_item(self, item_to_take):
        found_item, item_index, item = self._current_room.has_item(item_to_take)
        if found_item:
            self.items.append(item)
            item.on_take()
            self._current_room.remove_item(item_index)
        else:
            print("That item does not exist in this room")  

    def drop_item(self, item_to_drop):
        has_item = False
        for index, item in enumerate(self.items):
            if item.name == item_to_drop:
                self.items.pop(index)
                self._current_room.add_item(item)  
                has_item = True 

        if not has_item:
            print("You do not have that item")

    def show_inventory(self):
        new_line = '\n'
        print(f""""
        Items:
        {f'{new_line}'.join(str(item) for item in self.items)}
        """)  

    def _set_current_room(self, current_room):
        self._current_room = current_room

    def _get_current_room(self):
        return self._current_room              

    def __str__(self):
        return f"""
        Name: {self.name}
        """

    current_room = property(_get_current_room, _set_current_room)


