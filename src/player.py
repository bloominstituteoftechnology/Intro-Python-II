# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, starting_room, storage=[]):
        self.name = name
        self.current_room = starting_room
        self.storage = storage
    
    def storageString(self):
        return ', '.join([item.name for item in self.storage])
    
    def removeItem(self, item_name_to_remove):
        """
        Removes item from Player storage. Returns removed item, or False if not found.
        """
        items_to_keep = []
        item_found = None

        for item in self.storage:
            if item.name == item_name_to_remove:
                item_found = item
            else:
                items_to_keep.append(item)
        self.storage = items_to_keep
        
        if item_found:
            return item_found
        else:
            return False