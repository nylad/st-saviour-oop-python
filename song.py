# Song Class
class Song:
    def __init__(self, title: str, artist: str):
        self.title = title 
        self.artist = artist 

    
    def play(self):
        return self.title + ' by ' + self.artist + ' plays'

        


    
