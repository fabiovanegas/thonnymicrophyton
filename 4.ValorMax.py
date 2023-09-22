from machine import lightsleep
from machine import Pin
from machine import ADC
from machine import RTC
from time import sleep

# Configuración del pin ADC y LED
pin = Pin(34)
adc = ADC(pin)
button = Pin (0, Pin.IN)
adc.atten(ADC.ATTN_11DB)
led = Pin(2, Pin.OUT)  # GPIO2 como salida para el LED

# Configuración de la RAM RTC para almacenar el valor máximo
rtc = RTC()
rtcData=rtc.memory()
rtcData=bin(0)
rtc.memory(rtcData)
print('Valor inicial almacenado',rtcData)

while True:
    # Leer el valor del sensor
    val1 = adc.read()
    hex_value = rtc.memory()
    
    # Convierte el valor hexadecimal a decimal
    val3 = int(hex_value)

    # Obtener el valor máximo de las mediciones
    #max_value = rtc.memory()
    
    if val1 > val3:
        val3=val1
    
    
        rtcData=bin(val1)
        rtc.memory(rtcData)
        print('voltaje de entrada:', val1, ' and voltage maximo:', val3)   
        
        val=rtc.memory()
    

    led.value(1)  # Encender el LED
    sleep(1)  # Esperar 1 segundo
    led.value(0)  # Apagar el LED
    print('voltaje de entrada:', val1, ' and voltage max:', val3)
    if button.value() == 1:
       
        lightsleep(1000)  # Dormir durante 1000ms
