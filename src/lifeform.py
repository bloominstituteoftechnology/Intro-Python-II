class Lifeform:
    def __init__(self, name):
        self.name = name
        self.age = 0

    def sound(self):
        print('generic lifeform noise')

class Animal(Lifeform):
    pass

class Plant(Lifeform):
    def __init__(self, name, is_tree):
        super().__init__(name)
        self.is_tree = is_tree

class Cat(Animal):
    def sound(self):
        print('meow')

p = Plant('tom', False)
print(p.name)