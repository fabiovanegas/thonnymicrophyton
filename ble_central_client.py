# This example finds and connects to a BLE temperature sensor (e.g. the one in ble_temperature.py).

import bluetooth
import random
import struct
import time
import sys
from simpleBLE import BLECentral 

# Bluetooth object
ble = bluetooth.BLE()

# Environmental service
service='4bbf2613-4959-433a-ad75-273b9db0cfe5'

# Temperature characteristic
characteristic='445c218d-4ebb-4410-b292-6f8d21d2b04f'

# BLE Central object
central = BLECentral(ble,service,characteristic)

not_found = False

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

central.on_notify(callback= lambda data :print('Notified') )

# Explicitly issue reads, using "print" as the callback.
while central.is_connected():
    central.read(callback=lambda data: print(data[0]))
    time.sleep_ms(2000)

# Alternative to the above, just show the most recently notified value.
while central.is_connected():
    print(central.value())
    time.sleep_ms(2000)

print("Disconnected")


