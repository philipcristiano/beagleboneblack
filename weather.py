import httplib
import json
import time
import urllib2

from Adafruit_7Segment import SevenSegment

segment = SevenSegment(address=0x70)

def main():
    while True:
        temp = get_temp()
        display_temp(temp)
        time.sleep(180)

def display_temp(temp):
    #segment.writeDigit(0, int(temp / 100))
    segment.writeDigit(1, int(temp / 10))
    segment.writeDigit(3, int(temp % 10), dot=True)
    segment.writeDigit(4, int((temp * 10) % 10))
    segment.setColon(False)

def get_temp():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=new+york,ny,us'
    response = urllib2.urlopen(url).read()
    data = json.loads(response)
    tempK = data['main']['temp']
    tempF = (9.0/5.0) * (tempK - 273) + 32
    return tempF

if __name__ == '__main__':
    main()
