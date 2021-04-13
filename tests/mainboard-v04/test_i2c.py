import unittest

import busio
import board

class TestI2C(unittest.TestCase):

    """
    Test a simple locking of a device two possible I2C pins. Here we tested an
    adafruit TCS34725 RGB sensor with the red green and blue LEDS.
    """
    def simple_test(self):
        # busio.I2C(scl, sda) respectively
        i2c = busio.I2C(board.SCK, board.MOSI)
        i2c.try_lock()
        i2c.scan()
        print("Locked Successfully!")
