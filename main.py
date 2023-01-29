from machine import Pin, ADC
import time, dht
from Detector import *

BUZZER=Pin(25, Pin.OUT)
sensor = dht.DHT22(Pin(13))

pot = ADC(Pin(12))
pot.width(ADC.WIDTH_10BIT)
pot.atten(ADC.ATTN_11DB)


while True:
    hum = pot.read()
    sensor.measure()
    temp = sensor.temperature()
    print (hum)
    print (temp)
    x = Detector(temp, hum, BUZZER)
    print(x.calculate())
    x.buzz()
    time.sleep(2)