import pytest

from dboost.utils.autoconv import autoconv


@pytest.mark.parametrize(
    ("field", "floats_only", "return_value"),
    [
        ("1.1", True, 1.1),
        ("1.1", False, 1.1),
        ("a", True, "a"),
        ("a", False, "a"),
        (True, True, True),
        (False, False, False),
    ],
)
def test_fct__autovconv(field, floats_only, return_value):
    test_fct__autovconv.__test_type__ = "fct"
    assert autoconv(field=field, floats_only=floats_only) == return_value
