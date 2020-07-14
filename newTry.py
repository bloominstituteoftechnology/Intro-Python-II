from theTry import getch

while True:
    n = getch()
    n = n.decode('ascii')
 
    print(f"This is the letter that has been pressed {n}\n")