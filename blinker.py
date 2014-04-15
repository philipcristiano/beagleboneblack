import random
import time

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.ADC as ADC


def blink():
	GPIO.setup('P8_10', GPIO.OUT)
	GPIO.setup('P8_11', GPIO.OUT)

	while True:
		GPIO.output('P8_10', GPIO.LOW)
		GPIO.output('P8_11', GPIO.HIGH)
		time.sleep(1)
		GPIO.output('P8_10', GPIO.HIGH)
		GPIO.output('P8_11', GPIO.LOW)
		time.sleep(1)
	print GPIO.cleanup()

def scales():
	i = 0
	while True:
		for i in range(0, 100, 2):
			yield i
		for i in range(0, 100, 2):
			yield 100 - i
	

def flash():
	pins = ['P9_14', 'P9_21']
	for p in pins:
		PWM.start(p, 0)
		print 'start', p
	for i in scales():
		for p in pins:
			PWM.set_duty_cycle(p, i)
		time.sleep(.05)
		print get_temperature('AIN{}'.format(6))

def get_temperature(pin):
	value = ADC.read(pin)
	voltage = value * 1800
	celsius = (voltage - 500) / 10.0 
	fahrenheit = (celsius * 9.0 / 5.0) + 32.0
	return fahrenheit


if __name__ == '__main__':
	ADC.setup()
	flash()
