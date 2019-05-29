# classes


class Animal:
    def __init__(self, name, breed, gender):
        self.name = name
        self.breed = breed
        self.gender = gender

    def __str__(self):
        return f"Name: {self.name}\nGender: {self.gender}\nBreed: {self.breed}\n"


a = Animal("Groot", "Tree", "Who knows?!")


class Dog(Animal):
    def __init__(self, name, breed, gender, eyes, fluff, good_boye=True):
        super().__init__(name, breed, gender)
        self.eyes = eyes
        self.fluff = fluff
        self.good_boye = good_boye

    def give_belly_rub(self):
        if self.good_boye:
            print(
                f"the good boye {self.name} rolls on his back for the belly rub")
        else:
            self.bark()

    def bark(self):
        print("Woof woof")

    def __str__(self):
        return f"{super().__str__()}Eyes: {self.eyes}\nIs fluffy: {self.fluff}\nIs good boye: {self.good_boye}\n"


b = Dog("Fido", "Golden", "Male", 1, True, False)

print(a)
print(b)
b.give_belly_rub()
b.bark()
