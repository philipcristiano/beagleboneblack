from Adafruit_I2C import Adafruit_I2C

class MCP9808(object):

    def __init__(self, address=0x18):
        self._i2c = Adafruit_I2C(address)
        self._address = address

        # Assert it's the right thing
        val = hex(self._i2c.reverseByteOrder(self._i2c.readU16(0x06)))
        assert val == 0x54, 'Not right manufacturer'
        val = hex(self._i2c.reverseByteOrder(self._i2c.readU16(0x07)))
        assert val == 0x4, 'Not right device ID'

    def read_temp_c(self):
        val = self._i2c.reverseByteOrder(self._i2c.readU16(0x05))
        temp = val & 0x0FFF
        sign = val & 0x1000
        temp /= 16.0
        if sign:
            temp *= -1
        return temp

    def read_temp_f(self):
        return self.read_temp_c() * 9.0/5.0 + 32

def read():
    sensor = MCP9808()
    print sensor.read_temp_c()

if __name__ == '__main__':
    read()
