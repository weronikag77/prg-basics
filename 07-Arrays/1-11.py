#Number of measurements:
#Average temperature in the month:
#Minimum temperature:
#Maximum temperature:
#Number of days with negative temperature:

temperatures = [
 3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
 4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
 -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]

measurements = len(temperatures)
print(f"Number of measurements: {measurements}")

sum = 0
for item in temperatures:
    sum += item

average_temp = sum/measurements
print(f"Average temperature in the month: {average_temp}")

minimum_temp = min(temperatures)
print(f'Minimum temperature: {minimum_temp}')

maximum_temp = max(temperatures)
print(f"Maximum temperature: {maximum_temp}")

sum_negative = 0
for item in temperatures:
    if item < 0:
        sum_negative += 1

print(f"Number of days with negative temperature: {sum_negative}")