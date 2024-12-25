# from 34.0 to 42.0 degrees Celsius, with an accuracy of 0.1 degrees. 
# Write a program in which define a class that describes the states and behaviors 
# of the thermometer. The thermometer should enable temperature measurement 
# (do it by generating a random number from the 34.0 to 42.0 range) and display the measured value. 
# If the temperature is at least 37 degrees Celsius, the thermometer should additionally 
# display the 'Fever' message
import random

class thermometer():
    def __init__(self):
        self.temperature = 0
        self.fever = False
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False
        
    def measure_temperature(self):
        temperature = random.uniform(34.0, 42.0)
        self.temperature = round(temperature, 1)
        if self.temperature < 37:
            self.fever = False
        else:
            self.fever = True
    
    def display_status(self):
        if self.is_on == True:
            if self.fever == False:
                print(f"Temperature: {self.temperature} C")
            else:
                print(f"Temperature: {self.temperature} C, fever")
        else:
            print("The thermometer is off.")
