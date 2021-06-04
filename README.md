# Telemetrix i2c Extensions

This repository contains i2c extension libraries for the
[Telemetrix](https://mryslab.github.io/telemetrix/)
project.

Each library consists of two classes, one to handle non-asyncio applications and the 
other to support asyncio applications.

There are no changes required on the Telemetrix servers.  

Because the Telemetrix i2c API is consistent across all Telemetrix clients, to convert an 
application from one hardware platform to another, only one or two lines need to be 
modified.

For example, to convert the telemetrix_pca.py example to run on an ESP8266, only the 
Telemetrix client instantiation line needed to be modified

From:
```python
# create a telemetrix instance
the_board = telemetrix.Telemetrix()

```
To:
```python
# create a telemetrix instance
# Change the ip address to match the ip address of your nodemcu

the_board = telemetrix.Telemetrix(ip_address='192.168.2.170')


```

Both asyncio and non-asyncio library classes are available.

Currently supported devices:

1. **PCA9685 Servo Driver**


