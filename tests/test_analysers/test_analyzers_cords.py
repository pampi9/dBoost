import sys

from dboost.analyzers.cords import Cords
from dboost.analyzers.statistical import Pearson
import argparse

CORDS_PARAMETERS = ["1", "0.5"]


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


