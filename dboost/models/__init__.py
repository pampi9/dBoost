from .discrete import Histogram
from .discretepart import PartitionedHistogram
from .gaussian import Simple
from .mixture import Mixture

ALL = lambda: (Simple, Histogram, Mixture, PartitionedHistogram)
