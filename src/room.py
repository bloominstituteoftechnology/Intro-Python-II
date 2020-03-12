
class Room:
    def __init__(
            self, name='Nondescript',
            description='A very bland room, smells of ozone.',
            contents={}):
        self.name = name
        self.description = description
        self.contents = contents

    def __str__(self):
        return str(vars(self))
