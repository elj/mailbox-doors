import time
import pygame
import doorsound as ds
import os
import sys

# game loop
gameloop = True

print("number of channels = {}".format(pygame.mixer.get_num_channels()))

while gameloop:

    # print menu 
    
    answer = input("Now {} tracks are playing.\ntype a door # 1-8, or q to stop all: ".format(pygame.mixer.get_busy()))

    
    try:
            val = int(answer)
            print("N")
            ds.toggle_door(val)
            continue
    except ValueError:
            print("NaN")
            #answer = answer.lower() # force lower case
            
    if "a" in answer:
        ds.jump.play(fade_ms=2000)
        print("playing jump.wav once")
    elif "b" in answer:
        ds.fail.play()
        print("playing fail.wav once")
            
    elif "f" in answer:
        ds.fade_down_attempt(door1[0], 0.5, 5000)
    elif "r" in answer:
        ds.door1[0].set_volume(1.0)
            
#     elif "m" in answer:
#         if pygame.mixer.music.get_busy():
#             pygame.mixer.music.stop()
#         else:
#             pygame.mixer.music.play()
    elif "q" in answer:
        #nicely fade out playing sounds
        pygame.mixer.fadeout(ds.exitfade)           # expects milliseconds
        # pygame.mixer.music.fadeout(exitfade)  # expects milliseconds
        time.sleep(ds.exitfade/1000)                # expects seconds
        #break from gameloop
        gameloop = False
    else:
        print("that is not a thing :(")
		
#     print("{} tracks are playing".format(pygame.mixer.get_busy()))

print("bye-bye")
GPIO.cleanup()
pygame.quit() # clean exit
