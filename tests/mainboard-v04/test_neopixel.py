# standard libraries
import time

# 3rd-party libraries
import unittest

# pycubed libraries
from pycubed import cubesat


class TestNeoPixel(unittest.TestCase):

    """
    NeoPixel unit tests; runs red, green, and blue lights at low brightness three
    times Note: Neopixel can go from (R,G,B) values from 0 to 255.
    """

    def test_rgb(self):
        print("\n")
        for i in range(3):
            print("Red")
            cubesat.RGB = (50, 0, 0)
            time.sleep(1)
            print("Green")
            cubesat.RGB = (0, 50, 0)
            time.sleep(1)
            print("Blue")
            cubesat.RGB = (0, 0, 50)
            time.sleep(1)
            self.assertEqual(cubesat.RGB[0], 0)
            self.assertEqual(cubesat.RGB[1], 0)
            self.assertEqual(cubesat.RGB[2], 50)
        print("\n---------------------")