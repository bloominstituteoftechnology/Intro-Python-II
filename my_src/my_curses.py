import curses
 
# get the curses screen window
screen = curses.initscr()
 
# turn off input echoing
curses.noecho()
 
# respond to keys immediately (don't wait for enter)
curses.cbreak()
 
# map arrow keys to special values
screen.keypad(True)
 
try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_RIGHT:
            # print doesn't work with curses, use addstr instead
            screen.addstr(0, 0, "You've stepped East ")
        elif char == curses.KEY_LEFT:
            screen.addstr(0, 0, "You've stepped West ")       
        elif char == curses.KEY_UP:
            screen.addstr(0, 0, "You've stepped North ")       
        elif char == curses.KEY_DOWN:
            screen.addstr(0, 0, "You've stepped South ")
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
