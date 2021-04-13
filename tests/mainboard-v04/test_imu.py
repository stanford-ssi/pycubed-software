# standard libraries
import time

# third-party libraries
import unittest

# pycubed libraries
from pycubed import cubesat


class TestIMU(unittest.TestCase):
    def test_get_values(self):
        print(cubesat.hardware)
        for i in range(3):
            print(
                "Acceleration: {} Magnetic Field: {} Rotation Rates: {} Temperature {}C".format(
                    cubesat.acceleration,
                    cubesat.magnetic,
                    cubesat.gyro,
                    cubesat.temperature,
                )
            )
