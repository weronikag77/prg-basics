#A speed camera located in a city measures the speed of passing vehicles. 
# The maximum permitted speed of vehicles is 50 km/h. In the last minute, the speed camera 
# recorded the following values:

speed = [48,47,54,50,42,68,39,46]

too_high = list(filter(lambda item: True if item > 50 else False, speed))

print("Speed too high:",*too_high, sep=",")