

<div style="text-align:center;color:#990033; font-family:times, serif; font-size:3.5em"><i>Telemetrix I2C Extensions</i></div>
<br>
Telemetrix was designed from the beginning to allow users to extend its hardware support.
An extension example is provided in the [User's Guide.](https://mryslab.
github.io/telemetrix/dht/)

Typically, when adding an extension, one makes modifications to both the client and 
server 
sides of Telemetrix.

The exception to this rule is for adding support for i2c devices.

The i2c standard describes a serial protocol for writing to and reading from an i2c 
device. This communication protocol is independent of the functionality that the 
device provides. For example, an i2c device that controls a set of servo motors is 
very different from an i2c device that reports accelerometer data. Even devices with very 
similar functionality often do not share anything in common other than the 
communication protocol.

For Telemetrix, each server implements the i2c protocol tailored for the 
MCU it supports, resident in the server.

As a result, all the control and monitoring code for i2c devices resides within 
the client.  Through the Telemetrix API, the client 
instructs the server to perform an i2c read or write, with no further
modifications to the server required.

There are two ways to support i2c in Telemetrix. The first is to incorporate the i2c 
control code directly within your application. For simple i2c devices, this is perfectly 
adequate, and in fact, the
[ADXL-345](https://github.com/MrYsLab/telemetrix/blob/master/examples/i2c_adxl345_accelerometer.py)
example demonstrates this.  

A separate library control class would be a better choice for more complex devices, 
allowing for reuse and application design simplification.
Because Telemetrix uses a consistent API across all client versions, 
a single i2c device interface class can support all Telemetrix clients. 
The only distinction is whether the class needs to support asyncio or non-asyncio Telemetrix clients.

For example, to support the PCA9685 Servo Driver device, there are two interface classes.
The first, 
[telemetrix_pca9685.py](https://github.com/MrYsLab/telemetrix-extensions/blob/master/telemetrix_pca9685/telemetrix_pca9685.py),
supports non-asyncio applications, and the second, 
[telemetrix_pca9685_aio.py,](https://github.com/MrYsLab/telemetrix-extensions/blob/master/telemetrix_pca9685/telemetrix_pca9685_aio.py)
supports asyncio applications.


[Examples](https://github.com/MrYsLab/telemetrix-extensions/tree/master/examples/pca9685)
are available to demonstrate the use of both of these classes. 

The examples support Arduino, ESP-8266, and the Raspberry Pico MCU devices.

## An Important Implementation Note

Programming the PCA9685, in some cases, requires performing an i2c read of one of the 
device's 
registers 
and then applying 
the result of that read to a write operation to set a register value. 
Telemetrix uses callbacks to receive the results of  i2c reads. Therefore, internally, 
callback functions 
are provided within the library to receive the read results and use the results to 
complete the operation.

Let's look at the _sleep_ method in telemetrix_pca9685.py.
The request for the data is in the code below:

```python
    def sleep(self):
        """
        Puts board into sleep mode.
        First performs a read, and then processes return
        in _i2c_read_complete_sleep.
        """
        self.board.i2c_read(self.i2c_address,
                            pca9685_constants.PCA9685_MODE1, 1,
                            self._i2c_read_complete_sleep)
        time.sleep(.5)
```
Notice that a callback method,  _i2c_read_complete_sleep, is specified. 
The value of the MODE1 register is required to place the device into sleep mode.


With the MODE1 value in hand, the callback method then places the device into a sleep mode.

```python

        def _i2c_read_complete_sleep(self, data):
        """
        Finish processing sleep command

        :param data: data from i2c device
        """
        # data is [i2c_read_report, port, number of bytes read, i2c address,
        #           device_register, data value, time_stamp]
        awake = data[5]
        # set sleep-bit high
        sleep_value = awake | pca9685_constants.MODE1_SLEEP

        self.board.i2c_write(self.i2c_address, [pca9685_constants.PCA9685_MODE1,
                                                sleep_value])
        time.sleep(.005)  # wait until cycle ends for sleep to be active
```

















<br>


Copyright (C) 2021 Alan Yorinks. All Rights Reserved.

**Last updated 8 June 2021 **

