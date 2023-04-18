import argparse
import sys

import pytest

from dboost.models.gaussian import Simple
from dboost.analyzers.discrete import DiscreteStats

SIMPLE_PARAMETERS = ["1.5"]


def mock_sys_argv():
    return ["main.py", "--gaussian"] + SIMPLE_PARAMETERS


def test_const__simple():
    assert Simple.ID == "gaussian"


def test_cls__simple__register(monkeypatch):
    monkeypatch.setattr(sys, "argv", mock_sys_argv())
    parser = argparse.ArgumentParser(add_help=False)
    Simple.register(parser)
    args = parser.parse_args()
    assert args.gaussian == SIMPLE_PARAMETERS


def test_cls__simple__from_parse():
    simple = Simple.from_parse(SIMPLE_PARAMETERS)
    # simple is instance of Simple
    assert isinstance(simple, Simple)
    # attributes of simple are correctly set
    assert simple.tolerance == float(SIMPLE_PARAMETERS[0])
    assert simple.model is None


@pytest.mark.skip
def test_fct__fit(data_stream_numerical, stats_stream_numerical):
    def stream():
        for item in data_stream_numerical:
            yield item

    discrete_stats = DiscreteStats(max_buckets=8, fundep_size=2)
    discrete_stats.fit(stream())
    discrete_stats.expand_stats()
    simple = Simple(tolerance=float(SIMPLE_PARAMETERS[0]))
    simple.fit(stream(), discrete_stats)
    assert simple.hints == (
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
        ((0, 6), (1, 18)),
    )
