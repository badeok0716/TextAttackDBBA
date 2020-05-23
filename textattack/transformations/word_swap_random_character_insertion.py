import numpy as np

from textattack.shared import utils
from textattack.transformations.word_swap import WordSwap

class WordSwapRandomCharacterInsertion(WordSwap):
    """ Transforms an input by inserting a random character.

        Args:
            random_one (bool): Whether to return a single word with a random 
                character deleted. If not, returns all possible options.
    """
    def __init__(self, random_one=True, **kwargs):
        super().__init__(**kwargs)
        self.random_one = random_one

    def _get_replacement_words(self, word):
        """ Returns returns a list containing all possible words with 1 random
            character inserted.
        """
        if len(word) <= 1:
            return []
            
        candidate_words = []

        if self.random_one:
            i = np.random.randint(0, len(word))
            candidate_word = word[:i] + self._get_random_letter() + word[i:]
            candidate_words.append(candidate_word)
        else:
            for i in range(len(word)):
                candidate_word = word[:i] + self._get_random_letter() + word[i:]
                candidate_words.append(candidate_word)

        return candidate_words
