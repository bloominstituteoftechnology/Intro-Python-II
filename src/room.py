# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, describtion, emoji):
        self.name = name
        self.describtion = describtion
        self.emoji = emoji
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"{self.name} - {self.describtion}"
