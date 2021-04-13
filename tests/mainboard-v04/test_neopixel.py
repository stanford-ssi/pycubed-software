import unittest

class TestNeoPixel(unittest.TestCase):

    """
    NeoPixel unit tests; runs red, green, and blue lights at low brightness three
    times Note: Neopixel can go from (R,G,B) values from 0 to 255.
    """
    def Test_NeoPixel(self):
        for i in range(3):
            print("PyCubed Running!")
            cubesat.RGB = (50, 0, 0)
            time.sleep(1)
            cubesat.RGB = (0, 50, 0)
            time.sleep(1)
            cubesat.RGB = (0, 0, 50)
            time.sleep(1)
            self.assertEqual(cubesat.RGB[0], 0)
            self.assertEqual(cubesat.RGB[1], 0)
            self.assertEqual(cubesat.RGB[2], 50)
