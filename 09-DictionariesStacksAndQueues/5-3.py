translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

word  = input("Enter a word to translate: ")
for key, value in translations.items():
    if word == key:
        print(f"{key}: {value}")
    else:
        print("Translation unavailable.")