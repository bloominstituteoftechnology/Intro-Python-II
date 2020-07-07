# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def add_item(self, i):
        self.items.append(i)

    def remove_item(self, item):
        if len(self.items) > 1:
            for i in range(0, len(self.items)):
                if self.items[i].item_name == item:
                    self.items.remove(self.items[i])
                    break
        else:
            for i in range(0, len(self.items)):
                if self.items[i].item_name == item:
                    self.items.remove(self.items[i])

    def __repr__(self):
        def all_items():
            new_list = []
            if len(self.items) > 0:
                for i in range(len(self.items)):
                    new_list.append(self.items[i].description)
                return ', and also '.join(new_list)
            else:
                return 'nothing of interest'
        return f"you find yourself at the {self.name}, {self.description}, in it lies {all_items()}"
