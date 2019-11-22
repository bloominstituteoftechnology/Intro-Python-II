# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        output = f'{self.name}: {self.description}'
        return output


# black_room = Room('black', 'i am a dark room fear me!')
# print(black_room)
