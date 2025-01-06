# Define an anonymous function initials(name,surname) 
# that returns the first letters of the name and surname.

initials = lambda name,surname: f"{name[0]}{surname[0]}"

print(initials("Abcd", "Efgh"))