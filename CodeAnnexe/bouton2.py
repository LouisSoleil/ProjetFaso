import time
import grovepi
potentiometer = 0
grovepi.pinMode(potentiometer,"INPUT")
full_angle = 50

while True:
    sensor_value = grovepi.analogRead(potentiometer)
    print ((int)((sensor_value)/10))
    time.sleep(0.8)
    
    
