# standard libraries
import board
import busio
import time

# third-party libraries
import unittest
import adafruit_tcs34725
import bq25883
import bmx160
import adm1176


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

    def test_internal_I2C_devices(self):
        # initialize internal I2C pins
        i2c = busio.I2C(board.SCL,board.SDA)
        # print out addresses of all i2C device addresses
        i2c.try_lock()
        scan = i2c.scan()
        print("I2C scan:")
        for address in scan:
            print(hex(address))
        i2c.unlock()

        # try to initialize usb
        USB = bq25883.BQ25883(i2c)
        print("USB INITIALIZED SUCCESSFULLY at ", hex(USB.i2c_addr))
        # try to initialize power monitor
        PWR = adm1176.ADM1176(i2c)
        print("POWER MONITOR SUCCESSFULLY at ", hex(PWR.i2c_addr))
        # try to initialize IMU
        IMU = bmx160.BMX160_I2C(i2c)
        print("IMU SUCCESSFULLY at ", hex(IMU.i2c_addr))

        ## print IMU data
        # for i in range(50):
        #     print(IMU.accel, " --- ", IMU.mag, " --- ", IMU.gyro, " --- ", IMU.temperature)
        #     time.sleep(1)
