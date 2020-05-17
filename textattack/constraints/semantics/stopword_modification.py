""" Abstract classes represent constraints on text adversarial examples. 
"""

from textattack.shared.utils import default_class_repr
from textattack.transformations import WordSwap
from textattack.constraints import ModificationConstraint

class StopwordModification(ModificationConstraint):
    """ 
    A constraint disallowing the modification of stopwords
    """
   
    def _get_modifiable_indices(self, tokenized_text):
        """ Returns the word indices in x which are able to be deleted """
        try:
            return set(range(len(tokenized_text.words))) - tokenized_text.attack_attrs['stopword_indices'] 
        except KeyError:
            raise KeyError('`stopword_indices` in attack_attrs required for StopwordDeletion constraint.')


    def check_compatibility(self, transformation):
        """ 
        Checks if this constraint is compatible with the given transformation.
        Args:
            transformation: The transformation to check compatibility with.
        """
        return isinstance(transformation, WordSwap) 
