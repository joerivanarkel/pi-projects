import time
from gpiozero import LED

ledtest = LED(17)

while True:
    ledtest.on()
    time.sleep(0.5)
    ledtest.off()
    time.sleep(0.5)