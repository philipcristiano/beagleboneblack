import random
import time
import os

import librato
from luxmeter import Luxmeter

lib_api = librato.connect(os.getenv('LIBRATO_USER'), os.getenv('LIBRATO_TOKEN'))

def main():
	last_time = 0
	lm = Luxmeter()
	while True:
		lux = lm.getLux(1)
		print 'Lux', lux
		if time.time() > last_time + 60:
			lib_api.submit('home_lux', lux)
			last_time = time.time()
			print 'Saved to Librato'
		time.sleep(1)

if __name__ == '__main__':
	main()
