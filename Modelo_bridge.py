#Bridge
'''
Juan Carlos Rangel
25/11/2019
it allows to decouple an abstraction from its implementation,
so that both can vary independently.
'''
from abc import ABC, abstractmethod

class Anime(ABC):
    @abstractmethod
    def GenreAnime(self):
        pass

class GenreAnime(ABC):
    def __init__(self, anime):
        self.anime = anime

    @abstractmethod
    def manga(self):
        pass
#------------------------------------------------#
    
class Shounen(GenreAnime):
    def __init__(self, anime):
        super(Shounen, self).__init__(anime)

    def manga(self):
        print("Anime selected is genre Shounen: ")
        self.anime.GenreAnime(self)
        
#------------------------------------------------#
        
class Fantasy(GenreAnime):
    def __init__(self, anime):
        super(Fantasy, self).__init__(anime)

    def manga(self):
        print("Game selected is genre Fantasy: ")
        self.anime.GenreAnime(self)
        
#------------------------------------------------#
        
class MartialArts(GenreAnime):
    def __init__(self, anime):
        super(MartialArts, self).__init__(anime)

    def manga(self):
        print("Game selected is genre MartialArts: ")
        self.anime.GenreAnime(self)

#------------------------------------------------#
        
class Romance(GenreAnime):
    def __init__(self, anime):
        super(Romance, self).__init__(anime)

    def manga(self):
        print("Game selected is genre MartialArts: ")
        self.anime.GenreAnime(self)
        
#------------------------------------------------#
        
class Hero(Anime):
    def GenreAnime(self):
        print("Anime selected is Boku No Hero Academy")

class Sword(Anime):
    def GenreAnime(self):
        print("Anime selected is Sword Art Online")

class Dragon(Anime):
    def GenreAnime(self):
        print("Anime selected is Dragon Ball Z")

class Lie(Anime):
    def GenreAnime(self):
        print("Anime selected is Your Lie in April")

#------------------------------------------------#

def main():
    anime1 = Shounen(Hero)
    anime1.manga()
    
    print("\n")

    anime2 = Fantasy(Sword)
    anime2.manga()

    print("\n")

    anime3 = MartialArts(Dragon)
    anime3.manga()

    print("\n")

    anime4 = Romance(Lie)
    anime4.manga()
    
if __name__ == "__main__":
   main()

