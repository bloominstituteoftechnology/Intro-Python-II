# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, storage):
        self.name = name
        self.current_room = current_room
        self.storage = storage

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Current room: {self.current_room}\n" \
               f"Stuff on player: {self.storage}"


if __name__ == "__main__":
    a = Player("Bob", "Bob's Room")  # __repr__ works
    print(a)
