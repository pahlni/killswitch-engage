#!/usr/bin/env python3

import os
import time
from periphery import GPIO

# Init GPIO
led_out = GPIO(510, "out")
button_in = GPIO(511, "in")

# Set LED on
led_out.write(True)

# Wait on button press
while (True):
    time.sleep(0.03)
    value = button_in.read()
    if value == False:
        led_out.write(False)
        os.system('reboot')
