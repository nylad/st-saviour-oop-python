from song import Song

class Rap(Song):
    def __init__(self, title: str, artist: str, special_guests: list):
        super().__init__(title, artist)
        self.special_guests = special_guests

    def add_special_guests(self, *args):
        for arg in args:
            self.special_guests.append(arg)