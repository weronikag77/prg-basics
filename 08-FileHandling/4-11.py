#Write a program that calculates, prints, and saves to a text file integers from 1 to 100 
#and their second and third powers. Sample result:
#1,1,1
#2,4,8

powers_file = "powers.txt"

with open(powers_file, "a") as file:
    for i in range(1,101):
        power1 = i*1
        power2 = i*i
        power3 = i*i*i
        file.write(f"{power1}, {power2}, {power3}\n")
