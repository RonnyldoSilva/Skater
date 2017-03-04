from .global_interpretation.partial_dependence import PartialDependence
from .local_interpretation.local_interpreter import LocalInterpreter
from ..data.dataset import DataSet


# Create based on class name:
class Interpretation(object):
    '''
    Returns an interpretation class.

    Parameters:
    -----------
        interpretation_type(string): pdp, lime

    Returns:
    ----------
        interpretation subclass
    '''

    def __init__(self):
        self.local_interpreter = LocalInterpreter(self)
        self.partial_dependence = PartialDependence(self)
        self.data_set = None

    def consider(self, training_data, feature_names=None, index=None):
        self.data_set = DataSet(training_data, feature_names=feature_names, index=index)
