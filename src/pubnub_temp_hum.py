#!/usr/bin/python

import sys
import signal
import Adafruit_DHT
import time
import pdb
from pubnub import Pubnub


class Room:
   def __init__ (self, name, temp, humididy):
       self.Name = name
       self.Temperature = temp
       self.Humidity = humididy

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    global stopScript
    stopScript = True

def callback(message, channel):
    print(message)
  
  
def error(message):
    print("ERROR : " + str(message))
  
  
def connect(message):
    print("CONNECTED")
  
def reconnect(message):
    print("RECONNECTED")
  
  
def disconnect(message):
    print("DISCONNECTED")
  
#main
global stopScript
stopScript = False
signal.signal(signal.SIGINT, signal_handler)

pubnub = Pubnub(publish_key="pub-c-55470b0a-fe27-4763-b774-3aa63111fee0", subscribe_key="sub-c-783f7138-b7bd-11e6-91e2-02ee2ddab7fe")
channelName='home_channel'

time.sleep(10)

while True:
   humdity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
   humdity -= 7
   room = Room('bedroom', round(temperature,2), round(humdity,2))
   pubnub.publish(channel=channelName,  message=room.__dict__)
   print ("Send message to pubnub")
   print (room.__dict__)
   time.sleep(300)
   if stopScript:
      break

	  
