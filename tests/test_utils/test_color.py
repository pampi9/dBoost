import pytest

from dboost.utils.color import highlight, term, underline


@pytest.fixture
def msg():
    yield "sample_msg"


@pytest.mark.parametrize(("val1", "val2"), [("first", "secound")])
def test_const__template(val1, val2):
    test_const__template.__test_type__ = "const"
    assert term.TEMPLATE.format(val1, val2) == f"[{val1};{val2}m"


@pytest.mark.parametrize(("val1"), [("first")])
def test_const__colorless_template(val1):
    test_const__colorless_template.__test_type__ = "const"
    assert term.COLORLESS_TEMPLATE.format(val1) == f"[{val1}m"


def test_fct__highlight(msg):
    test_fct__highlight.__test_type__ = "fct"
    assert (
        highlight(msg=msg)
        == f"{term.RESET}{term.TEMPLATE.format(term.BOLD, term.RED)}{msg}{term.RESET}"
    )


def test_fct__underline(msg):
    test_fct__underline.__test_type__ = "fct"
    assert (
        underline(msg=msg)
        == f"{term.RESET}{term.COLORLESS_TEMPLATE.format(term.UNDERLINE)}{msg}{term.RESET}"
    )
