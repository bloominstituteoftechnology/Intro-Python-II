import sys
import time
from textwrap import wrap

def crawlText(text, delay=0.01):
    text = wrap(text, 50)
    text = '\n\r'.join(text)
    for ln in text:
        sys.stdout.write(ln)
        sys.stdout.flush()
        time.sleep(delay)
    print('\n')