"""
This script captures images from a webcam using cv2 and
displays them as monochrome ASCII art in the terminal.
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


def main():
    """
    The main function captures images from the webcam and displays them in the terminal.
    """
    stdscr = curses.initscr()
    signal.signal(signal.SIGINT, signal_handler)
    capture = cv2.VideoCapture(0)
    palette = [' ', '.', '.', '/', 'c', '(', '@', '#', '8']
    rows, columns = map(int, os.popen('stty size', 'r').read().split())

    while True:
        img = capture.read()[1]
        thumbnail = cv2.resize(img, (columns, rows))

        for x in range(thumbnail.shape[0]):
            for y in range(thumbnail.shape[1]):
                blue, green, red = thumbnail[x, y]
                value = blue * 0.1145 + green * 0.5866 + red * 0.2989
                index = int(math.floor(value / (256.0 / len(palette)))) % len(palette)

                try:
                    stdscr.move(x, y)
                    stdscr.addch(palette[index])
                except curses.error:
                    pass

        stdscr.refresh()


if __name__ == "__main__":
    main()
