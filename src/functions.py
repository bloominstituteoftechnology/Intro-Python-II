import time, sys, random

# function to print string like typing
def print_slow(s):
    for letter in s:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)