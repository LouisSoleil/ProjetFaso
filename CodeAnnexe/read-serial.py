#!/usr/bin/env python
import time
import serial

ser=serial.Serial( #brancher arduino sur port usb en bas a gauche
	port='/dev/ttyACM0',
	baudrate=9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
)
counter=0
while 1:
	#time.sleep(3)
	x=ser.readline()
	#return x
	print x

