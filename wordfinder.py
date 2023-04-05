"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:
    """Class with list of words from a path to a file containing those words
        Also prints out the amount of words in the list
        Has a random method that prints out a random word from list
        
    """
    def __init__(self, path) -> None:
        """initialize instance and call necessary functions to get words and count"""
        txt_file = open(path)
        self.words = self.get_words(txt_file) 
        self.count = self.get_count()


    def get_words(self, txt_file):
        """read words from path and store in list"""
        return [w.strip() for w in txt_file]
    
    def get_count(self):
        return len(self.words)


    def random(self):
        """return random word from list"""
        return choice(self.words)

    # "C:\Users\jjcor\school_stuff\python-oo-practice\words.txt"