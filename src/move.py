#empty 
def move_check():
    letter = input('Type n e s w to move, and press q to quit: ')
    if letter.lower() in ['n','e','s','w','q' ]:
        return(letter.lower())
    else: 
        print('')
        try_again = input('Try again: ')
        while try_again.lower() not in ['n', 'e', 's', 'w', 'q']:
            try_again = input('Try again: ')   
        return(try_again)    