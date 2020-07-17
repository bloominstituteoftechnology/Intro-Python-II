import re

vowels = re.compile('a|e|i|o|u', re.IGNORECASE)


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.used = False

    def a_or_an(self):
        if vowels.match(self.name[0]):
            return 'an'
        else:
            return 'a'

    def __str__(self):
        return f'There is {self.a_or_an()} {self.name} here. {self.description}'
