#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import pygame
import doorsound

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

gpio_inputs = [4, 5, 22, 23]

GPIO.setup(gpio_inputs, GPIO.IN, pull_up_down=GPIO.PUD_UP)

gpio_to_doors = [0]*30
gpio_to_doors[22]= 2
gpio_to_doors[23]= 3
gpio_to_doors[4] = 4
gpio_to_doors[5] = 5


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
##    if detect is None: print("Nothing") else: print(i, " Edge on
##        channel ", detect) time.sleep(0.5)

# waits for one edge change then exits

##try:
##    GPIO.wait_for_edge(18, GPIO.FALLING)
##    print("Edge detected")
##except KeyboardInterrupt:
##    GPIO.cleanup()
##GPIO.cleanup()


def door_change_callback(channel):
    door = gpio_to_doors[channel]
    if (door == 0):
        print("Not a door!")
        return
    time.sleep(0.1)
    if GPIO.input(channel):
        print("Circuit open on door ", door)
        doorsound.set_door_audio(door, True)
    else:
        print("Circuit closed on door ", door)
        doorsound.set_door_audio(door, False)

for i in gpio_inputs:
    GPIO.add_event_detect(i, GPIO.BOTH, callback=door_change_callback, bouncetime=500)
    door_change_callback(i)

# game loop
gameloop = True

print("number of channels = {}".format(pygame.mixer.get_num_channels()))



try:
    print("Detecting edges for 300 seconds")
    time.sleep(300)
    print("Ending now!")
finally:
    GPIO.cleanup()
    
