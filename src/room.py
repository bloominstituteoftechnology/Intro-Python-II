# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, n_to=None, w_to=None, e_to=None, s_to=None):
        self.n_to = n_to
        self.w_to = w_to
        self.e_to = e_to
        self.s_to = s_to
        self.name = name
        self.description = description

    def __str__(self):
        return f"Name of room: {self.name}\nDescription: {self.description}\nNorth: {self.n_to}\nWest: {self.w_to}\n" \
               f"East: {self.e_to}\nSouth: {self.s_to}"

if __name__ == "__main__":
    a = Room("asdf", "asjd;kl;") # __str__ works
    print(a)