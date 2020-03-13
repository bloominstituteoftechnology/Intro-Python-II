class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def on_take(self):
        return f'You have picked up {self.name}'
    
    def on_drop(self):
        return f'You have dropped {self.name}'
        
class Food(Item):
    def __init__(self, name, description, calories):
        super().__init__(name, description)
        self.calories = calories
