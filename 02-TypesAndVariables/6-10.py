###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# display number of characters
print('Number of characters: ', len(movie))

# display title in capital letters
title_uppercase = movie.upper()
print(title_uppercase)

# display title in small letters
title_lowercase = movie.lower()
print(title_lowercase)

# display how many times the vowel "e" appears in the title
e_number = movie.count('e')
print(e_number)

# display where in the text is the word "Lord"
place_lord = movie.find('Lord')
print(place_lord)

# display where in the text is the word "dragon"
place_dragon = movie.find('dragon')
print(place_dragon)