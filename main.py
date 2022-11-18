import time
from gpiozero import LED


class Board():
    def __init__(self, pinnumber:int) -> None:
        self.led = LED(pinnumber)
    def blink(self):
        self.led.on()
        time.sleep(0.5)
        self.led.off()
        time.sleep(0.5)