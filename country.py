from song import Song

class Country(Song): 
    def __init__(self, title: str artist : str, slower_speed: str):
    super(). __init__("title", "artist")
    self.slower_speed = slower_speed
    
    def add_slower_speed (self, *arg):
        for arg in args:
            self._slower_speed.append(arg)

        
    


    