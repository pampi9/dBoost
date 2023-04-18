import sys

import pytest

from dboost.analyzers.utils import Stats
from dboost.analyzers.statistical import Pearson
import argparse

PEARSON_PARAMETERS = ["1"]


def mock_sys_argv():
    return ["main.py", "--statistical"] + PEARSON_PARAMETERS


def test_const__cords():
    assert Pearson.ID == "statistical"


def test_cls__pearson__register(monkeypatch):
    monkeypatch.setattr(sys, "argv", mock_sys_argv())
    parser = argparse.ArgumentParser(add_help=False)
    Pearson.register(parser)
    args = parser.parse_args()
    assert args.statistical == PEARSON_PARAMETERS


def test_cls__pearson__from_parse():
    pearson = Pearson.from_parse(PEARSON_PARAMETERS)
    # pearson is instance of Pearson
    assert isinstance(pearson, Pearson)
    # attributes of cords are correctly set
    assert pearson.corr_threshold == float(PEARSON_PARAMETERS[0])
    assert pearson.mask is None
    assert pearson.hints == []
    assert pearson.stats is None
    assert pearson.pearsons == {}
    assert pearson.pairwise_prods is None


@pytest.mark.parametrize(
    ("s1_items", "s2_items", "expected_output"),
    [
        ([1, 2, 3], [1, 3, 3], -6.062177826491074),
        ([1, 3, 3], [1, 3, 3], -6.1250000000000115),
    ],
)
def test_fct__pearson(s1_items, s2_items, expected_output):
    pearson = Pearson(0.5)
    s1 = Stats()
    for item in s1_items:
        s1.update(item)
    s2 = Stats()
    for item in s2_items:
        s2.update(item)
    pearson.stats = {"ABC": {True: s1, False: s2}, "DEF": {True: s2, False: s2}}
    pearson.pairwise_prods = {(("ABC", True), ("DEF", False)): 0}
    assert pearson.pearson((("ABC", True), ("DEF", False))) == expected_output


