import json

# Open the JSON file in read mode
with open("cities.json", "r", encoding="utf-8") as file:
    data = json.load(file)

for i in range(len(data)):
    for key, value in data[i].items():
        print(f"{key}: {value}")