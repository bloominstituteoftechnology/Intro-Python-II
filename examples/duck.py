class Duck:
    def __init__(self, name, bill_description, tail_length, collar):
        self.name = name
        self.bill = Bill(bill_description)
        self.tail = Tail(tail_length)
        self.collar = collar

    def about(self):
        print(f"This duck has a {self.bill.description} bill, a {self.tail.length} tail, and a {self.collar.color} collar.")

class Bill:
    def __init__(self, description):
        self.description = description

class Tail:
    def __init__(self, length):
        self.length = length

class Collar:
    def __init__(self, color):
        self.color = color

new_collar = Collar('Blue')
duck = Duck('Quackers', 'wide orange', 'long', new_collar)
duck.about()
       