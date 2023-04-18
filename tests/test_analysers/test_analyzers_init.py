from dboost.analyzers import ALL, Pearson, DiscreteStats, Cords


def test_const__all():
    assert ALL() == (Pearson, DiscreteStats, Cords)
