from room import Room
from item import Item, Key

# Declare all the rooms
room = {
    'entrance': Room("Entrance", 'To the North is a long hallway with multiple doors.\nYou see a door to the east and west of you as well\n'),

    'closet': Room("Closet", 'You enter the closet and notice an old dusty box, the only way out is the door to the east\n'),

    'x': Room("Model X", 'You enter a garage like room and see a Tesla Model X\nThere is a door to the north and to the east\n'),

    'kitchen': Room("Kitchen", 'The smell of freshly cooked bacon fills the air as you enter the kitchen\nYou have a door in all four directions\n'),

    'patio': Room("Patio", 'The aroma of the pine trees please you as you step onto the patio\nthe only way back inside is to the east\n'),

    'hallway': Room('Hallway 1', 'You enter the first part of the hallway and notice the wierd art\nThe hallway continues north and you have a door to the east and west\n'),

    'hallway2': Room('Hallway 2', '''You enter the second half of the hallway and realize how slick the marble floor is\nThere is a red, green, and blue door in front of you\nand a door to the east and west and the hallway with the art to the south\n'''),

    'diningroom': Room('Dining Room', 'You enter the dining room and see a table set for four people and a dish for a dog.\nYou have doors in all four directions\n'),

    's': Room('Model S', 'You enter a room full of lemon scent and see a bright red Tesla Model S.\nThe only way out is to the east\n'),

    'roadster': Room('Roadster', 'You enter the room and see what appears to be a car that can go 0-60mph in 1.9 seconds\nyou quickly realize it\'s the Tesla Roadster(with the rocket thruster option of course)\nThere is a door to the east and the south\n'),

    'bedroom': Room('Bedroom', 'You enter the bedrrom and see a massive bed, nearly double the size of a California Queen.\nThere is only a door to the east'),

    '3': Room('Model 3', 'You enter a garage like room and see a Tesla model 3\nThere are doors to the north, east, and west\n'),

    'bathroom': Room('Bathroom', 'You enter a bathroom and notice it\'s still steamy in here, someone must have showered recently\nThere is a door to the east and the north\n'),

    'masterbath': Room('Master Bathroom', 'You enter a massive bathroom and noticed the massive bathtub, it might as well be a small pool\nThere is a door to the south and the east\n'),

    'artroom': Room('Art Room', 'So much strange art, whoever owns this must have a wierd taste in art\nThere is a door in all four directions\n'),

    'y': Room('Model Y', 'You enter a garage like room and see a sleek Tesla Model Y\nThere is only a door to the south\n'),

    'cybertruck': Room('CyberTruck', 'You found the Cybertruck!\nIs that Elon Musk inside?\nHe offers you a job at Tesla!\n')
}

# Declare the items
items = {
    'redkey': Key('Red Key', 'Normal house key', 'Red'),

    'greenkey': Key('Green Key', 'Old fashioned looking key', 'Green'),

    'bluekey': Key('Blue Key', 'Looks like a credit card, but it does say key on it.', 'Blue'),

    'spatula': Item('Spatula', 'This spatula would be a great addition to your own kitchen'),

    'owl': Item('Owl', 'An art piece that looks like an owl, it has a note that says \"It\'s artificial\".'),

    'pillow': Item('Pillow', 'You really needed a new pillow, and this one looks like it\'s in great condition'),

    'travelshampoo': Item('Travel Shampoo', 'You take them from Hotels, so what\'s the difference?'),

    'lemon': Item('Lemon', 'The smell of lemon is so good, you just had to have it.'),

    'cactus': Item('Cactus', 'You could alsways use another mini cactus to have at home.')
}

# Link rooms together
room['entrance'].n_to = room['hallway']
room['entrance'].e_to = room['x']
room['entrance'].w_to = room['closet']

room['x'].n_to = room['kitchen']
room['x'].e_to = room['entrance']

room['closet'].e_to = room['entrance']

room['kitchen'].n_to = room['diningroom']
room['kitchen'].e_to = room['hallway']
room['kitchen'].s_to = room['x']
room['kitchen'].w_to = room['patio']

room['hallway'].n_to = room['hallway2']
room['hallway'].e_to = room['3']
room['hallway'].s_to = room['entrance']
room['hallway'].w_to = room['kitchen']

room['patio'].e_to = room['kitchen']

room['3'].n_to = room['artroom']
room['3'].e_to = room['bathroom']
room['3'].w_to = room['hallway']

room['bathroom'].n_to = room['masterbath']
room['bathroom'].w_to = room['3']

room['masterbath'].s_to = room['bathroom']
room['masterbath'].w_to = room['artroom']

room['artroom'].n_to = room['y']
room['artroom'].e_to = room['masterbath']
room['artroom'].s_to = room['3']
room['artroom'].w_to = room['hallway2']

room['y'].s_to = room['artroom']

room['hallway2'].n_to = room['cybertruck']
room['hallway2'].e_to = room['artroom']
room['hallway2'].s_to = room['hallway']
room['hallway2'].w_to = room['diningroom']

room['diningroom'].n_to = room['roadster']
room['diningroom'].e_to = room['hallway2']
room['diningroom'].s_to = room['kitchen']
room['diningroom'].w_to = room['s']

room['s'].e_to = room['diningroom']

room['roadster'].s_to = room['diningroom']
room['roadster'].w_to = room['bedroom']

room['bedroom'].e_to = room['roadster']

# Add items and keys to rooms
room['kitchen'].items = [items['spatula'], items['lemon']]

room['artroom'].items = [items['owl']]

room['bathroom'].items = [items['travelshampoo']]

room['bedroom'].items = [items['pillow']]

room['patio'].items = [items['cactus']]

room['3'].items = [items['bluekey']]

room['y'].items = [items['greenkey']]

room['roadster'].items = [items['redkey']]



