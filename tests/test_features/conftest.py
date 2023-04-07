import pytest


@pytest.fixture
def unknow_rule():
    def invalid_rule():
        pass

    yield {"fct": invalid_rule, "name": "invalid_rule"}
