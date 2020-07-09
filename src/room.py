# python room.py

# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None 

    def __repr__(self):
        return f"Name: {self.name}, Description: {self.description}"


if __name__ == "__main__":
    room = Room("kitchen", "Place to cook meals")
    print(room)