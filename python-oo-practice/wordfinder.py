"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Machine for finding random words from a dictionary.
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, path):
        # read dict file and report number of items
        try:
            with open(path, 'r') as file:
                self.words = self.parse(file)
            print(f"{len(self.words)} words read")
        except FileNotFoundError:
            print(f"Error: The file '{path}' was not found.")
            self.words = []

    def parse(self, file):
        #  parses the file into a list of words 
        return [w.strip() for w in file]
    
    def random(self):
        #  returns a random word from the list 
        if not self.words:
            raise ValueError("No words available to choose from.")
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines and comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def parse(self, file):
        # parses the file into a list of words, skipping blank lines and comments
        return [w.strip() for w in file if w.strip() and not w.startswith('#')]
    

with open('words.txt', 'w') as f:
    f.write('cat\n')
    f.write('dog\n')
    f.write('porcupine\n')

with open('complex.txt', 'w') as f:
    f.write('# Comment line\n')
    f.write('pear\n')
    f.write('carrot\n')
    f.write('\n')
    f.write('kale\n')
    f.write('# Another comment\n')

#  assertions 
wf = WordFinder('words.txt')
assert len(wf.words) == 3, 'expected 3 words, but got a different number'
assert wf.random() in ['cat', 'dog', 'porcupine'], 'random word is not in the expected list'

swf = SpecialWordFinder('complex.txt')
assert len(swf.words) == 3, 'expected 3 words, but got a different number'
assert swf.random() in ['pear', 'carrot', 'kale'], 'random word is not in the expected list'