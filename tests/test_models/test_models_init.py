from dboost.models import ALL, Simple, Histogram, Mixture, PartitionedHistogram


def test_const__all():
    assert ALL() == (Simple, Histogram, Mixture, PartitionedHistogram)
