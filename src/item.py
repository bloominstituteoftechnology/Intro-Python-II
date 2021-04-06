class Item:
    def __init__(self, id, name, description, room_description, vitamins):
        self.id = id
        self.name = name
        self.description = description
        self.room_description = room_description
        self.vitamins = vitamins

    def __str__(self):
        return f"{self.name} is worth {self.vitamins} vitamins"
    def to_inventory(self):
        print(f"{self.name} was placed into your inventory")
    def to_floor(self):
        print(f"{self.name} was dropped on the floor.")

class Container(Item):
    def __init__(self, id, name, description, room_description, inventory):
        super().__init__(id, name, description, room_description, 0)
        self.inventory = inventory

    def letter_to_int(self, letter):
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        if letter in alphabet:
            return alphabet.index(letter)

    def int_to_letter(self, index):
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        if len(alphabet) >= index + 1:
            return alphabet[index]

    def list_inventory(self, player):
        #turning a letter into bytes
        letter_i = self.letter_to_int('a')

        for item in self.inventory:
            #decode to string and make uppercase
            letter_s = self.int_to_letter(letter_i)
            upper_str = letter_s.upper()
            #output
            print(f"{upper_str}: {item.name}")
            #increment to the next byte (this will convert to the next character)
            letter_i += 1
        if len(self.inventory) > 0:
            treasure = input("select a letter to take an item: ").lower()
            index = self.letter_to_int(treasure)

            if isinstance(index, int) and len(self.inventory) >= index + 1:
                player.take(self.inventory[index])
                self.inventory.pop(index)
            else:
                print(f"{treasure} cannot be removed from this chest")
        else:
            print(f"{self.name} is empty!")

        
class Trinket(Item):
    def __init__(self, id, name, description, room_description, sparkle):
        super().__init__(id, name, description, room_description)
        self.sparkle = sparkle

class VitaminPack(Item):
    def __init__(self, id, room_description):
        super().__init__(id, "vitamins", "", room_description)
        self.description = f"vitamins - to keep you going in circles longer"

