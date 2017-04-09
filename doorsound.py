#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Name:    010_sound_only_no_graphic.py
Purpose: demonstrate use of pygame for playing sound & music
URL:     http://ThePythonGameBook.com 
Author:  Horst.Jens@spielend-programmieren.at
Licence: gpl, see http://www.gnu.org/licenses/gpl.html

works with pyhton3.4 and python2.7
"""

#the next line is only needed for python2.x and not necessary for python3.x
from __future__ import print_function, division

import pygame
import os
import sys
import time

# if using python2, the get_input command needs to act like raw_input:
if sys.version_info[:2] <= (2, 7):
    get_input = raw_input
else:
    get_input = input # python3
    
### custom variables for this file ###


# set number of desired asynchronous channels (referenced later in mixer setup)
number_of_channels = 8

# set final fadeout time
exitfade = 1000

### end custom variables ###
    
### functions and stuff go here ###

	
# the REAL way to get the number of channels a sound is playing on
def get_num_active_channels(sound):
    """
    Returns the number of pygame.mixer.Channel that are actively playing the sound. 
    http://stackoverflow.com/questions/17534247/pygame-sound-get-num-channels-not-accurate
    """
    active_channels = 0
    if sound.get_num_channels() > 0:
        for i in range(pygame.mixer.get_num_channels()):
            channel = pygame.mixer.Channel(i)
            if channel.get_sound() == sound and channel.get_busy():
                active_channels += 1
    print("actually detected active channels = {}".format(active_channels))
    return active_channels
	
# process a door changing state
def toggle_door(d):
    if d > (len(doors)-1):
        print("door not found!")
        return
        
    num_active = get_num_active_channels(doors[d][0])
    if num_active > 0:
        print("toggling door {} OFF because it is playing on {} channels".format(d, num_active))
        doors[d][0].fadeout(doors[d][1])        # expects milliseconds
    else:
        ch = doors[d][0].play(loops=doors[d][2])
        print("toggling door {} ON, channel {}".format(d, ch))
    # TODO: more door-audio toggling goes here #

def set_door_audio(d, desired_state):
    if d > (len(doors)-1):
        print("door not found!")
    if(desired_state):
        if get_num_active_channels(doors[d][0]) > 0:
            print("already playing door", d)
        else:
            print("playing door", d)
            doors[d][0].play(loops=doors[d][2])
    else:
        print("stopping door", d)
        doors[d][0].fadeout(doors[d][1])
    
	
# work-in-progress for making fades nicer
def fade_down_attempt(sound, target_level, fade_ms):
    i = sound.get_volume()
    step_time = (i - target_level)/fade_ms
    print("step time = {}".format(step_time))
    while i > target_level:
        i -= 0.01
        # sound.set_volume(i)
        time.sleep(fade_ms) # expects seconds
        print(i)
    

### end functions ###

pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag

pygame.init()						#initialize pygame - this is where terrible things happen
pygame.mixer.set_num_channels(number_of_channels)	# must come *after* .init

# look for sound & music files in subfolder 'data'
#pygame.mixer.music.load(os.path.join('data', 'loophole.wav'))#load music
jump = pygame.mixer.Sound(os.path.join('data','jump.wav'))  #load sound
fail = pygame.mixer.Sound(os.path.join('data','fail.wav'))  #load sound

###		LOAD DOOR SOUNDS HERE	###

# door = sound,                                                     fadeout_ms, loops]

door0 = [pygame.mixer.Sound(os.path.join('data','fail.wav')),       0,          0]
door1 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door2 = [pygame.mixer.Sound(os.path.join('data','jump2.wav')),      100,        0]
door3 = [pygame.mixer.Sound(os.path.join('data','1-Prologue.wav')),       100,        0]
door4 = [pygame.mixer.Sound(os.path.join('data','kanye.wav')),   100,        0]
door5 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door6 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door7 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door8 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door9 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door10 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),  100,        0]
door11 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),  100,        0]
door12 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door13 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door14 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door15 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door16 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door17 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door18 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door19 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door20 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door21 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door22 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door23 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door24 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door25 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door26 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door27 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door28 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door29 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]
door30 = [pygame.mixer.Sound(os.path.join('data','loophole.wav')),   100,        0]

doors = [door0, door1, door2, door3, door4, door5, door6, door7, door8, door9, door10,
         door11, door12, door13, door14, door15, door16, door17, door18, door19, door20,
         door21, door22, door23, door24, door25, door26, door27, door28, door29, door30]

###		END LOAD DOOR SOUNDS	###

f = [1.0,	0.99,	0.98,	0.97,	0.96,	0.95,	0.94,	0.93,	0.92,	0.91,
	0.90,	0.89,	0.88,	0.87,	0.86,	0.85,	0.84,	0.83,	0.82,	0.81,	
	0.80,	0.79,	0.78,	0.77,	0.76,	0.75,	0.74,	0.73,	0.72,	0.71,	
	0.70,	0.69,	0.68,	0.67,	0.66,	0.65,	0.64,	0.63,	0.62,	0.61,	
	0.60,	0.59,	0.58,	0.57,	0.56,	0.55,	0.54,	0.53,	0.52,	0.51,	
	0.50,	0.49,	0.48,	0.47,	0.46,	0.45,	0.44,	0.43,	0.42,	0.41,	
	0.40,	0.39,	0.38,	0.37,	0.36,	0.35,	0.34,	0.33,	0.32,	0.31,	
	0.30,	0.29,	0.28,	0.27,	0.26,	0.25,	0.24,	0.23,	0.22,	0.21,	
	0.20,	0.19,	0.18,	0.17,	0.16,	0.15,	0.14,	0.13,	0.12,	0.11,
	0.10,	0.09,	0.08,	0.07,	0.06,	0.05,	0.04,	0.03,	0.02,	0.01,	0.00]

print("number of channels = {}".format(pygame.mixer.get_num_channels()))

### game loop goes here
