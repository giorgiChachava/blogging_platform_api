import sys
import time

def typeout(text, delay=0.02):
    if not sys.stdout.isatty():
        print(text)
        return

    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def typeout2(text, delay=0.004):
    if not sys.stdout.isatty():
        print(text)
        return

    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()
    
def typeout3(text, delay=0.0005):
    if not sys.stdout.isatty():
        print(text)
        return

    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()