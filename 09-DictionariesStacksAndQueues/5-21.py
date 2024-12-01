# Create a dictionary that describes your favorite book or movie with at least five key-value pairs. 
# Then, create a program that writes the dictionary data to the favourite.json file.
import json

movie = {
    "title": "Promising. Young. Woman",
    "director": "Emerald Fennell",
    "year of release": 2020,
    "Oscar": True,
    "main actress": "Carey Mulligan"

}

favorite_file = "favorite.json"

with open(favorite_file, "w", encoding="utf-8") as file:
    json.dump(movie, file, indent=4)
