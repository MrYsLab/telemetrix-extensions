# noinspection GrazieInspection
"""
 Copyright (c) 2021 Alan Yorinks All rights reserved.

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
 along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

"""
This example demonstrates controlling a PCA9685 i2c servo driver board
from telemetrix.
"""


from telemetrix_pca9685 import telemetrix_pca9685
from telemetrix import telemetrix
import sys
import time

# create a telemetrix instance
# Change the ip address to match the ip address of your nodemcu

the_board = telemetrix.Telemetrix(ip_address='192.168.2.170')

# set i2c pin mode
the_board.set_pin_mode_i2c()

# create an instance of the pc9685 handler
servo = telemetrix_pca9685.TelemetrixPCA9685(board=the_board)

# servo number
SERVO = 15

while True:
    try:
        # sweep in one direction using set_pwm
        for x in range(servo.position_min, servo.position_max):
            servo.set_pwm(SERVO, 0, x)
        time.sleep(.5)

        # sweep in other direction using set_pwm
        for x in range(servo.position_max, servo.position_min, -1):
            servo.set_pwm(SERVO, 0, x)
        time.sleep(.5)

        # set the servo to specific angles using set_angle
        servo.set_angle(SERVO, 0)
        time.sleep(1)
        servo.set_angle(SERVO, 90)
        time.sleep(1)
        servo.set_angle(SERVO, 180)
        time.sleep(1)
        servo.set_angle(SERVO, 0)
        time.sleep(1)
    except KeyboardInterrupt:
        the_board.shutdown()
        sys.exit(0)
