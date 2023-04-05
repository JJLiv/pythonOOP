"""Word Finder sub-class: finds random words from a dictionary. and also
    excludes comments or blank lines"""

from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    def __init__(self, path) -> None:
        super().__init__(path)
        
    def getWords(self, txt_file):
        return [w.strip() for w in txt_file if w.strip() and not w.startswith("#")]

