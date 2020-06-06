class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}: ${str(self.price)}'

class Clothing(Product):
    def __init__(self, name, price, size, color):
        super().__init__(name, price)
        self.size = size
        self.color= color

class Equipment(Product):
    def __init__(self, name, price, material, weight):
        super().__init__(name, price)
        self.size = material
        self.color = weight


shoes = Clothing("running shoes", 100, 11, "black")
bat = Equipment("baseball bat", 100, 'wood', 2)
print(bat)

print(shoes)