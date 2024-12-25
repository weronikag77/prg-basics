import thermometer

#Create a thermometer
def main():
    therm = thermometer.thermometer()


#Turn thermometer on
    therm.turn_on()
#Measure temperature
    therm.measure_temperature()
#Display temperature
    therm.display_status()
#Turn thermometer off
    therm.turn_off()


if __name__ =="__main__":
   main()

