#A variable contains text:

#An apple a day keeps the doctor away

#Create a module MyText, containing:

#1. A function that returns the number of words in the text
#2. A function that returns an ordered array of words, from longest to shortest
#3. A function that returns an alphabetically ordered array of words

words = "An apple a day keeps the doctor away"

def num_words(sentence):
    arr = sentence.split(" ")
    return len(arr)

print(num_words(words))

def sorted(sentence):
    arr = sentence.split(" ")
    arr.sort(key=len)
    return arr

print(sorted(words))    

def alphabet_order(sentence):
    arr = sentence.split(" ")
    arr.sort(key=str.lower)
    return arr

print(alphabet_order(words))  