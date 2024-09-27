import sys
from time import sleep

def print_lyrics():
    lines = [
        ("Dear God the only thing I ask of you is", 0.10),
        ("To hold her when I'm not around", 0.07),
        ("When I'm much too far away", 0.07),
        ("We all need that person who can be true to you", 0.08),
        ("But I left her when I found her", 0.06),
        ("And now I wish I'd stayed", 0.08)
    ]

    delays = [2.5, 3, 3, 4, 3.5, 4]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
        
        sleep(delays[i])
        print('')

print_lyrics()
