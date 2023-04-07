from dboost.features.utils import string_normalize


def test_fct__string_normalize():
    test_fct__string_normalize.__test_type__ = "fct"
    assert string_normalize("mon café") == "mon cafe"
