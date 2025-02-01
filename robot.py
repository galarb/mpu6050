from mpu6050 import MPU6050  # Assuming the MPU6050 module is named mpu6050.py
from machine import I2C, Pin
from nahumtakum import NahumTakum
import time
from math import degrees, atan2

i2c = I2C(1, sda=Pin(17), scl=Pin(16), freq=100000)  
mpu = MPU6050(bus=i2c)


print(mpu.read_temperature())
print(mpu.calcangle())

for _ in range(500):
    mpu.update_angle()

    #print('gyro angle = ', mpu.(update_angle))
