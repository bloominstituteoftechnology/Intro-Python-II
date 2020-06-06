# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = []

    def __str__(self):
        test_output = self.name + "\n"
        test_output += self.description + "\n"
        return test_output


    def add_items(self, items):
        itemize = map(lambda x: Item(x['name'], x['description']), items)
        self.items.extend(itemize)

    def add_off_drop_item(self, item):
        self.items.append(item)

    def delete_item(self, item):
        self.items.remove(item)

    def ask_for_items(self):
        items = []
        final_items = []
        the_input = input("What items would you like to add? For multiple items, separate with a comma")
        new_items = the_input.split(",")
        items.extend(new_items)
        for i in items:
            add_description = input(f'Description for {i} ? ')
            final_items.append({'name': i, 'description': add_description})

        self.add_items(final_items)



