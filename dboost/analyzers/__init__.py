# Pearson (in statistical) is reused in cords => statistical must be imported for cords
from .statistical import Pearson
from .cords import Cords
from .discrete import DiscreteStats

ALL = lambda: (Pearson, DiscreteStats, Cords)
