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
from telemetrix_aio.
"""

import asyncio
import sys

from telemetrix_aio import telemetrix_aio

from telemetrix_pca9685 import telemetrix_pca9685_aio


class PcaAsyncExample:
    def __init__(self, servo_number, the_loop):

        self.servo_number = servo_number
        self.the_loop = the_loop

        # instantiate telemetrix
        self.the_board = telemetrix_aio.TelemetrixAIO(ip_address='192.168.2.170',
                                                      loop=self.the_loop)
        loop.run_until_complete(self.the_board.set_pin_mode_i2c())
        self.servo = telemetrix_pca9685_aio.TelemetrixPCA9685Aio(board=self.the_board,
                                                                 loop=self.the_loop)

    async def run_the_example(self):
        while True:
            try:
                # sweep in one direction using set_pwm
                for x in range(self.servo.position_min, self.servo.position_max):
                    await self.servo.set_pwm(self.servo_number, 0, x)
                await asyncio.sleep(.5)

                # sweep in other direction using set_pwm
                for x in range(self.servo.position_max, self.servo.position_min, -1):
                    await self.servo.set_pwm(self.servo_number, 0, x)
                await asyncio.sleep(.5)

                # set the servo to specific angles using set_angle
                await self.servo.set_angle(self.servo_number, 0)
                await asyncio.sleep(1)
                await self.servo.set_angle(self.servo_number, 90)
                await asyncio.sleep(1)
                await self.servo.set_angle(self.servo_number, 180)
                await asyncio.sleep(1)
                await self.servo.set_angle(self.servo_number, 0)
                await asyncio.sleep(1)
            except KeyboardInterrupt:
                await self.the_board.shutdown()
                sys.exit(0)


loop = asyncio.get_event_loop()

# to keep pep8 inspection happy
servo_run = None

try:
    servo_run = PcaAsyncExample(15, loop)
    loop.run_until_complete(servo_run.run_the_example())
except KeyboardInterrupt:
    if servo_run:
        loop.run_until_complete(servo_run.the_board.shutdown())
        sys.exit(0)
