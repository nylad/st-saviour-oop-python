from abc import ABC, abstractmethod

# Song Class
class Song(ABC):
    def __init__(self, title: str, artist: str):
        self.title = title 
        self.artist = artist 

    @abstractmethod
    def play(self) -> str:
        pass

        


    
