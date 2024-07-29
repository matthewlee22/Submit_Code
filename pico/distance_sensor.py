from hcsr04 import HCSR04
from machine import Pin

dist_sensor = HCSR04(trigger_pin=16, echo_pin=0)

def get_distance():
    distance = dist_sensor.distance_cm()
    return distance()


