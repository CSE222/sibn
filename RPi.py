#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import requests
import random


GPIO.setmode(GPIO.BOARD)

tremor = 7;
#led = 13;

GPIO.setup(tremor, GPIO.IN)
#GPIO.setup(led, GPIO.OUT)

url = 'http://192.168.0.2:8000/readings/'
headers = {'content-type': 'application/json'}

while True:
	tremor = GPIO.wait_for_edge(tremor, GPIO.RISING)
	
	#GPIO.output(led, GPIO.HIGH)
	payload = {"sensor_id":2987 ,"sensor_type":"Tremor", "sensor_reading":"%.4f" % (0.9 + random.random()/10)}

	requests.post(url, json=payload, headers=headers)
	time.sleep(0.25);
	
	#GPIO.output(led,GPIO.LOW)


GPIO.cleanup()


