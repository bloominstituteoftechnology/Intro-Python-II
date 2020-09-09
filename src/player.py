# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"Name: {self.name}\nCurrent room: {self.current_room}"


if __name__ == "__main__":
    a = Player("Bob", "Bob's Room") # __repr__ works
    print(a)
