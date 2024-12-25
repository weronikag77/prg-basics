# An object representing an employee contains the following data: name, surname, age, and seniority 
# (the number of years worked). Define a C class that allows you to create an object. 
# Provide employee data at the time of creating the object, in the given order. 
# Define a text representation of an object in the class that contains a string of 
# last name, first letter of first name, and seniority. If the employee is an adult 
# (at least 18 years old), use uppercase letters, otherwise lowercase letters. Sample result:

#C("Anna","May",17,7) returns "maya7"
#C("George","Brown",21,4) returns "BROWNG4"

class C():
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority
        self.letters = []
    def text(self):
        self.letters.append(self.surname)
        self.letters.append(self.name[0])
        self.letters.append(str(self.seniority))
        result = "".join(self.letters)
        if self.age < 18:
            result = result.lower()
        else:
            result = result.upper()
        print(result)

def main():
    string = C("George","Brown",21,4)
    string.text()

if __name__ =="__main__":
   main()