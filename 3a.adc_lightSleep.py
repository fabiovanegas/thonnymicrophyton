from machine import lightsleep
from machine import Pin
from machine import ADC
from time import sleep

pin = Pin(34)
adc=ADC(pin)
adc.atten(ADC.ATTN_11DB)
led = Pin (2, Pin.OUT)      #GPIO2 as output for
button = Pin (0, Pin.IN)
print('Going into Light Sleep Mode')
while True:
    val1=adc.read()
    val2=3.3*val1/4095
    print('Raw value: ',val1,' and voltage: ',val2)
    led.value(1)                 #LED is ON
    sleep(1)                     #delay of 1 second
    led.value(0)
    if button.value()==0:
        break
    lightsleep(1000)     #10000ms sleep time
    


