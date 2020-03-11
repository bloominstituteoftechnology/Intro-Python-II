from abc import ABC, abstractmethod


class Human:
    def __init__(self, name, pets=None):
        self.name = name
        self.pets = pets
        if self.pets is None:
            self.pets = []
    def add_pet(self, new_pet):
        self.pets.append(new_pet)
        new_pet.owners.append(self)

class Animal(ABC):
    count = 0
    def __init__(self, name, color, height, diet, species, owners = None):
        self.name = name
        self.color = color
        self.height = height
        self.diet = diet
        self.species = species
        self.owners = owners
        Animal.count += 1
    @abstractmethod
    def speak(self):
        pass
    @abstractmethod
    def eat(self, food):
        pass
    def sleep(self):
        print("zzzz")
    @abstractmethod
    def move(self):
        pass



class Dog(Animal):
    def __init__(self, name, color, height, owners=None):
        super().__init__(name, color, height, "CARNIVORE", "DOG", owners)
        self.owners = owners
    def speak(self):
        print("Woof!")
    def eat(self, food):
        if food == "MEAT":
            print("yum!")
        else:
            print("yuck")
    def move(self):
        print(f"{self.name} walks.")


d = Dog("Fido", 'BROWN', 12)