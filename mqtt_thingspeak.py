from os import statvfs
from time import sleep
import network
from mqtt import MQTTClient 
import machine 
import time
import json
import random
from micropython import const
from machine import Pin
from machine import ADC

USERNAME = const('IyoeKSkuNyk1LQsiOB80Jx8')
CLIENTID = const('IyoeKSkuNyk1LQsiOB80Jx8')
PASS = const('/q8ZhT3X+eRMTAw4zfEHT68g')
SERVER=const('mqtt3.thingspeak.com')
CHANNEL=const('2279520')

def free_flash():
  s = statvfs('//')
  return ('{0} MB'.format((s[0]*s[3])/1048576))

# https://api.thingspeak.com/update?api_key=JGM08DVSS7Z3IX1U&field2=0
def sub_cb(topic, msg):
    print(msg[0])   
    if msg[0]==48:
       led.value(0)
    elif msg[0]==49:
        led.value(1)

print('Available flash memory: '+free_flash())


led=machine.Pin(2,machine.Pin.OUT)


client = MQTTClient(client_id=CLIENTID, server=SERVER,user=CLIENTID,password=PASS )
 

client.set_callback(sub_cb) 
client.connect()
client.subscribe(topic='channels/'+CHANNEL+'/subscribe/fields/field1')
pin = Pin(34)
adc=ADC(pin)
adc.atten(ADC.ATTN_11DB)
counter=0;
T=30
while True:
  try:  
 
    value = adc.read()
    
    if (counter%T)==0:
        client.publish(topic="channels/2279520/publish", msg='field1='+str(value))   
        print(value)
    sleep(1)
    counter+=1
    client.check_msg();
  except OSError as e:
    print('Failed')
