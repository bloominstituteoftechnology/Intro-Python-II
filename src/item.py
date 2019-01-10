# Item class
class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"{self.name} \n {self.description}"

    # def on_get(self, item_list, item, i):
    #     item_list.append(item.pop(i))
