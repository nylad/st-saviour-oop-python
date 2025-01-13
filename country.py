from song import Song

class Country(Song): 
    def __init__(self, title: str, artist : str, speed: int):
        super().__init__(title, artist)
        self.speed = speed

    def play(self):
        return self.title + ' by ' + self.artist + ' plays at speed: ' + str(self.speed)
