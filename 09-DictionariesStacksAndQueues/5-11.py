# Voting results are saved in the voting.json file with the structure below. 
# The program takes a person's name from the keyboard and increases the number of 
# votes for that person by 1. If this is a new person, they are added to the 
# list with a vote count of 1. You can run the program multiple times to add additional votes to 
# the json file.

#{
#   person_name: number of votes,
#   person_name: number of votes,
#   ...
#   ...
#}

import json


data = {

}

# Read the contents of the json file


# Vote for a person
person_name = 1
while person_name != "0":
    person_name = input('Name of the person you are voting for: ')
    with open('voting.json', 'a', encoding="utf-8") as f:
        if person_name in data:
            data[person_name] += 1
        elif person_name not in data and person_name != "0":
            data[person_name] = 1
        else:
            break
with open('voting.json', 'a', encoding="utf-8") as f:      
    json.dump(data, f)
print(data)




    