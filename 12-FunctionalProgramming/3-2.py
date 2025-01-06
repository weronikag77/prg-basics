#text
text = "I completely agree with you"
text_list = text.split(" ")

number_of_letters = list(map(lambda item: len(item), text_list))
print(f"Number of letters in each word: {number_of_letters}")