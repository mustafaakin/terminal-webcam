import cv
import os
import sys
import math
import curses
import signal

def signal_handler(signal, frame):
    print 'You pressed Ctrl + C!'
    curses.endwin()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

stdscr = curses.initscr()
palette = [' ', '.', '.', '/', 'c', '(', '@', '#', '8']
capture = cv.CaptureFromCAM(0)

# Get the width and height from the terminal (console)
(rows, columns) = os.popen('stty size', 'r').read().split()
rows = int(rows)
columns = int(columns)

while True:
    # Capture the image
    img = cv.QueryFrame(capture)

    thumbnail = cv.CreateImage(
            (columns, rows),
            img.depth,
            img.nChannels
    )

    cv.Resize(img, thumbnail)

    img = thumbnail

    # Print the output
    for x in xrange(img.height):
        for y in xrange(img.width):
            b, g, r = img[x, y]
            value = b * 0.1145 + g * 0.5866 + r * 0.2989
            index = int(math.floor(value / (256.0 / (len(palette)))))

            try:
                stdscr.move(x, y)
                stdscr.addch(palette[index])
            except:
                pass

    stdscr.refresh()
