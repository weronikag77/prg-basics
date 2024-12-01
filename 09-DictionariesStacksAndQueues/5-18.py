#Write a program that prints information about dogs younger than 5 years.

import json

with open("dogs.json", "r", encoding="utf-8") as file:
    data = json.load(file)

for i in range(len(data)):
    for key, item in data[i].items():
        if data[i]["age"] < 5:
            print(f"{key}: {item}")