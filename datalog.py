import random
import time
import os
import sys

from Adafruit_7Segment import SevenSegment
from luxmeter import Luxmeter
from mcp9808 import MCP9808
import librato

segment = SevenSegment(address=0x71)

lib_api = librato.connect(os.getenv('LIBRATO_USER'), os.getenv('LIBRATO_TOKEN'))

def main():
	last_time = 0
	lm = Luxmeter()
	mcp = MCP9808()
	while True:
		lux = lm.getLux(1)
		print 'Lux', lux
		temp_f = mcp.read_temp_f()
		display_temp(segment, temp_f)
		print 'Temp', temp_f
		if time.time() > last_time + 60:
			lib_api.submit('home_lux', lux)
			lib_api.submit('home_temp_f', temp_f)
			last_time = time.time()
			print 'Saved to Librato'
		sys.stdout.flush()
		time.sleep(1)

def display_temp(segment, temp):
    segment.writeDigit(1, int(temp / 10))
    segment.writeDigit(3, int(temp % 10), dot=True)
    segment.writeDigit(4, int((temp * 10) % 10))
    segment.setColon(False)

if __name__ == '__main__':
	main()
