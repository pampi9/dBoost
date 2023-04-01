from .cords import Cords
from .discrete import DiscreteStats
from .statistical import Pearson

ALL = lambda: (Pearson, DiscreteStats, Cords)
