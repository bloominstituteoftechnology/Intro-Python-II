def print_color(color, str):
    if color == 'red':
        print(f'\033[91m {str}\033[00m')
    elif color == 'green':
        print(f'\033[92m {str}\033[00m')
    elif color == 'yellow':
        print(f'\033[93m {str}\033[00m')
    elif color == 'light_purple':
        print(f'\033[94m {str}\033[00m')
    elif color == 'purple':
        print(f'\033[95m {str}\033[00m')
    elif color == 'cyan':
        print(f'\033[96m {str}\033[00m')
    elif color == 'light_grey':
        print(f'\033[97m {str}\033[00m')
    elif color == 'black':
        print(f'\033[98m {str}\033[00m')
