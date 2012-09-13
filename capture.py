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

palette = [' ', '.', '.', '/', 'c', '(', '@', '#', '8']

while True:
	# Capture the image
	img = cv.QueryFrame(capture)
	
	# Resize the Image
	size = cv.GetSize(img)
	height = size[0] * width / size[1]

	thumbnail = cv.CreateImage( ( height, width), img.depth, img.nChannels)
	cv.Resize(img, thumbnail)
	img = thumbnail

	# Clear screen

	# Print the output
	for x in xrange(img.height):
		for y in xrange(img.width):
			b, g, r = img[x, y]
			value = 0.1145 * b + g * 0.5866 + r * 0.2989
			index = int(math.floor( value / (256.0 / (len(palette)))))
			try:
				stdscr.move(x,y)
				stdscr.addch(palette[index])
			except:
				pass
	stdscr.refresh()