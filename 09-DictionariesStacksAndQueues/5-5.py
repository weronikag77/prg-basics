#Write a program that counts how many times each word appears in a paragraph.

#Hint: Check the dictionary to see if the next word appears in it. 
#If so, increase the number of times the word appears by 1. 
#You can easily split a paragraph into individual words using the split() method.

paragraph = "cat dog mouse cat rat cat mouse"
paragraph = paragraph.split(" ")

dictionary = {

}

for item in paragraph:
    if item not in dictionary:
        dictionary[item] = 1
    else: 
        dictionary[item] += 1

print(dictionary)
