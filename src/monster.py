class Monster:
    def __init__(self, name, description, attack, hit_points):
        self.name = name
        self.description = description
        self.attack = attack
        self.hit_points = hit_points
        self.is_alive = True

    def on_attack(self, attack):
        if self.is_alive:
            self.hit_points -= attack
            if self.hit_points <= 0:
                self.is_alive = False
                print(f"{self.name} has been defeated!")
            else:
                print(f"{self.name} was damaged! It's health is now at {self.hit_points}.")
        else:
            print(f"{self.name} is already dead!")
