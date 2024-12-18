#Genres Class
class Genre:
    def __init__(self, title: str, artist: str):
        self.title = title 
        self.artist = artist 

    
    def play(self):
        print(self.title + ' by ' + self.artist + ' plays')


    
