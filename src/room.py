from item import LightSource


class Room():
    def __init__(self,
                 name,
                 description,
                 items=[]):
        self.name = name
        self.description = description
        self.list_items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.is_light = True
        return

    def __str__(self):
        return (self.description)

    def add_item(self, item):
        self.list_items.append(item)
        return

    def remove_item(self, item_name):
        for i in self.list_items:
            if i.name == item_name:
                self.list_items.remove(i)
                return
        return

    def inventory(self):
        if len(self.list_items) == 0:
            print('there is nothing around....')
        else:
            print("looking around, you see.... ")
            for i in self.list_items:
                print(i)
        return

    def in_room(self, item_name):
        ex_ists = False
        for i in self.list_items:
            if i.name == item_name:
                ex_ists = True
        return ex_ists

    def get_item(self, item_name):
        if self.in_room(item_name):
            for i in self.list_items:
                if i.name == item_name:
                    return i
        return None

    def visible(self):
        return self.is_light

    def has_light(self):
        ex_ists = False
        for i in self.list_items:
            if isinstance(i, LightSource):
                ex_ists = True
        return ex_ists
