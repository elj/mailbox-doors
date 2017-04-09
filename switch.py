#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import pygame
import doorsound

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# continuously print whether button is pressed or unpressed

##while True:
##    input_state = GPIO.input(18)
##    if input_state == False:
##        print('Button Pressed')
##        time.sleep(0.2)
##    else:
##        print('Button Unpressed')
##        time.sleep(0.2)

# prints "edge on channel" when state changes

##i=0
##while True:
##    detect = GPIO.wait_for_edge(18, GPIO.RISING)
##    i += 1
##
##    if detect is None:
##        print("Nothing")
##    else:
##        print(i, " Edge on channel ", detect)
##    time.sleep(0.5)

# waits for one edge change then exits

##try:
##    GPIO.wait_for_edge(18, GPIO.FALLING)
##    print("Edge detected")
##except KeyboardInterrupt:
##    GPIO.cleanup()
##GPIO.cleanup()


def my_callback(channel):
    time.sleep(0.1)
    if GPIO.input(18):
        print("Circuit open")
        doorsound.set_door_audio(1, True)
    else:
        print("Circuit closed")
        doorsound.set_door_audio(1, False)

GPIO.add_event_detect(18, GPIO.BOTH, callback=my_callback, bouncetime=1000)
my_callback(18)

# game loop
gameloop = True

print("number of channels = {}".format(pygame.mixer.get_num_channels()))



try:
    print("Detecting edges for 30 seconds")
    time.sleep(30)
    print("Ending now!")
finally:
    GPIO.cleanup()
    
