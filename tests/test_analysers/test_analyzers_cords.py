import argparse
import sys

from dboost.analyzers.cords import Cords
from dboost.analyzers.statistical import Pearson
from dboost.analyzers.utils import Stats

CORDS_PARAMETERS = ["8", "0.3"]  # p < 1/sqrt(2*pi)


def mock_sys_argv():
    return ["main.py", "--cords"] + CORDS_PARAMETERS


def test_const__cords():
    assert Cords.ID == "cords"


def test_cls__cords__register(monkeypatch):
    monkeypatch.setattr(sys, "argv", mock_sys_argv())
    parser = argparse.ArgumentParser(add_help=False)
    Cords.register(parser)
    args = parser.parse_args()
    assert args.cords == CORDS_PARAMETERS


def test_cls__cords__from_parse():
    cords = Cords.from_parse(CORDS_PARAMETERS)
    # cords is instance of Cord
    assert isinstance(cords, Cords)
    # attributes of cords are correctly set
    assert cords.p == float(CORDS_PARAMETERS[1])
    assert cords.delta == 0.005
    assert cords.hints == []
    assert cords.stats is None
    # attribute pearson is correctly set
    assert isinstance(cords.pearson, Pearson)
    assert cords.pearson.corr_threshold == float(CORDS_PARAMETERS[0])
    assert cords.pearson.mask is None
    assert cords.pearson.hints == []
    assert cords.pearson.stats is None
    assert cords.pearson.pearsons == {}
    assert cords.pearson.pairwise_prods is None


def test_fct__fit(data_stream_numerical, stats_stream_numerical):
    def stream():
        for item in data_stream_numerical:
            yield item

    cords = Cords(corr_threshold=float(CORDS_PARAMETERS[0]), p=float(CORDS_PARAMETERS[1]))
    cords.fit(stream())
    for (key1, stats) in enumerate(cords.pearson.stats):
        for (key2, stat) in enumerate(stats):
            print(key1, key2, stat)
            if isinstance(stat, Stats):
                assert stat.count == stats_stream_numerical[key1][key2]["count"]
                assert stat.sum == stats_stream_numerical[key1][key2]["sum"]
                assert stat.sum2 == stats_stream_numerical[key1][key2]["sum2"]
                assert stat.min == stats_stream_numerical[key1][key2]["min"]
                assert stat.max == stats_stream_numerical[key1][key2]["max"]
                assert stat.elems == stats_stream_numerical[key1][key2]["elems"]
    assert cords.hints == [
        ((0, 0), (1, 0)),
        ((0, 0), (1, 1)),
        ((0, 0), (1, 2)),
        ((0, 0), (1, 3)),
        ((0, 0), (1, 4)),
        ((0, 0), (1, 5)),
        ((0, 0), (1, 6)),
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
        ((0, 0), (1, 18)),
        ((0, 4), (1, 0)),
        ((0, 4), (1, 1)),
        ((0, 4), (1, 2)),
        ((0, 4), (1, 3)),
        ((0, 4), (1, 4)),
        ((0, 4), (1, 5)),
        ((0, 4), (1, 6)),
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
        ((0, 4), (1, 18))
    ]
