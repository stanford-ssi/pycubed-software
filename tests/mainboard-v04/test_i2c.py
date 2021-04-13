import busio
import board
import time

import unittest
import adafruit_tcs34725


class TestI2C(unittest.TestCase):

    """
    Test a simple locking of a device two possible I2C pins. Here we tested an
    adafruit TCS34725 RGB sensor with the red green and blue LEDS.
    """

    def test_lock(self):
        print("") # XXX newline
        # busio.I2C(scl, sda) respectively
        i2c = busio.I2C(board.SCK, board.MOSI)
        i2c.try_lock()
        scan = i2c.scan()
        print("I2C scan:")
        print(scan)
        print("Locked Successfully!")
        i2c.unlock()
        print("Unlocked Successfully!")
        print("----------")
        i2c.deinit()

    def test_rgb_sensor(self):
        print("") # XXX newline
        # busio.I2C(scl, sda) respectively
        i2c = busio.I2C(board.SCK, board.MOSI)
        sensor = adafruit_tcs34725.TCS34725(i2c)
        # read the color temperature and lux of the sensor too
        for i in range(3):
            temp = sensor.color_temperature
            lux = sensor.lux
            print("Temperature: {0}K Lux: {1}".format(temp, lux))
            time.sleep(1.0)

        print("----------")
        i2c.deinit()