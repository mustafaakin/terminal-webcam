import cv
import sys
import math
import curses
import signal

stdscr = curses.initscr()

def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    curses.endwin()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
width = int(sys.argv[1]) if len(sys.argv) > 1 else 50

# cv.NamedWindow("camera", 1)
capture = cv.CaptureFromCAM(0)

# Initialize colors and palette
palette = [' ', '.', '.', '/', 'c', '(', '@', '#', '8']
curses.start_color()
pair = 1
depth = 6
splitby = (depth - 1) / 1000.0

for R in xrange(depth):
    for G in xrange(depth):
        for B in xrange(depth):             
            curses.init_color(pair, int(R/splitby), int(G/splitby), int(B/splitby))
            curses.init_pair(pair, pair, 0)
            pair = pair + 1

while True:
    # Capture the image
    img = cv.QueryFrame(capture)

    # Resize the image
    size = cv.GetSize(img)
    height = size[0] * width / size[1]

    thumbnail = cv.CreateImage(
            (height, width),
            img.depth,
            img.nChannels
    )

    cv.Resize(img, thumbnail)
    img = thumbnail

    # Print the output
    for x in xrange(img.height):
        for y in xrange(img.width):
            b, g, r = img[x, y]
            value = 0.1145 * b + g * 0.5866 + r * 0.2989
            index = int(math.floor( value / (256.0 / (len(palette)))))

            try:
                stdscr.move(x,y)
                r = int( r / 256.0 * 6)
                g = int( g / 256.0 * 6)
                b = int( b / 256.0 * 6)

                pair = r * depth * depth + g * depth + b + 1
                stdscr.attrset(curses.color_pair(pair))
                stdscr.addch(palette[index])
            except:
                pass

    stdscr.refresh()