def test_fct__fit(data_stream_numerical, stats_stream_numerical):
    def stream():
        for item in data_stream_numerical:
            yield item

    pearson = Pearson(1)
    pearson.fit(stream())
    for (key1, stats) in enumerate(pearson.stats):
        for (key2, stat) in enumerate(stats):
            print(stat)
            if isinstance(stat, Stats):
                assert stat.count == stats_stream_numerical[key1][key2]["count"]
                assert stat.sum == stats_stream_numerical[key1][key2]["sum"]
                assert stat.sum2 == stats_stream_numerical[key1][key2]["sum2"]
                assert stat.min == stats_stream_numerical[key1][key2]["min"]
                assert stat.max == stats_stream_numerical[key1][key2]["max"]
                assert stat.elems == stats_stream_numerical[key1][key2]["elems"]
    assert pearson.pairwise_prods == {
        ((0, 0), (1, 0)): 123,
        ((0, 0), (1, 1)): 1970,
        ((0, 0), (1, 2)): 1,
        ((0, 0), (1, 3)): 1,
        ((0, 0), (1, 4)): 0,
        ((0, 0), (1, 5)): 2,
        ((0, 0), (1, 6)): 3,
        ((0, 0), (1, 7)): 3,
        ((0, 0), (1, 8)): 1,
        ((0, 0), (1, 9)): 0,
        ((0, 0), (1, 10)): 1,
        ((0, 0), (1, 11)): 1,
        ((0, 0), (1, 12)): 0,
        ((0, 0), (1, 13)): 1,
        ((0, 0), (1, 14)): 1,
        ((0, 0), (1, 15)): 1,
        ((0, 0), (1, 16)): 1,
        ((0, 0), (1, 17)): 0,
        ((0, 0), (1, 18)): 3,
        ((0, 1), (1, 0)): 0,
        ((0, 1), (1, 1)): 0,
        ((0, 1), (1, 2)): 0,
        ((0, 1), (1, 3)): 0,
        ((0, 1), (1, 4)): 0,
        ((0, 1), (1, 5)): 0,
        ((0, 1), (1, 6)): 0,
        ((0, 1), (1, 7)): 0,
        ((0, 1), (1, 8)): 0,
        ((0, 1), (1, 9)): 0,
        ((0, 1), (1, 10)): 0,
        ((0, 1), (1, 11)): 0,
        ((0, 1), (1, 12)): 0,
        ((0, 1), (1, 13)): 0,
        ((0, 1), (1, 14)): 0,
        ((0, 1), (1, 15)): 0,
        ((0, 1), (1, 16)): 0,
        ((0, 1), (1, 17)): 0,
        ((0, 1), (1, 18)): 0,
        ((0, 2), (1, 0)): 0,
        ((0, 2), (1, 1)): 0,
        ((0, 2), (1, 2)): 0,
        ((0, 2), (1, 3)): 0,
        ((0, 2), (1, 4)): 0,
        ((0, 2), (1, 5)): 0,
        ((0, 2), (1, 6)): 0,
        ((0, 2), (1, 7)): 0,
        ((0, 2), (1, 8)): 0,
        ((0, 2), (1, 9)): 0,
        ((0, 2), (1, 10)): 0,
        ((0, 2), (1, 11)): 0,
        ((0, 2), (1, 12)): 0,
        ((0, 2), (1, 13)): 0,
        ((0, 2), (1, 14)): 0,
        ((0, 2), (1, 15)): 0,
        ((0, 2), (1, 16)): 0,
        ((0, 2), (1, 17)): 0,
        ((0, 2), (1, 18)): 0,
        ((0, 3), (1, 0)): 0,
        ((0, 3), (1, 1)): 0,
        ((0, 3), (1, 2)): 0,
        ((0, 3), (1, 3)): 0,
        ((0, 3), (1, 4)): 0,
        ((0, 3), (1, 5)): 0,
        ((0, 3), (1, 6)): 0,
        ((0, 3), (1, 7)): 0,
        ((0, 3), (1, 8)): 0,
        ((0, 3), (1, 9)): 0,
        ((0, 3), (1, 10)): 0,
        ((0, 3), (1, 11)): 0,
        ((0, 3), (1, 12)): 0,
        ((0, 3), (1, 13)): 0,
        ((0, 3), (1, 14)): 0,
        ((0, 3), (1, 15)): 0,
        ((0, 3), (1, 16)): 0,
        ((0, 3), (1, 17)): 0,
        ((0, 3), (1, 18)): 0,
        ((0, 4), (1, 0)): 144987531414,
        ((0, 4), (1, 1)): 189730,
        ((0, 4), (1, 2)): 549,
        ((0, 4), (1, 3)): 2460,
        ((0, 4), (1, 4)): 1295,
        ((0, 4), (1, 5)): 3513,
        ((0, 4), (1, 6)): 2634,
        ((0, 4), (1, 7)): 464,
        ((0, 4), (1, 8)): 16292,
        ((0, 4), (1, 9)): 91,
        ((0, 4), (1, 10)): 24,
        ((0, 4), (1, 11)): 17,
        ((0, 4), (1, 12)): 49,
        ((0, 4), (1, 13)): 45,
        ((0, 4), (1, 14)): 45,
        ((0, 4), (1, 15)): 73,
        ((0, 4), (1, 16)): 17,
        ((0, 4), (1, 17)): 0,
        ((0, 4), (1, 18)): 604,
        ((0, 5), (1, 0)): 0,
        ((0, 5), (1, 1)): 0,
        ((0, 5), (1, 2)): 0,
        ((0, 5), (1, 3)): 0,
        ((0, 5), (1, 4)): 0,
        ((0, 5), (1, 5)): 0,
        ((0, 5), (1, 6)): 0,
        ((0, 5), (1, 7)): 0,
        ((0, 5), (1, 8)): 0,
        ((0, 5), (1, 9)): 0,
        ((0, 5), (1, 10)): 0,
        ((0, 5), (1, 11)): 0,
        ((0, 5), (1, 12)): 0,
        ((0, 5), (1, 13)): 0,
        ((0, 5), (1, 14)): 0,
        ((0, 5), (1, 15)): 0,
        ((0, 5), (1, 16)): 0,
        ((0, 5), (1, 17)): 0,
        ((0, 5), (1, 18)): 0,
        ((0, 6), (1, 0)): 0,
        ((0, 6), (1, 1)): 0,
        ((0, 6), (1, 2)): 0,
        ((0, 6), (1, 3)): 0,
        ((0, 6), (1, 4)): 0,
        ((0, 6), (1, 5)): 0,
        ((0, 6), (1, 6)): 0,
        ((0, 6), (1, 7)): 0,
        ((0, 6), (1, 8)): 0,
        ((0, 6), (1, 9)): 0,
        ((0, 6), (1, 10)): 0,
        ((0, 6), (1, 11)): 0,
        ((0, 6), (1, 12)): 0,
        ((0, 6), (1, 13)): 0,
        ((0, 6), (1, 14)): 0,
        ((0, 6), (1, 15)): 0,
        ((0, 6), (1, 16)): 0,
        ((0, 6), (1, 17)): 0,
        ((0, 6), (1, 18)): 0,
    }
    assert pearson.mask == (
        (True, True, True, True, True, True, True),
        (
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        ),
    )
    assert pearson.hints == [((0, 0), (1, 2)), ((0, 4), (1, 7)), ((0, 4), (1, 8))]
