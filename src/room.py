# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, text, items):
        self.name = name
        self.text = text
        self.items = items
        
        def add_item(self, item):
            self.items.append(item)

        def get_items_list(self):
            if (self.items):
                return [x.name for x in self.items]
            else:
                return []
        def print_items(self):
            print('Items: {self.items}')

# hello = Room()
# hello.add_item("Kili Kili Power")
# hello.get_items_list()

