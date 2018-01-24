#!/usr/bin/env python
import minimalmodbus
import time

thruster = minimalmodbus.Instrument('/dev/ttyUSB0',1)
minimalmodbus.BAUDRATE = 19200

imu = minimalmodbus.Instrument('/dev/ttyUSB0',2)
minimalmodbus.BAUDRATE = 19200

value = imu.read_float(30,3,2)
print "Pressure: " , value , " Bar"
time.sleep(0.1)

thruster.write_register(0,1550,0,6,False)
print "OK"
time.sleep(0.1)

rax = imu.read_float(0,3,2)
print "rax: " , rax
time.sleep(0.1)

thruster.write_register(0,1500,0,6,False)
print "OK"
time.sleep(0.1)

ray = imu.read_float(4,3,2)
print "ray: " , ray
time.sleep(0.1)

thruster.write_register(1,1550,0,6,False)
print "OK"
time.sleep(0.1)

raz = imu.read_float(8,3,2)
print "raz: " , raz
time.sleep(0.1)

thruster.write_register(1,1500,0,6,False)
print "OK"
time.sleep(0.1)
