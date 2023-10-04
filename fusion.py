from os import statvfs
from time import sleep
import network
from mqtt import MQTTClient 
import machine 
import time
import json
import bluetooth
import sys
from micropython import const
from machine import Pin
from machine import ADC
from simpleBLE import BLECentral

ble = bluetooth.BLE()

# Environmental service
service='4bbf2613-4959-433a-ad75-273b9db0cfe5'

# Temperature characteristic
characteristic='445c218d-4ebb-4410-b292-6f8d21d2b04f'

# BLE Central object
central = BLECentral(ble,service,characteristic)

not_found = False
USERNAME = const('IyoeKSkuNyk1LQsiOB80Jx8')
CLIENTID = const('IyoeKSkuNyk1LQsiOB80Jx8')
PASS = const('/q8ZhT3X+eRMTAw4zfEHT68g')
SERVER=const('mqtt3.thingspeak.com')
CHANNEL=const('2279520')

valor=0

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

def cambiar(data):
      counter=0;
      T=2
      try:     
        value = data        
        if (counter%T)==0:
            client.publish(topic="channels/2279520/publish", msg='field1='+str(value))   
            print("El valor de salida es",value)
        sleep(1)
        counter+=1
        client.check_msg();
      except OSError as e:
        print('Failed')
    
print('Inializando')

def on_scan(addr_type, addr, name):
    if addr_type is not None:
        print("Found sensor:", addr_type, addr, name)
        central.connect()
    else:
        global not_found
        not_found = True
        print("No sensor found.")

central.scan(callback=on_scan)

# Wait for connection...
while not central.is_connected():
    time.sleep_ms(100)
    if not_found:
        sys.exit()

print("Connected")

central.on_notify(callback= lambda data:print('Notified') )

# Explicitly issue reads, using "print" as the callback.
while central.is_connected():
    central.read(callback=lambda data: cambiar(data[0]))
    time.sleep_ms(2000)

# Alternative to the above, just show the most recently notified value.
# while central.is_connected():
#     print(central.value())
#     time.sleep_ms(2000)

print("Disconnected")






  
 
    


