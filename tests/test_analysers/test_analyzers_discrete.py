import argparse
import sys

from dboost.analyzers.discrete import DiscreteStats
from dboost.analyzers.statistical import Pearson
from dboost.analyzers.utils import Stats

DISCRETE_STATS_PARAMETERS = ["8", "2"]  # p < 1/sqrt(2*pi)


def mock_sys_argv():
    return ["main.py", "--discretestats"] + DISCRETE_STATS_PARAMETERS


def test_const__discrete_stats():
    assert DiscreteStats.ID == "discretestats"


def test_cls__discrete_stats__register(monkeypatch):
    monkeypatch.setattr(sys, "argv", mock_sys_argv())
    parser = argparse.ArgumentParser(add_help=False)
    DiscreteStats.register(parser)
    args = parser.parse_args()
    assert args.discretestats == DISCRETE_STATS_PARAMETERS


def test_cls__discrete_stats__from_parse():
    discrete_stats = DiscreteStats.from_parse(DISCRETE_STATS_PARAMETERS)
    # discrete_stats is instance of DiscreteStats
    assert isinstance(discrete_stats, DiscreteStats)
    # attributes of discrete_stats are correctly set
    assert discrete_stats.max_buckets == int(DISCRETE_STATS_PARAMETERS[0])
    assert discrete_stats.fundep_size == int(DISCRETE_STATS_PARAMETERS[1])
    assert discrete_stats.histograms is None
    assert discrete_stats.stats is None
    assert discrete_stats.hints is None


def test_fct__fit(data_stream_numerical, stats_stream_numerical):
    def stream():
        for item in data_stream_numerical:
            yield item

    discrete_stats = DiscreteStats(
        max_buckets=int(DISCRETE_STATS_PARAMETERS[0]), fundep_size=int(DISCRETE_STATS_PARAMETERS[1])
    )
    discrete_stats.fit(stream())
    assert discrete_stats.hints == (
        ((0, 0), (1, 1)),
        ((0, 0), (1, 2)),
        ((0, 0), (1, 3)),
        ((0, 0), (1, 4)),
        ((0, 0), (1, 7)),
        ((0, 0), (1, 8)),
        ((0, 0), (1, 9)),
        ((0, 0), (1, 10)),
        ((0, 0), (1, 11)),
        ((0, 0), (1, 12)),
        ((0, 0), (1, 13)),
        ((0, 0), (1, 14)),
        ((0, 0), (1, 15)),
        ((0, 0), (1, 16)),
        ((0, 0), (1, 17)),
        ((0, 0), (1, 18)),
        ((0, 1), (1, 1)),
        ((0, 1), (1, 2)),
        ((0, 1), (1, 3)),
        ((0, 1), (1, 4)),
        ((0, 1), (1, 7)),
        ((0, 1), (1, 8)),
        ((0, 1), (1, 9)),
        ((0, 1), (1, 10)),
        ((0, 1), (1, 11)),
        ((0, 1), (1, 12)),
        ((0, 1), (1, 13)),
        ((0, 1), (1, 14)),
        ((0, 1), (1, 15)),
        ((0, 1), (1, 16)),
        ((0, 1), (1, 17)),
        ((0, 1), (1, 18)),
        ((0, 2), (1, 1)),
        ((0, 2), (1, 2)),
        ((0, 2), (1, 3)),
        ((0, 2), (1, 4)),
        ((0, 2), (1, 7)),
        ((0, 2), (1, 8)),
        ((0, 2), (1, 9)),
        ((0, 2), (1, 10)),
        ((0, 2), (1, 11)),
        ((0, 2), (1, 12)),
        ((0, 2), (1, 13)),
        ((0, 2), (1, 14)),
        ((0, 2), (1, 15)),
        ((0, 2), (1, 16)),
        ((0, 2), (1, 17)),
        ((0, 2), (1, 18)),
        ((0, 3), (1, 1)),
        ((0, 3), (1, 2)),
        ((0, 3), (1, 3)),
        ((0, 3), (1, 4)),
        ((0, 3), (1, 7)),
        ((0, 3), (1, 8)),
        ((0, 3), (1, 9)),
        ((0, 3), (1, 10)),
        ((0, 3), (1, 11)),
        ((0, 3), (1, 12)),
        ((0, 3), (1, 13)),
        ((0, 3), (1, 14)),
        ((0, 3), (1, 15)),
        ((0, 3), (1, 16)),
        ((0, 3), (1, 17)),
        ((0, 3), (1, 18)),
        ((0, 4), (1, 1)),
        ((0, 4), (1, 2)),
        ((0, 4), (1, 3)),
        ((0, 4), (1, 4)),
        ((0, 4), (1, 7)),
        ((0, 4), (1, 8)),
        ((0, 4), (1, 9)),
        ((0, 4), (1, 10)),
        ((0, 4), (1, 11)),
        ((0, 4), (1, 12)),
        ((0, 4), (1, 13)),
        ((0, 4), (1, 14)),
        ((0, 4), (1, 15)),
        ((0, 4), (1, 16)),
        ((0, 4), (1, 17)),
        ((0, 4), (1, 18)),
        ((0, 5), (1, 1)),
        ((0, 5), (1, 2)),
        ((0, 5), (1, 3)),
        ((0, 5), (1, 4)),
        ((0, 5), (1, 7)),
        ((0, 5), (1, 8)),
        ((0, 5), (1, 9)),
        ((0, 5), (1, 10)),
        ((0, 5), (1, 11)),
        ((0, 5), (1, 12)),
        ((0, 5), (1, 13)),
        ((0, 5), (1, 14)),
        ((0, 5), (1, 15)),
        ((0, 5), (1, 16)),
        ((0, 5), (1, 17)),
        ((0, 5), (1, 18)),
        ((0, 6), (1, 1)),
        ((0, 6), (1, 2)),
        ((0, 6), (1, 3)),
        ((0, 6), (1, 4)),
        ((0, 6), (1, 7)),
        ((0, 6), (1, 8)),
        ((0, 6), (1, 9)),
        ((0, 6), (1, 10)),
        ((0, 6), (1, 11)),
        ((0, 6), (1, 12)),
        ((0, 6), (1, 13)),
        ((0, 6), (1, 14)),
        ((0, 6), (1, 15)),
        ((0, 6), (1, 16)),
        ((0, 6), (1, 17)),
        ((0, 6), (1, 18))
    )
