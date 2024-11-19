#To calculate the number of words in a line, use the split() method, 
#which splits a string into a list where each word is a list item. 
#Then read the length of this list. Use the len() function. 
#Finally, sum the number of words in each line.
def read_from_file(name):
    with open(name, "r") as file:
        content = file.read()
    return content

file_content = read_from_file("pets.txt")

file_lines = file_content.splitlines()

sum = 0
for line in file_lines:
    sum += len(line)

print(sum)