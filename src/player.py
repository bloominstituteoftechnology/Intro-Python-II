# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location):
        self.location = location
    def move(self, direction):
        directions = ['w', 'e', 'n', 's']
        if direction not in directions:
            new_direction = input("Please enter a valid direction. (n, s, w, e)")
            self.move(new_direction)
        else:
            try:
                diff_location = self.location[f"{direction}_to"]
                self.location = diff_location
            except:
                new_direction = input("You can't move in that direction! Try again. (n, s, w, e)")
                self.move(new_direction)
    def loot(self):
        item = self.location.get_item()
        if item:
            print(f"Yes! You got {item}.")
        else:
            print('There are no items in this room.')
