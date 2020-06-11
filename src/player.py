# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, locus):
        self.name = name
        self.locus = locus
    
    def __str__(self):
        return f'I am in {self.locus}'