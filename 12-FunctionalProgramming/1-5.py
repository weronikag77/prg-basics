# Write a program that calculates the average speed of a vehicle. 
# Enter from the keyboard: a distance in km, a number of travel hours and a number of travel minutes. 
# Define a function avg_speed(distance,hours,minutes) that returns the calculated average speed. 
# Sample result:

#Enter distance in km: 70
#Enter number of travel hours: 1
#Enter number of travel minutes: 23
#Average speed: 50.6 km/h 
distance = int(input("Enter the distance in km: "))
hours = int(input("Enter the number of travel hours: "))
minutes = int(input("Enter the number of travel minutes: "))

def avg_speed(distance,hours,minutes):
    
    minutes = minutes + 60*hours
    speed = distance/minutes*60
    return f"Average speed: {speed}"

print(avg_speed(distance, hours, minutes))