import bluetooth
import random
import time
from simpleBLE import BLEPeripheral
from machine import Pin
from machine import ADC

# Bluetooth object
ble = bluetooth.BLE() 

# Environmental service
service='4bbf2613-4959-433a-ad75-273b9db0cfe5' 

# Temperature characteristic
characteristic='445c218d-4ebb-4410-b292-6f8d21d2b04f' 

# BLE peripheral object
temp = BLEPeripheral(ble,"my",service,characteristic) 
pin = Pin(34)
adc=ADC(pin)
adc.atten(ADC.ATTN_11DB)
t = 0
i=0
while True:
    # Write every second, notify every 10 seconds.
    i = (i + 1) % 10
    t =adc.read()
    temp.set_values([int(t)], notify=i == 0, indicate=False)
    # Random walk the temperature.
    
    time.sleep_ms(1000)


