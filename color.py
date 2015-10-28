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

stdscr = curses.initscr()
curses.start_color()
signal.signal(signal.SIGINT, signal_handler)
capture = cv.CaptureFromCAM(0)
palette = [' ', '.', '.', '/', 'c', '(', '@', '#', '8']
pair = 1
depth = 6
splitby = (depth - 1) / 1000.0
(rows, columns) = os.popen('stty size', 'r').read().split()
rows = int(rows)
columns = int(columns)

for R in xrange(depth):
    for G in xrange(depth):
        for B in xrange(depth):
            curses.init_color(pair, int(R / splitby), int(G / splitby), int(B / splitby))
            curses.init_pair(pair, pair, 0)
            pair = pair + 1

while True:
    img = cv.QueryFrame(capture)
    size = cv.GetSize(img)
    height = size[0] * columns / size[1]

    thumbnail = cv.CreateImage(
            (columns, rows),
            img.depth,
            img.nChannels
    )

    cv.Resize(img, thumbnail)
    img = thumbnail

    for x in xrange(img.height):
        for y in xrange(img.width):
            b, g, r  = img[x, y]
            value = b * 0.2989 + g * 0.5866 + 0.1145 * r
            index = int(math.floor(value / (256.0 / (len(palette)))))

            try:
                stdscr.move(x, y)
                r = int( r / 256.0 * 6)
                g = int( g / 256.0 * 6)
                b = int( b / 256.0 * 6)
                pair = r * depth * depth + g * depth + b + 1

                stdscr.attrset(curses.color_pair(pair))
                stdscr.addch(palette[index])
            except:
                pass

    stdscr.refresh()
