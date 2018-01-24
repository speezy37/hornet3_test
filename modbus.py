#!/usr/bin/env python
import minimalmodbus
import time

instrument = minimalmodbus.Instrument('/dev/ttyUSB0',1)
minimalmodbus.BAUDRATE = 19200
#print instrument

#value = instrument.read_registers(30,4,3)
#value = instrument.read_registers(30,4,3)
#print value

while True:
	instrument.write_register(0,1550,0,6,False)
	print "RUN 1"
	time.sleep(1)

	instrument.write_register(0,1500,0,6,False)
	print "STOP 1"
	time.sleep(1)

	instrument.write_register(1,1550,0,6,False)
	print "RUN 2"
	time.sleep(1)

	instrument.write_register(1,1500,0,6,False)
	print "STOP 2"
	time.sleep(1)

	instrument.write_register(2,1550,0,6,False)
	print "RUN 3"
	time.sleep(1)

	instrument.write_register(2,1500,0,6,False)
	print "STOP 3"
	time.sleep(1)

	instrument.write_register(3,1550,0,6,False)
	print "RUN 4"
	time.sleep(1)

	instrument.write_register(3,1500,0,6,False)
	print "STOP 4"
	time.sleep(1)

	instrument.write_register(4,1550,0,6,False)
	print "RUN 5"
	time.sleep(1)

	instrument.write_register(4,1500,0,6,False)
	print "STOP 5"
	time.sleep(1)

	instrument.write_register(5,255,0,6,False)
	print "SERVO END"
	time.sleep(1)

	instrument.write_register(5,0,0,6,False)
	print "SERVO START"
	time.sleep(1)

#instrument.write_register(5,1550,0,6,False)
#print "RUN 5"
#time.sleep(1)

#instrument.write_register(5,1500,0,6,False)
#print "STOP 5"
#time.sleep(1)

#print instrument.read_float(0,3,2)
