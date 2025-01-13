from song import Song

class Rap(Song):
    def __init__(self, title: str, artist: str, special_guests: list):
        super().__init__(title, artist)
        self.special_guests = special_guests

    def add_special_guests(self, *args):
        for arg in args:
            self.special_guests.append(arg)

    def play(self) -> str:
        return self.title + ' by ' + self.artist + ' plays with special guests: ' + str(self.special_guests)
    
    def __str__(self):
        return f'title: {self.title}, artist: {self.artist}, special guests: {str(self.special_guests)}'