# Define a class constructor that allows you to set the initial values of the music piece (artist, track title, album, year) 
# when the object is created. Complete the class with the __str__ method returning the song data as a string, in the format as below (4 lines). 
# Then, create two objects that represent two pieces of music and print their data. 

class Song():
    def __init__(self, artist, title, album, year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year
    
    def __str__(self):
        return f"Artist: {self.artist}, \nTitle: {self.title}, \nAlbum: {self.album}, \nYear: {self.year}"

song1 = Song("Taylor Swift", "Call It What You Want", "Reputation", 2017)
song2 = Song("Noah Kahan", "Dial Drunk", "Stick Season", 2023)

print(song1)
print(song2)