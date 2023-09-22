#This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
# import webrepl
# webrepl.start()
from machine import deepsleep
from machine import Pin
from machine import ADC
from machine import RTC
from time import sleep

pin = Pin(34)
adc=ADC(pin)
adc.atten(ADC.ATTN_11DB)
led = Pin (2, Pin.OUT)      #GPIO2 as output for
button = Pin (0, Pin.IN)


val1=adc.read()
val2=3.3*val1/4095
print('Raw value: ',val1,' and voltage: ',val2)
led.value(1)                 #LED is ON
sleep(1)                     #delay of 1 second
led.value(0)
if button.value()==1:
    deepsleep(1000)     #10000ms sleep time
    print('Modo sueño profundo')
    


