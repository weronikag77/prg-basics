# Write a program that calculates the average speed of a vehicle. 
# Enter from the keyboard: a distance in km, a number of travel hours and a number of travel minutes. 
# Define and use an anonymous function avg_speed(distance,hours,minutes) to calculate the result. 

distance = int(input("Enter the distance in km: "))
hours = int(input("Enter the number of travel hours: "))
minutes = int(input("Enter the number of travel minutes: "))

avg_speed = lambda distance,hours,minutes: distance/(minutes + 60*hours)*60

print(f"Average speed: {avg_speed(distance,hours,minutes)}")