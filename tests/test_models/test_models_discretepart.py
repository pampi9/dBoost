import argparse
import sys
from collections import Counter

import pytest

from dboost.analyzers.discrete import DiscreteStats
from dboost.models.discretepart import PartitionedHistogram

PARTITIONED_HISTOGRAM_PARAMETERS = ["5", "0.8", "0.05"]


def mock_sys_argv():
    return ["main.py", "--partitionedhistogram"] + PARTITIONED_HISTOGRAM_PARAMETERS


def test_const__partitioned_histogram():
    assert PartitionedHistogram.ID == "partitionedhistogram"


def test_cls__partitioned_histogram__register(monkeypatch):
    monkeypatch.setattr(sys, "argv", mock_sys_argv())
    parser = argparse.ArgumentParser(add_help=False)
    PartitionedHistogram.register(parser)
    args = parser.parse_args()
    assert args.partitionedhistogram == PARTITIONED_HISTOGRAM_PARAMETERS


def test_cls__partitioned_histogram__from_parse():
    partitioned_histogram = PartitionedHistogram.from_parse(PARTITIONED_HISTOGRAM_PARAMETERS)
    # partitioned_histogram is instance of PartitionedHistogram
    assert isinstance(partitioned_histogram, PartitionedHistogram)
    # attributes of partitioned_histogram are correctly set
    assert partitioned_histogram.jmp_threshold == float(PARTITIONED_HISTOGRAM_PARAMETERS[0])
    assert partitioned_histogram.peak_threshold == float(PARTITIONED_HISTOGRAM_PARAMETERS[1])
    assert partitioned_histogram.outlier_threshold == float(PARTITIONED_HISTOGRAM_PARAMETERS[2])

    assert partitioned_histogram.all_counters is None
    assert partitioned_histogram.counters is None
    assert partitioned_histogram.sizes is None


@pytest.mark.skip
def test_fct__fit(data_stream_numerical, stats_stream_numerical):
    def stream():
        for item in data_stream_numerical:
            yield item

    discrete_stats = DiscreteStats(max_buckets=8, fundep_size=2)
    discrete_stats.fit(stream())
    discrete_stats.expand_stats()
    partitioned_histogram = PartitionedHistogram(
        jmp_threshold=float(PARTITIONED_HISTOGRAM_PARAMETERS[0]),
        peak_threshold=float(PARTITIONED_HISTOGRAM_PARAMETERS[1]),
        outlier_threshold=float(PARTITIONED_HISTOGRAM_PARAMETERS[2]),
    )
    partitioned_histogram.fit(stream(), discrete_stats)
    assert partitioned_histogram.all_counters == (
        (
            Counter({False: 13, True: 1}), 
            Counter({False: 14}), 
            Counter({False: 14}), 
            Counter({False: 14}), 
            Counter({7: 13, 3: 1}), 
            Counter({False: 14}), 
            Counter({False: 14})
        ),
        (
            Counter({123: 1, 1593270896: 1, 1593271461: 1, 1593269744: 1, 1593269818: 1, 1593269669: 1, 1593271588: 1, 1593269166: 1, 1593269708: 1, 1593268409: 1, 1593268528: 1, 1593268492: 1, 1593268448: 1, 1593268508: 1}),
            Counter({2020: 13, 1970: 1}),
            Counter({6: 13, 1: 1}),
            Counter({27: 13, 1: 1}),
            Counter({14: 10, 15: 3, 0: 1}),
            Counter({55: 2, 35: 2, 34: 2, 2: 1, 14: 1, 24: 1, 56: 1, 54: 1, 26: 1, 46: 1, 33: 1}),
            Counter({8: 3, 29: 2, 28: 2, 3: 1, 56: 1, 21: 1, 44: 1, 58: 1, 6: 1, 52: 1}),
            Counter({5: 13, 3: 1}),
            Counter({179: 13, 1: 1}),
            Counter({True: 13, False: 1}),
            Counter({0: 10, 1: 4}),
            Counter({0: 11, 1: 3}),
            Counter({0: 7, 1: 7}),
            Counter({1: 7, 0: 7}),
            Counter({1: 7, 0: 7}),
            Counter({1: 11, 0: 3}),
            Counter({False: 11, True: 3}),
            Counter({False: 14}),
            Counter({8: 6, 6: 2, 9: 2, 3: 1, 1: 1, 4: 1, 2: 1})
        )
    )
    assert partitioned_histogram.counters == (
        (
            Counter({False: 13, True: 1}),
            Counter({False: 14}),
            Counter({False: 14}),
            Counter({False: 14}),
            Counter({7: 13, 3: 1}),
            Counter({False: 14}),
            Counter({False: 14})
        ),
        (
            None,
            Counter({2020: 13, 1970: 1}),
            Counter({6: 13, 1: 1}),
            Counter({27: 13, 1: 1}),
            None,
            None,
            None,
            Counter({5: 13, 3: 1}),
            Counter({179: 13, 1: 1}),
            Counter({True: 13, False: 1}),
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            Counter({False: 14}),
            None
        )
    )
    assert partitioned_histogram.sizes == (
        (14, 14, 14, 14, 14, 14, 14),
        (14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14)
    )
