import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(12,GPIO.IN)

input = GPIO.input(12)

while True:
	if (GPIO.input(12)):
		print("Button Pressed")

