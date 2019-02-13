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

        def __str__(self):
            return f"{self.name}, {self.desc}"
