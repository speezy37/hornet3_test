#!/usr/bin/env python
import minimalmodbus
import time

instrument = minimalmodbus.Instrument('/dev/ttyUSB0',2)
minimalmodbus.BAUDRATE = 19200
#print instrument

#value = instrument.read_registers(30,2,3)
while True:
  #now = time.time()
  value = instrument.read_float(15,3,2)
  print "Pressure: " , value , " Bar"

  time.sleep(0.1)
  '''
  later = time.time()

  difference = float(later - now)
  print(difference)
  '''

  rax = instrument.read_float(0,3,2)
  print "rax: " , rax
  time.sleep(0.1)
  ray = instrument.read_float(2,3,2)
  print "ray: " , ray
  time.sleep(0.1)
  raz = instrument.read_float(4,3,2)
  print "raz: " , raz
  time.sleep(0.1)
  rgx = instrument.read_float(6,3,2)
  print "rgx: " , rgx
  time.sleep(0.1)
  rgy = instrument.read_float(8,3,2)
  print "rgy: " , rgy
  time.sleep(0.1)
  rgz = instrument.read_float(10,3,2)
  print "rgz: " , rgz
  time.sleep(0.1)
  mx = instrument.read_register(12,0,3,True)
  print "mx: " , mx
  time.sleep(0.1)
  my = instrument.read_register(13,0,3,True)
  print "my: " , my
  time.sleep(0.1)
  mz = instrument.read_register(14,0,3,True)
  print "mz: " , mz
  time.sleep(0.1)
  depth = instrument.read_float(17,3,2)
  print "depth: ", depth
  time.sleep(0.1)

  #time.sleep(0.2)
