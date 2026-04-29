import time
from w1thermsensor import W1ThermSensor, Unit
from gpiozero import LED, Buzzer
import matplotlib
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
sensor=W1ThermSensor()
red= LED(18)
blue = LED (24)
buzzer = Buzzer(22)
current_datetime= datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        
        


def Data_Collection(xs,ys):

    while True:
        temp_c=sensor.get_temperature(Unit.DEGREES_C)
        
        
        print(temp_c, "Celsius")
        print(current_datetime)
        
        
        time.sleep(1)
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
            
        tempGraph(xs,ys,temp_c)
        DataStorage(temp_c,current_datetime)

        


