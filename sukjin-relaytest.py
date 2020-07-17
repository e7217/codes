##################################################

#           P26 ----> Relay_Ch1
#			P20 ----> Relay_Ch2
#			P21 ----> Relay_Ch3

##################################################
#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

###hello

Relay_Ch1 = 26
# Relay_Ch2 = 20
# Relay_Ch3 = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Relay_Ch1,GPIO.OUT)
# GPIO.setup(Relay_Ch2,GPIO.OUT)
# GPIO.setup(Relay_Ch3,GPIO.OUT)

print("Setup The Relay Module is [success]")

try:
	# A접전 및 B접점 구분자 mode
	mode = 'a'

	# B접점
	if mode == 'b':

		#Control the Channel 1
		GPIO.output(Relay_Ch1,GPIO.LOW)
		print("Channel 1:The Common Contact is access to the Normal Open Contact!")
		time.sleep(0.5)

		GPIO.output(Relay_Ch1,GPIO.HIGH)
		print("Channel 1:The Common Contact is access to the Normal Closed Contact!\n")
		time.sleep(0.5)

	# A접점
	elif mode == 'a':

		#Control the Channel 1
		GPIO.output(Relay_Ch1,GPIO.LOW)
		print("Channel 1:The Common Contact is access to the Normal Open Contact!")
		time.sleep(0.5)

		GPIO.output(Relay_Ch1,GPIO.HIGH)
		print("Channel 1:The Common Contact is access to the Normal Closed Contact!\n")
		time.sleep(0.5)

	GPIO.cleanup()
		
except:
	print("except")
	GPIO.cleanup()
