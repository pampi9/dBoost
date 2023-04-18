import argparse
import sys

import pytest

from dboost.analyzers.discrete import DiscreteStats
from dboost.models.mixture import Mixture

MIXTURE_PARAMETERS = ["2", "0.3"]


def mock_sys_argv():
    return ["main.py", "--mixture"] + MIXTURE_PARAMETERS


def test_const__mixture():
    assert Mixture.ID == "mixture"


def test_cls__mixture__register(monkeypatch):
    monkeypatch.setattr(sys, "argv", mock_sys_argv())
    parser = argparse.ArgumentParser(add_help=False)
    Mixture.register(parser)
    args = parser.parse_args()
    assert args.mixture == MIXTURE_PARAMETERS


def test_cls__histogram__from_parse():
    mixture = Mixture.from_parse(MIXTURE_PARAMETERS)
    # mixture is instance of Mixture
    assert isinstance(mixture, Mixture)
    # attributes of mixture are correctly set
    assert mixture.n_components == int(MIXTURE_PARAMETERS[0])
    assert mixture.cutoff == float(MIXTURE_PARAMETERS[1])

    assert mixture.gmms is None


@pytest.mark.skip
def test_fct__fit(data_stream_numerical, stats_stream_numerical):
    def stream():
        for item in data_stream_numerical:
            yield item

    discrete_stats = DiscreteStats(max_buckets=8, fundep_size=2)
    discrete_stats.fit(stream())
    discrete_stats.expand_stats()
    mixture = Mixture(
        n_components=int(MIXTURE_PARAMETERS[0]), cutoff=float(MIXTURE_PARAMETERS[1])
    )
    mixture.fit(stream(), discrete_stats)
    assert mixture.gmms == ()
