from machine import Pin
from machine import ADC
from time import sleep_ms

pin = Pin(34)
adc=ADC(pin)
adc.atten(ADC.ATTN_11DB)
while True:
    val1=adc.read()
    val2=3.3*val1/4095
    print('Raw value: ',val1,' and voltage: ',val2)
    sleep_ms(1000)
    


