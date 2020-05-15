# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def move_to(self, direction):
        short_direction = direction[0]

        if getattr(self.current_room, f"{short_direction}_to") is not None:
            self.current_room = getattr(
                self.current_room, f"{short_direction}_to")

            print(f"Player is in room {self.current_room}\n")
            if self.current_room.items is not None:
                print(f"In the room, there is a {self.current_room.items}")
                print("Would you like to pick up? (yes, no)")
                while True:
                    selection = input()
                    if selection == "yes":
                        print("adding item to inventory")
                        self.pickup_item(self.current_room.items)
                        print(
                            f"{self.current_room.items.name} is now in your inventory.")
                        break
                    elif selection == "no":
                        print("Leaving item in place")
                        break
                    else:
                        print("That is not a valid selection")
        else:
            print("There is no room in that Direction!")

    def pickup_item(self, item):
        self.items.append(item)

    def destroy_item(self, item):
        for i in self.items:
            if i.name == item.name:
                del items[i]
                print(f"{item} was removed from your inventory and destroyed.")
