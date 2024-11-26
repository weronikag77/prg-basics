person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

#Displays name
print(person["name"])
#Displays hobby
print(person["hobby"])
#Displays the entire contents of the dictionary
print(person)
#Changes surname to 'Nowak'
person["surname"] = "Nowak"
#Changes person's marriage status
person["married"] = False
#Adds gender: 'male'
person["gender"] = "male"
#Adds a new hobby: 'bicycle'
person["hobby"].append("bicycle")
#Adds work phone to existing phones: '313131444'
person["phone"].update({"work":"313131444"})
#Displays the entire contents of the dictionary (iterate over dictionary items)
for item, value in person.items():
    print(item, value)