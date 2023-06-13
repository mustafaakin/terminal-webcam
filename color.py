"""
This script captures images from a webcam using cv2 and
displays them as colored ASCII art in the terminal.
"""

import os
import sys
import math
import curses
import signal
import cv2


def signal_handler(sig, _):
    """
    Handle Ctrl+C and clean up curses before exiting.

    Args:
        sig (int): The signal number.
        _ (Frame): The interrupted stack frame.
    """
    print('You pressed Ctrl + C!')
    curses.endwin()
    sys.exit(0)


def initialize_colors(depth):
    """
    Initialize color pairs in curses for the given color depth.

    Args:
        depth (int): The color depth (number of levels per RGB component).
    """
    splitby = (depth - 1) / 1000.0
    pair = 1

    for red in range(depth):
        for green in range(depth):
            for blue in range(depth):
                curses.init_color(
                    pair,
                    int(red / splitby),
                    int(green / splitby),
                    int(blue / splitby)
                )
                curses.init_pair(pair, pair, 0)
                pair += 1


def main():
    """
    The main function captures images from the webcam and displays them in the terminal.
    """
    stdscr = curses.initscr()
    curses.start_color()
    signal.signal(signal.SIGINT, signal_handler)
    capture = cv2.VideoCapture(0)
    palette = [' ', '.', '.', '/', 'c', '(', '@', '#', '8']
    depth = 6
    rows, columns = map(int, os.popen('stty size', 'r').read().split())

    initialize_colors(depth)

    while True:
        img = capture.read()[1]
        thumbnail = cv2.resize(img, (columns, rows))

        for x in range(thumbnail.shape[0]):
            for y in range(thumbnail.shape[1]):
                blue, green, red = thumbnail[x, y]
                value = blue * 0.1145 + green * 0.5866 + red * 0.3989
                index = int(math.floor(value / (256.0 / len(palette)))) % len(palette)

                try:
                    stdscr.move(x, y)
                    red = int(red / 256.0 * 6)
                    green = int(green / 256.0 * 6)
                    blue = int(blue / 256.0 * 6)
                    pair = red * depth * depth + green * depth + blue + 1

                    stdscr.attrset(curses.color_pair(pair))
                    stdscr.addch(palette[index])
                except curses.error:
                    pass

        stdscr.refresh()


if __name__ == "__main__":
    main()
