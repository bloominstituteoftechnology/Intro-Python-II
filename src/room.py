# Implement a class to hold room information. This should have name and
# description attributes.
"""Will need the following:
name
text
items
is_hungry
directions (n_to, s_to, e_to, w_to, s_to) """


class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        # self.items = items
        # self.n_to = None
        # self.s_to = None
        # self.e_to = None
        # self.w_to = None

        def __str__(self):
            return f"{self.name}, {self.desc}"

        # def display_items(self):
        #     if (self.items):
        #         for i in self.items:
        #             print(i.name)
        #     else:
        #         print('No items in the room')
