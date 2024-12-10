# The class should contain one boolean attribute called is_on that specifies whether the TV set is turned on. 
# Initially, the TV is turned off. 
# Add turn_on() and turn_off() methods in the class to turn the TV on and off, respectively. 
# Also, add a show_status() method to print whether the TV is on or off. 

# tv.py file
# class definition
class TV():
    def __init__(self):
        self.is_on = False
    def turn_off(self):
        self.is_on = False
    def turn_on(self):
        self.is_on = True

    def show_status(self):
        if self.is_on == True:
            print("The TV is on")
        else:
            print("The TV is off")

def main():
    my_tv = TV()
    my_tv.turn_on()
    my_tv.show_status()

if __name__ =="__main__":
    main()
