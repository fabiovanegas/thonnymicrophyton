from machine import Pin
import _thread
#This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
# import webrepl
# webrepl.start()

import time
from machine import ADC
from machine import deepsleep

BUTTON=0
# Lock to avoid race condition when accessing the flag
myLock = _thread.allocate_lock()

# Flag to control threads execution
flag = True
boton = Pin(BUTTON, Pin.IN)
# Function to simulate sensor measurements
def sensor_measurement():
    cuenta=0
    while True:
        if flag:
            pin = Pin(34)
            adc=ADC(pin)
            mediciones = adc.read()
            print("Medición del sensor:", mediciones)
            print(cuenta)
            cuenta=cuenta+1
        time.sleep(1)

# Function to read user button and control sensor measurement printing
def control_sensor_printing():
   
    global flag
    status=0
    while True:
        #user_input = input("Press Enter to start/stop sensor measurement printing: ")
        if status==0:
            if boton.value() == 0:
                status=1
        
        else:
            if boton.value() == 1:
                status=0
            
                myLock.acquire()
                flag = not flag  # Toggle the flag
                myLock.release()
                
        time.sleep(0.01)

# Start Thread1 for sensor measurements
_thread.start_new_thread(sensor_measurement, ())

# Start Thread2 for controlling sensor measurement printing
_thread.start_new_thread(control_sensor_printing, ())

# Main thread is an endless loop
while True:
    pass
print('Im awake, but Im going to sleep')
#sleep for 1 second (1000 milliseconds)

if button.value()==0:
    deepsleep(1000)
