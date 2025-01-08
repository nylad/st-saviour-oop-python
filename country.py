from song import Song

class Country(Song): 
    def __init__(self, title: str artist : str) :
        super().__init__(title, artist)