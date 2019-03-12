import RPi.GPIO as GPIO
from time import sleep
import requests
from pygame import mixer 
 
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(8,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16,GPIO.OUT, initial=GPIO.LOW)
state = 0
while True:
	genesys = GPIO.input(8)
	armagedom = GPIO.input(10)
	if (genesys == False and state == 0):
            #try:
                print("Chamando API genesys")
                mixer.init()
                mixer.music.load('/home/pi/Desktop/genesys.mp3')
                mixer.music.play()
                response = requests.get("http://3.18.144.236:35000/genesys")
                print(response.text)
                #sleep(15)
                #music.music.stop()
                GPIO.output(12,1)
                GPIO.output(16,0)
                state = 1
                sleep(2)
                print("Supremo senhor do universo, qual o seu comando?")
                
            #except:
            #    pass
	elif (armagedom == False and state == 1):
		print("Chamando API armagedom")
		mixer.init()
		mixer.music.load('/home/pi/Desktop/armageddon.mp3')
		mixer.music.play()
		response = requests.get("http://3.18.144.236:35000/armageddon")
		print(response.text)
		GPIO.output(16,1)
		GPIO.output(12,0)
		state = 0
		sleep(2)
		print("Supremo senhor do universo, qual o seu comando?")