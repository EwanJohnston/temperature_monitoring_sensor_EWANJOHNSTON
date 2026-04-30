##import modules and libraries##

import time
from w1thermsensor import W1ThermSensor, Unit
from gpiozero import LED, Buzzer
import matplotlib
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

## Create variables for sensors and connect to GPIO pins##
sensor=W1ThermSensor()
red= LED(18)
blue = LED (24)
buzzer = Buzzer(22)
current_datetime= datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        
        


def Data_Collection(xs,ys): ## data collection function##

    while True:
        temp_c=sensor.get_temperature(Unit.DEGREES_C) ## converts temperature gathered from sensor to celsius##
        
        
        print(temp_c, "Celsius")
        print(current_datetime)
        
        
        time.sleep(1)

        ##creates alerts for users within temperature parameters##
        if temp_c <30 and temp_c >=20:
            red.on()
            blue.off()
            buzzer.off()
        elif temp_c >=30 and temp_c <40:
            red.off()
            blue.on()
            buzzer.off()
        elif temp_c >=40:
            red.off()
            blue.off()
            buzzer.on()
        else:
            red.off()
            blue.off()
            buzzer.off()
            
        ##runs other functions in the loop ##
        tempGraph(xs,ys,temp_c)
        DataStorage(temp_c,current_datetime)

        


